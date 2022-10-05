#!/usr/bin/env python3

# checkSystemResources.py - Checks the available disk space, memory, and current CPU usage of the system.
# Checks the total and available system memory (excluding swap) and if a system restart is required.
# Creates a PDF report of the results, with a timestamp for when the script was executed, in the user's home directory.


import os
import shutil
import psutil
import socket
import time
import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def check_disk_usage(disk):
    diskInfo = []
    du = shutil.disk_usage(disk)                                                                # Get a tuple of various disk info using shutil.
    diskInfo.append('Total Disk Usage for \'{}\': {:.2f}G'.format(disk, (du.used / 2**30)))     # Print the total disk usage in G.
    diskInfo.append('Free Space: {:.2f}G'.format(du.free / 2**30))                              # Print the free disk space in G.
    if (du.free / du.total * 100) < 20:                                                         # Print a message depending on the available disk space.
        diskInfo.append('Available disk space less than 20%!')
    else:
        diskInfo.append('Disk Check: OK')
    
    return diskInfo


def check_cpu_usage():
    cpuInfo = []
    physicalCores = psutil.cpu_count(logical=False)                                         # Get the number of physical CPU cores
    cpuInfo.append('Current Number of CPU Cores (Physical): {}'.format(physicalCores))      # and print them to the screen.
    logicalCores = psutil.cpu_count()                                                       # Get the number of logical CPU cores (cores x threads per core)
    cpuInfo.append('Current Number of CPU Cores (Logical): {}'.format(logicalCores))        # and print them to the screen.
    usage = psutil.cpu_percent(1)
    if usage > 75:                                                                          # Check CPU usage and print a message depending on the
        cpuInfo.append('WARNING! CPU usage over 75%!')                                      # current CPU usage.
    else:
        cpuInfo.append('CPU Check: OK')
    
    return cpuInfo
        
        
def check_memory_usage():
    memInfo = []
    mem = psutil.virtual_memory()                                                   # Get a tuple of system memory info using psutil.
    memInfo.append('Total Memory: {:.2f}G'.format(mem.total / 2**30))               # Print the total system memory (excluding swap) in G.
    memInfo.append('Available Memory: {:.2f}G'.format(mem.available / 2**30))       # Print the available memory (excluding swap) in G.
    if mem.available < (1 * 2**30):                                                 # Print a message if the available memory is lower than 1G.
        memInfo.append('WARNING! System memory lower than 1G!')
    else:
        memInfo.append('Memory Check: OK')
    
    return memInfo


def check_localhost():
    localhost = socket.gethostbyname('localhost')       # Check if the network interface is up and working for the system.
    if localhost == "127.0.0.1":
        return 'localhost: 127.0.0.1'
    else:
        return 'localhost: Failed'
        
        
def check_internet(host='8.8.8.8', port=53, timeout=3):     # Check if the system can reach the internet. Use an IPv4 address to prevent DNS errors.
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))     # Test for a connection to 8.8.8.8 on port 53 (DNS).
        return 'Internet Check: OK'                                                 # Uses one of Google's public DNS servers.
    except socket.error as ex:
        return 'Internet Check: Failed'


def check_DNS(host='google-public-dns-a.google.com', timeout=3):        # Check if DNS is working properly and the system is correctly resolving host names.
    socket.setdefaulttimeout(timeout)                                   # Uses one of Google's public DNS servers.
    googleDNS = socket.gethostbyname(host)
    if googleDNS == '8.8.8.8':
        return 'DNS Check: OK'
    else:
        return 'DNS Check: Failed'


def check_reboot_required():
    if os.path.exists('/var/run/reboot-required'):      # Check if the 'reboot-required' file exists on the system
        return 'REBOOT REQUIRED'                        # and print a message depending on if it exists or not.
    else:
        return 'No reboot required'


def generate_report(dataList):
    # Create the report object/name, the list of data to be generated into the report, as well as get the current time and format it.
    report = SimpleDocTemplate(os.path.join(os.path.expanduser('~'), 'system-resources-report.pdf'))
    styles = getSampleStyleSheet()
    Story = []
    today = datetime.datetime.now()
    formatTime = today.strftime("%A, %B %d, %Y, %H:%M:%S")
    
    reportTitle = Paragraph('System Resources Report for {}'.format(formatTime), styles["h1"])      # Create the report title/header.
    Story.append(reportTitle)
    
    for data in dataList:
        Story.append(Spacer(1, 12))
        if type(data) is list:                                      # If the data is of type list, loop through each line of the
            for line in data:                                       # list and add it to the Story.
                Story.append(Paragraph(line, styles["Normal"]))
        else:
            Story.append(Paragraph(data, styles["Normal"]))         # Add any lines to the Story that aren't of type list.
    
    # Build the report and print the location/name of the report generated.
    report.build(Story)
    print('Report generated at \'{}\''.format(os.path.join(os.path.expanduser('~'), 'system-resources-report.pdf')))


def main():
    dataList = []
    start_time = time.time()
    print('\nChecking Disk...\n')
    dataList.append(check_disk_usage('/'))

    print('\nChecking CPU...\n')
    dataList.append(check_cpu_usage())

    print('\nChecking Memory...\n')
    dataList.append(check_memory_usage())

    print('\nChecking Internet Connection...\n')
    dataList.append(check_localhost())
    dataList.append(check_internet())
    dataList.append(check_DNS())

    print('\nChecking Reboot...\n')
    dataList.append(check_reboot_required())
    
    print('\nGenerating Report...\n')
    generate_report(dataList)
    
    print('\nChecks finished\nExiting...')
    duration = time.time() - start_time
    print(f'\nDuration: {duration}')


if __name__ == "__main__":
    main()
