#!/usr/bin/env python3

# checkSystemResources.py - Checks the available disk space, memory, and current CPU usage of the system.
# Checks the total and available system memory (excluding swap) if a system restart is required.


import os
import shutil
import psutil
import socket


def check_disk_usage(disk):
    du = shutil.disk_usage(disk)                                                       # Get a tuple of various disk info using shutil.
    print('Total Disk Usage for \'{}\': {:.2f}G'.format(disk, (du.used / 2**30)))      # Print the total disk usage in G.
    print('Free Space: {:.2f}G'.format(du.free / 2**30))                               # Print the free disk space in G.
    if (du.free / du.total * 100) < 20:                                                # Print a message depending on the available disk space.
        print('Available disk space less than 20%!')
    else:
        print('Disk Check: OK')


def check_cpu_usage():
    physicalCores = psutil.cpu_count(logical=False)                                 # Get the number of physical CPU cores
    print('Current Number of CPU Cores (Physical): {}'.format(physicalCores))       # and print them to the screen.
    logicalCores = psutil.cpu_count()                                               # Get the number of logical CPU cores (cores x threads per core)
    print('Current Number of CPU Cores (Logical): {}'.format(logicalCores))         # and print them to the screen.
    usage = psutil.cpu_percent(1)
    if usage > 75:                                                                  # Check CPU usage and print a message depending on the
        print('WARNING! CPU usage over 75%!')                                       # current CPU usage.
    else:
        print('CPU Check: OK')
        
        
def check_memory_usage():
    mem = psutil.virtual_memory()                                          # Get a tuple of system memory info using psutil.
    print('Total Memory: {:.2f}G'.format(mem.total / 2**30))               # Print the total system memory (excluding swap) in G.
    print('Available Memory: {:.2f}G'.format(mem.available / 2**30))       # Print the available memory (excluding swap) in G.
    if mem.available < (1 * 2**30):                                        # Print a message if the available memory is lower than 1G.
        print('WARNING! System memory lower than 1G!')
    else:
        print('Memory Check: OK')


def check_localhost():
    localhost = socket.gethostbyname('localhost')
    if localhost == "127.0.0.1":
        print('localhost: 127.0.0.1')
    else:
        print('localhost: Failed')
        
        
def check_internet(host='8.8.8.8', port=53, timeout=3):
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        print('Internet Check: OK')
    except socket.error as ex:
        #print(ex)
        print('Internet Check: Failed')


def check_DNS(host='google-public-dns-a.google.com', timeout=3):
    socket.setdefaulttimeout(timeout)
    googleDNS = socket.gethostbyname(host)
    if googleDNS == '8.8.8.8':
        print('DNS Check: OK')
    else:
        print('DNS Check: Failed')


def check_reboot_required():
    if os.path.exists('/var/run/reboot-required'):      # Check if the 'reboot-required' file exists on the system
        print('REBOOT REQUIRED')                        # and print a message depending on if it exists or not.
    else:
        print('No reboot required')


##############
# MAIN BLOCK #
##############

print('\nChecking Disk...\n')
check_disk_usage('/')

print('\nChecking CPU...\n')
check_cpu_usage()

print('\nChecking Memory...\n')
check_memory_usage()

print('\nChecking Internet Connection...\n')
check_localhost()   
check_internet()
check_DNS()

print('\nChecking Reboot...\n')
check_reboot_required()
print('\nChecks finished\nExiting...')
