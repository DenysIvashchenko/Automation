import asyncio
from health import health_check
import asyncio

def main():
    print("🔍 Health check...")
    ok = asyncio.run(health_check())

    if not ok:
        raise SystemExit(1)

    print("✅ Automation finished successfully")

if __name__ == "__main__":
    main()