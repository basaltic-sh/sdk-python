"""Public runtime, formatting, and static consumer checks; no generator required."""

import os
import subprocess
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
env = dict(os.environ, PYTHONPATH=str(root / "src"))
for args in [
    ["ruff", "check", "src", "tests", "scripts"],
    ["ruff", "format", "--check", "src", "tests", "scripts"],
    ["mypy"],
    ["unittest", "discover", "-s", "tests", "-p", "test_*.py", "-v"],
]:
    subprocess.run([sys.executable, "-m", *args], cwd=root, env=env, check=True)
