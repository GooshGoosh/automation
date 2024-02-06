'''
io_non_concurrent.py - An example program of performing multiple input/output
operations at once without concurrency.
'''


import time
import requests


def download_site(url, session):
    """Sends http requests to the specified URL within the given session.

    Args:
        url (str): URL to send the http request to.
        session (requests.Session): Session for making http requests.
    """
    with session.get(url) as response:
        print(f"Read{len(response.content)} from {url}")


def download_all_sites(site_list):
    """Creates a session to send http requests to the urls specified in the
    given site list.

    Args:
        site_list (list): List of URLs to send http requests to.
    """
    with requests.Session() as session:
        for url in site_list:
            download_site(url, session)


if __name__ == "__main__":
    sites = [ 
             'http://www.jython.org',
             'http://olympus.realpython.org'
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Download {len(sites)} in {duration} seconds")
