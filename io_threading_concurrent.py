'''
io_threading_concurrent.py - Example program to show the efficiency of using threading
when performing multiple input/output operations at once.
'''


import threading
import time
import concurrent.futures
import requests


thread_local = threading.local()


def get_session():
    """Creates a session for sending http requests.

    Returns:
        requests.Session: Session for sending http requests.
    """
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    """Sends http requests to the specified URL.

    Args:
        url (str): URL for sending requests to.
    """
    session = get_session()
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(site_list):
    """Sends http requests to the URLs in the given site list.

    Args:
        site_list (list): URLs to send http requests to.
    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, site_list)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
