'''
io_async_concurrent.py - Example program to show the efficiency of using asyncio
when performing multiple input/output operations at once.
'''

import asyncio
import time
import aiohttp


async def download_site(session, url):
    """Sends http requests to the specified URL within the given session.

    Args:
        session (aiohttp.client.ClientSession): Session for making http requests.
        url (str): URL for sending requests to.
    """
    async with session.get(url) as response:
        print(f"Read {response.content_length} from {url}")


async def download_all_sites(sites_list):
    """Creates a session to send http requests to the urls specified in the
    given site list.

    Args:
        sites_list (list): List of URLs to send http requests to.
    """
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites_list:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    asyncio.run(download_all_sites(sites))
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")
