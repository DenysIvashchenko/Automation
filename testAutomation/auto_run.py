from pathlib import Path
import subprocess
import sys

ROOT_DIR = Path(__file__).resolve().parents[1]
SERVER_DIR = ROOT_DIR / "server"

def run_test():
    result = subprocess.run(
        ["npm", "test"],
        cwd=SERVER_DIR,
        shell=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )

    print(result.stdout)

    if result.returncode != 0:
        print("BUILD FAILED")
        sys.exit(1)

    print("BUILD SUCCESS")