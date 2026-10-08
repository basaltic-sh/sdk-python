"""Build and verify clean, installable wheel and sdist from the public source."""

import hashlib
import os
import subprocess
import sys
import tarfile
import tempfile
import tomllib
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(*args, cwd=ROOT, env=None):
    subprocess.run(list(args), cwd=cwd, env=env, check=True)


def payload(wheel):
    with zipfile.ZipFile(wheel) as z:
        names = z.namelist()
        assert all(n.startswith(("basaltic/", "basaltic_sh_sdk_python-")) for n in names)
        assert all(
            not any(s in n for s in ["__pycache__", "AGENTS", "internal/", ".pyc"]) for n in names
        )
        assert "basaltic/py.typed" in names
        return {n: z.read(n) for n in names if n.startswith("basaltic/")}


def main():
    meta = tomllib.loads((ROOT / "pyproject.toml").read_text())["project"]
    assert meta["name"] == "basaltic-sh-sdk-python"
    version = meta["version"]
    assert (
        (ROOT / "src/basaltic/_version.py")
        .read_text()
        .strip()
        .endswith(f'__version__ = "{version}"')
    )
    if tag := os.environ.get("RELEASE_TAG"):
        # Public tags use SemVer; Python versions use the equivalent PEP 440 spelling.
        import re

        expected = re.sub(
            r"-(alpha|beta|rc)\.(\d+)$",
            lambda m: {"alpha": "a", "beta": "b", "rc": "rc"}[m[1]] + m[2],
            tag.removeprefix("v"),
        )
        assert expected == version, "Release tag does not match package version"
    with tempfile.TemporaryDirectory(prefix="python-package-") as directory:
        tmp = Path(directory)
        dist = tmp / "dist"
        env = dict(
            os.environ,
            SOURCE_DATE_EPOCH="1700000000",
            PIP_CONFIG_FILE=os.devnull,
            PIP_DISABLE_PIP_VERSION_CHECK="1",
        )
        env.pop("PYTHONPATH", None)
        run(sys.executable, "-m", "build", "--no-isolation", "--outdir", str(dist), env=env)
        (wheel,) = dist.glob("*.whl")
        (sdist,) = dist.glob("*.tar.gz")
        run(sys.executable, "-m", "twine", "check", str(wheel), str(sdist), env=env)
        expected = {
            str(p.relative_to(ROOT / "src")): p.read_bytes()
            for p in (ROOT / "src/basaltic").rglob("*")
            if p.is_file() and p.suffix != ".pyc" and "__pycache__" not in p.parts
        }
        assert payload(wheel) == expected, "Wheel differs from checked source"
        unpacked = tmp / "unpacked"
        unpacked.mkdir()
        with tarfile.open(sdist) as archive:
            for member in archive.getmembers():
                parts = Path(member.name).parts
                assert (
                    not Path(member.name).is_absolute()
                    and ".." not in parts
                    and not member.issym()
                    and not member.islnk()
                )
                relative = Path(*parts[1:])
                assert not any(
                    s in parts for s in ["internal", "AGENTS.md", "CLAUDE.md", ".gitlab-ci.yml"]
                )
                if member.isfile():
                    assert str(relative).startswith("src/basaltic/") or str(relative) in {
                        "README.md",
                        "SECURITY.md",
                        "LICENSE",
                        "pyproject.toml",
                        "PKG-INFO",
                        ".gitignore",
                    }
                    target = unpacked / relative
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(archive.extractfile(member).read())
        rebuilt = tmp / "rebuilt"
        run(
            sys.executable,
            "-m",
            "build",
            "--wheel",
            "--no-isolation",
            "--outdir",
            str(rebuilt),
            cwd=unpacked,
            env=env,
        )
        assert payload(next(rebuilt.glob("*.whl"))) == expected, (
            "Source distribution rebuild differs"
        )
        for label, artifact in [("wheel", wheel), ("sdist", sdist)]:
            venv = tmp / label
            run(sys.executable, "-m", "venv", "--without-pip", str(venv), env=env)
            python = venv / "bin/python"
            run(
                sys.executable,
                "-m",
                "pip",
                "--python",
                str(python),
                "install",
                "--quiet",
                str(artifact),
                cwd=tmp,
                env=env,
            )
            run(
                str(python),
                "-c",
                "import asyncio, httpx, basaltic; from importlib.resources import files; "
                "from basaltic.models import compute; "
                f"assert basaltic.__version__ == {version!r}; "
                'assert files(basaltic).joinpath("py.typed").is_file(); '
                'h=httpx.Client(transport=httpx.MockTransport(lambda r:httpx.Response(200,json={"instance":{"id":"ok"}}))); '
                'c=basaltic.Client(http_client=h,access_token="token",region="test-1",read_environment=False); '
                'assert c.compute.get_instance("ok").data["instance"]["id"]=="ok"; c.close(); h.close(); '
                'a=basaltic.AsyncClient(access_token="token",read_environment=False); asyncio.run(a.aclose())',
                cwd=tmp,
                env=env,
            )
        print("Verified clean wheel, source distribution, rebuild, and isolated installations.")
        for artifact in (wheel, sdist):
            print(artifact.name, hashlib.sha256(artifact.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
