import asyncio
import uvicorn
from fastapi import FastAPI
from webserver.main import main

async def request(i):
    print(f"Request №{i} start")
    await main()
    print(f"Request №{i} stop")


async def asn():
    await asyncio.gather(*[request(i) for i in range(100)])


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asn())
    loop.close()
