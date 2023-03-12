import aiohttp
import asyncio
from time import time


def write_file(data):
    filename = f'file-{int(time()*1000)}.jpeg'
    with open(filename, 'wb') as file:
        file.write(data)


async def fetch_content(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        write_file(data)


async def main():
    url = 'https://loremflickr.com/320/240'
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(fetch_content(url, session))
            tasks.append(task)
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    t0 = time()
    asyncio.run(main())
    print(time() - t0)
