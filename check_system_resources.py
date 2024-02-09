'''
check_system_resources.py - Checks the available disk space, memory, and current CPU
usage of the system. Checks the total and available system memory (excluding swap)
and if a system restart is required. Creates a PDF report of the results, with a
timestamp for when the script was executed, in the user's home directory.
'''


import socket
import time
import datetime
import os
import shutil
import psutil
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def check_disk_usage(disk):
    """Checks the disk usage and prints the total usage as well as the free space
    available.

    Args:
        disk (str): The path of the disk to check.

    Returns:
        list: List of the disk info.
    """
    disk_info = []
    du = shutil.disk_usage(disk)
    disk_info.append(f'Total Disk Usage for \'{disk}\': {du.used / 2**30:.2f}G')
    disk_info.append(f'Free Space: {du.free / 2**30:.2f}G')
    if (du.free / du.total * 100) < 20:
        disk_info.append('Available disk space less than 20%!')
    else:
        disk_info.append('Disk Check: OK')

    return disk_info


def check_cpu_usage():
    """Gets the number of physical and logical CPU cores and prints a message
    depending on the current CPU usage.

    Returns:
        list: List of CPU info.
    """
    cpu_info = []
    physical_cores = psutil.cpu_count(logical=False)
    cpu_info.append(f'Current Number of CPU Cores (Physical): {physical_cores}')
    logical_cores = psutil.cpu_count()
    cpu_info.append(f'Current Number of CPU Cores (Logical): {logical_cores}')
    usage = psutil.cpu_percent(1)
    if usage > 75:
        cpu_info.append('WARNING! CPU usage over 75%!')
    else:
        cpu_info.append('CPU Check: OK')

    return cpu_info


def check_memory_usage():
    """Checks the total system memory and available system memory (excluding swap).

    Returns:
        list: List of memory info.
    """
    mem_info = []
    mem = psutil.virtual_memory()
    mem_info.append(f'Total Memory: {mem.total / 2**30:.2f}G')
    mem_info.append(f'Available Memory: {mem.available / 2**30:.2f}G')
    if mem.available < (1 * 2**30):
        mem_info.append('WARNING! System memory lower than 1G!')
    else:
        mem_info.append('Memory Check: OK')

    return mem_info


def check_localhost():
    """Checks if the network interface is up and working for the system.

    Returns:
        str: A message depending on the status of the network interface.
    """
    localhost = socket.gethostbyname('localhost')
    if localhost == "127.0.0.1":
        return 'localhost: 127.0.0.1'
    else:
        return 'localhost: Failed'


def check_internet(host='8.8.8.8', port=53, timeout=3):
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
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return 'Internet Check: OK'
    except socket.error:
        return 'Internet Check: Failed'


def check_dns(host='google-public-dns-a.google.com', timeout=3):
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
        return 'DNS Check: OK'
    return 'DNS Check: Failed'


def check_reboot_required():
    """Checks if a reboot of the system is required.

    Returns:
        str: A message depending on if the system needs a reboot.
    """
    if os.path.exists('/var/run/reboot-required'):\
        return 'REBOOT REQUIRED'
    return 'No reboot required'


def generate_report(data_list):
    """Generate a report of the system resources check and save is as a PDF.

    Args:
        data_list (list): List of all the system test and check results.
    """
    # Create the report object/name, the list of data to be generated into the report,
    # as well as get the current time and format it.
    report = SimpleDocTemplate(os.path.join(os.path.expanduser('~'),
                                            'system-resources-report.pdf'))
    styles = getSampleStyleSheet()
    story = []
    today = datetime.datetime.now()
    format_time = today.strftime("%A, %B %d, %Y, %H:%M:%S")

    report_title = Paragraph(f'System Resources Report for {format_time}', styles["h1"])
    story.append(report_title)

    for data in data_list:
        story.append(Spacer(1, 12))
        if isinstance(data, list):
            for line in data:
                story.append(Paragraph(line, styles["Normal"]))
        else:
            story.append(Paragraph(data, styles["Normal"]))

    # Build the report and print the location/name of the report generated.
    report.build(story)
    print(f'Report generated at '\
        f'{os.path.join(os.path.expanduser("~"),"system-resources-report.pdf")}')


def main():
    """Main function to run the program.
    """
    data_list = []
    start_time = time.time()
    print('\nChecking Disk...\n')
    data_list.append(check_disk_usage('/'))

    print('\nChecking CPU...\n')
    data_list.append(check_cpu_usage())

    print('\nChecking Memory...\n')
    data_list.append(check_memory_usage())

    print('\nChecking Internet Connection...\n')
    data_list.append(check_localhost())
    data_list.append(check_internet())
    data_list.append(check_dns())

    print('\nChecking Reboot...\n')
    data_list.append(check_reboot_required())

    print('\nGenerating Report...\n')
    generate_report(data_list)

    print('\nChecks finished\nExiting...')
    duration = time.time() - start_time
    print(f'\nDuration: {duration}')


if __name__ == "__main__":
    main()
