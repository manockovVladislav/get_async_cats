import time
import asyncio
import aiohttp
import aiofiles

COUNT_FILE_CATS = 100
LINK_SITE = 'http://cataas.com'


async def download_a_cat(session, cat):
    async with session.get('/cat') as res:
        extention = res.headers.get('Content-Type').split('/')[1]
        async with aiofiles.open(f'cats/cat{cat}.{extention}', 'wb') as fp:
            print(f'Starting the cat {cat}..')
            await fp.write(await res.read())
            print(f"The cat {cat} is done!")


async def main():
    start_time = time.time()
    tasks = []
    async with aiohttp.ClientSession(LINK_SITE) as session:
        for cat in range(0, COUNT_FILE_CATS):
            task = asyncio.create_task(download_a_cat(session, cat))
            tasks.append(task)
        await asyncio.gather(*tasks)
    print("Total time: " + str(time.time() - start_time))

if __name__ == "__main__":
    asyncio.run(main())
