"""Self-check for masked_input() in scripts/unlock_files.py.

Run: poetry run python tests/test_masked_input.py
"""

import importlib.util
import io
import sys
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent.parent / "scripts" / "unlock_files.py"

spec = importlib.util.spec_from_file_location("unlock_files", SCRIPT_PATH)
assert spec and spec.loader
unlock_files = importlib.util.module_from_spec(spec)
spec.loader.exec_module(unlock_files)


def test_non_tty_falls_back_to_getpass():
    original_stdin = sys.stdin
    original_getpass = unlock_files.getpass.getpass
    sys.stdin = io.StringIO("secret\n")  # StringIO is not a TTY
    unlock_files.getpass.getpass = lambda prompt: "secret"
    try:
        assert unlock_files.masked_input("Password: ") == "secret"
    finally:
        sys.stdin = original_stdin
        unlock_files.getpass.getpass = original_getpass


if __name__ == "__main__":
    test_non_tty_falls_back_to_getpass()
    print("✅ masked_input self-check passed")
