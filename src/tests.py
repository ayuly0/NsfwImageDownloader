import asyncio
import uuid
import aiohttp
import async_timeout
import hmtai

async def get_url(url, session):
    file_name = "image/" + uuid.uuid4().hex + ".png"
    async with async_timeout.timeout(120):
        async with session.get(url) as response:
            with open(file_name, 'wb') as fd:
                async for data in response.content.iter_chunked(1024):
                    fd.write(data)
    return 'Successfully downloaded ' + file_name
async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [get_url(url, session) for url in urls]
        return await asyncio.gather(*tasks)
urls = [hmtai.get("hmtai", "yuri") for i in range(10)]
loop = asyncio.get_event_loop()
results = loop.run_until_complete(main(urls))
print('\n'.join(results))
