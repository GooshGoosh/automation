'''
health_checks.py - Performs health checks on the system such as disk usage and
cpu usage.
'''

import shutil
import psutil
import network


def check_disk_usage(disk):
    """Checks the disk usage of the given disk.

    Args:
        disk (str): Path of the disk to check.

    Returns:
        bool: Whether or not the percentage of free disk space is over 20%.
    """
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20


def check_cpu_usage():
    """Checks the cpu usage of the system.

    Returns:
        bool: Whether or not the percent of cpu usage is less than 75%.
    """
    usage = psutil.cpu_percent(1)
    return usage < 75


def main():
    """Main function to run the program.
    """
    if not check_disk_usage("/") or not check_cpu_usage():
        print("ERROR!")
    elif network.check_localhost() and network.check_connectivity():
        print("Everything ok")
    else:
        print("Network checks failed")


if __name__ == "__main__":
    main()
    