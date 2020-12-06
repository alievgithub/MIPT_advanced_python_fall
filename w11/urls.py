from typing import Any, Union, Coroutine
import aiohttp
import asyncio
from aiofile import LineReader, async_open, AIOFile
import re

async def text(session, service):
    async with session.get(service) as file:
        text = file.text()
        text = re.split(r"[\r\n]", text)
        for x in text:
            if x.startswith("<a >"):
                async with AIOFile("str.txt", "w") as f:
                    writer = Writer(f)
                    await writer(x)


async def help(name):
    async with AIOFile(name, "r") as file:
        print(file)
        async for line in LineReader(file):
            print(line)
            async with aiohttp.ClientSession() as session:
                asyncio.ensure_future(text(session, line))

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(help("urls.txt"))
    loop.close()
