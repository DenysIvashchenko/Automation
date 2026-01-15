import asyncio
import os
from aiohttp import ClientSession
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.environ.get("BASE_URL", "http://localhost:3000")

URLS = [f"{BASE_URL}"]

async def check(url, session):
    try:
        async with session.get(url, timeout=5) as r:
            return r.status == 200, url
    except Exception as e:
        return False, f"{url} ({e})"

async def health_check() -> bool:
    async with ClientSession() as session:
        results = await asyncio.gather(*(check(url, session) for url in URLS))

    failed = [url for success, url in results if not success]
    succeeded = [url for success, url in results if success]

    if succeeded:
        print("✅ URLs OK:", ", ".join(succeeded))
    if failed:
        print("❌ URLs FAILED:", ", ".join(failed))

    return len(failed) == 0

if __name__ == "__main__":
    asyncio.run(health_check())