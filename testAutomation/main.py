import asyncio
import sys

from health import health_check
from auto_run import run_test


def main():
    print("🔍 Health check...")
    ok = asyncio.run(health_check())

    if not ok:
        print("❌ Health check failed")
        sys.exit(1)

    print("🚀 Running tests...")
    run_test()


if __name__ == "__main__":
    main()