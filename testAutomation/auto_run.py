from pathlib import Path
import platform
import subprocess
import sys

def find_server_dir(start: Path) -> Path:
    for parent in start.parents:
        candidate = parent / "server" / "package.json"
        if candidate.exists():
            return parent / "server"
    raise RuntimeError("server/package.json not found")

SERVER_DIR = find_server_dir(Path(__file__).resolve())
ROOT_DIR = SERVER_DIR.parent

def run_test():
    npm = "npm.cmd" if platform.system() == "Windows" else "npm"

    result = subprocess.run(
        [npm, "test"],
        cwd=SERVER_DIR,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )

    print(result.stdout)

    if result.returncode != 0:
        print("BUILD FAILED")
        sys.exit(1)

    print("BUILD SUCCESS")