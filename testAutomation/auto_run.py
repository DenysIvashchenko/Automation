from pathlib import Path
import subprocess
import sys

ROOT_DIR = Path(__file__).resolve().parents[1]
SERVER_DIR = ROOT_DIR 

print("ROOT_DIR =", ROOT_DIR)
print("SERVER_DIR =", SERVER_DIR)
print("package.json exists:", (SERVER_DIR / "package.json").exists())

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