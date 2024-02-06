'''
network_checks.py - Performs network checks on the system.
'''

import socket
import requests


def check_localhost():
    """Checks the localhost to ensure the system network interface is working.

    Returns:
        bool: Whether or not the system network interface is working.
    """
    localhost = socket.gethostbyname('localhost')
    return localhost == "127.0.0.1"


def check_connectivity():
    """Checks for internet connectivity.

    Returns:
        bool: Whether or not the internet request succeeded with a status code 200.
    """
    request = requests.get(url="https://www.google.com", timeout=10)
    return request.status_code == 200
