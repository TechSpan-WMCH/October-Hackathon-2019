import asyncio

from aiohttp import ClientSession
from yarl import URL


async def fetch_headers(session: ClientSession, url: URL):
    async with session.get(url, verify_ssl=False) as response:
        return url, response.headers


async def get_data(urls):
    tasks = []
    async with ClientSession() as session:
        for address in urls:
            url = URL.build(scheme="http", host=address)
            task = fetch_headers(session=session, url=url)
            tasks.append(task)

        results = await asyncio.gather(*tasks)

        for result in results:
            print(result[0], result[1]['Server'])


if __name__ == '__main__':
    urls = ['httpbin.org', 'techspan.org', 'example.com', 'google.com', 'test.com', 'github.com', 'readthedocs.io']
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_data(urls=urls))

# The below is merely a non-working PoC for what a server version scanner could look like. This could be quickly expedited by using a much faster method for banners in Python.
print("\n\nThe Apache server version is vulnerable:")
print(r.headers['Server'])
print("Refer to https://www.exploit-db.com/exploits/41570")
# print(r.text) return the html
