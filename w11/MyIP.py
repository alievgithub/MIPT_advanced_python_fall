from collections import namedtuple
import time
import asyncio
from concurrent.futures import FIRST_COMPLETED
import aiohttp

Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query')
)

async def fetch_ip(session, service):
    #print(f"{service}")
    async with session.get(service.url) as result:
        html = await result.json()
        return html


async def asynchronous():
    async with aiohttp.ClientSession() as session:
        MyID = await asyncio.wait({fetch_ip(session, elem) for elem in SERVICES}, return_when = asyncio.FIRST_COMPLETED)
        #print(MyID)
        for x in MyID[0]:
                res = x.result()
                for service in SERVICES:
                    try:
                        print(res[service.ip_attr])
                    except:
                        pass

ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())
