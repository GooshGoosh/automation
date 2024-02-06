'''
check_system_resources_asyncio.py - Checks the available disk space, memory, and
current CPU usage of the system. Checks the total and available system memory
(excluding swap) and if a system restart is required.
'''

import socket
import asyncio
import time
import os
import shutil
import psutil


async def check_disk_usage(disk):
    """Get the total disk usage and free disk space in GB. Prints a message
    depending on the available disk space.

    Args:
        disk (str): Path to the disk to check.
    """
    print('\nChecking Disk...\n')
    du = shutil.disk_usage(disk)
    print(f'Total Disk Usage for \'{disk}\': {du.used / 2**30:.2f}G')
    print(f'Free Space: {du.free / 2**30:.2f}G')
    if (du.free / du.total * 100) < 20:
        print('Available disk space less than 20%!')
    else:
        print('Disk Check: OK')


async def check_cpu_usage():
    """Gets the number of physical and logical CPU cores and prints them to the
    screen. Prints a message depending on the current CPU usage.
    """
    print('\nChecking CPU...\n')
    physical_cores = psutil.cpu_count(logical=False)
    print(f'Current Number of CPU Cores (Physical): {physical_cores}')
    logical_cores = psutil.cpu_count()
    print(f'Current Number of CPU Cores (Logical): {logical_cores}')
    usage = psutil.cpu_percent(1)
    if usage > 75:
        print('WARNING! CPU usage over 75%!')
    else:
        print('CPU Check: OK')


async def check_memory_usage():
    """Prints the total system memory and available memory in GB. Prints a message
    to the screen depending on the available system memory.
    """
    print('\nChecking Memory...\n')
    mem = psutil.virtual_memory()
    print(f'Total Memory: {mem.total / 2**30:.2f}G')
    print(f'Available Memory: {mem.available / 2**30:.2f}G')
    if mem.available < (1 * 2**30):
        print('WARNING! System memory lower than 1G!')
    else:
        print('Memory Check: OK')


async def check_localhost():
    """Checks if the network interface is up and working for the system. Prints
    a message depending on the test result.
    """
    localhost = socket.gethostbyname('localhost')
    if localhost == "127.0.0.1":
        print('localhost: 127.0.0.1')
    else:
        print('localhost: Failed')


async def check_internet(host='8.8.8.8', port=53, timeout=3):
    """Checks if the system can reach the internet. Uses an IPv4 address to prevent
    DNS errors.
    
    Args:
        host (str, optional): IP address of the host to use as a test.
        Defaults to '8.8.8.8'.
        port (int, optional): Port to use for the test. Defaults to 53.
        timeout (int, optional): How long to wait for a response before quitting
        the test. Defaults to 3.
        
    Returns:
        str: A message depending on the results of the test.
    """
    print('\nChecking Internet Connection...\n')
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        print('Internet Check: OK')
    except socket.error:
        print('Internet Check: Failed')


async def check_dns(host='google-public-dns-a.google.com', timeout=3):
    """Checks if DNS is working properly and the system is correctly resolving
    host names.

    Args:
        host (str, optional): Host to use as a test. Defaults to 'google-public-dns-a.google.com'.
        timeout (int, optional): How long to wait for a response before quitting
        the test. Defaults to 3.

    Returns:
        str: A message depending on the results of the test.
    """
    socket.setdefaulttimeout(timeout)
    google_dns = socket.gethostbyname(host)
    if google_dns == '8.8.8.8':
        print('DNS Check: OK')
    else:
        print('DNS Check: Failed')


async def check_reboot_required():
    """Checks if a reboot of the system is required.

    Returns:
        str: A message depending on if the system needs a reboot.
    """
    print('\nChecking Reboot...\n')
    if os.path.exists('/var/run/reboot-required'):
        print('REBOOT REQUIRED')
    else:
        print('No reboot required')


def main():
    """Main function to run the program.
    """
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(check_disk_usage('/'),
                                           check_cpu_usage(),
                                           check_memory_usage(),
                                           check_internet(),
                                           check_localhost(),
                                           check_dns(),
                                           check_reboot_required()
                                           ))

    print('\nChecks finished\nExiting...')
    duration = time.time() - start_time
    print(f'\nDuration: {duration}')


if __name__ == "__main__":
    main()
