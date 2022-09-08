#!/usr/bin/env python3

# checkSystemResources.py - Checks the available disk space, memory, and current CPU usage of the system.
# Checks the total and available system memory (excluding swap) if a system restart is required.


import os
import shutil
import psutil


def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    print('Total Disk Usage for \'{}\': {:.2f}GB'.format(disk, (du.used / 2**30)))
    print('Free Space: {:.2f}GB'.format(du.free / 2**30))
    if (du.free / du.total * 100) < 20:
        print('Available disk space less than 20%!')
    else:
        print('Disk Check: OK')


def check_cpu_usage():
    physicalCores = psutil.cpu_count(logical=False)
    print('Current Number of CPU Cores (Physical): {}'.format(physicalCores))
    logicalCores = psutil.cpu_count()
    print('Current Number of CPU Cores (Logical): {}'.format(logicalCores))
    usage = psutil.cpu_percent(1)
    if usage > 75:
        print('WARNING! CPU usage over 75%!')
    else:
        print('CPU Check: OK')
        
        
def check_memory_usage():
    mem = psutil.virtual_memory()
    print('Total Memory: {:.2f}GB'.format(mem.total / 2**30))
    print('Available Memory: {:.2f}GB'.format(mem.available / 2**30))
    if mem.available < (1 * 2**30):
        print('WARNING! System memory lower than 1GB!')
    else:
        print('Memory Check: OK')


def check_reboot_required():
    if os.path.exists('/var/run/reboot-required'):
        print('REBOOT REQUIRED')
    else:
        print('No reboot required')


print('\nChecking Disk...\n')
check_disk_usage('/')
print('\nChecking CPU...\n')
check_cpu_usage()
print('\nChecking Memory...\n')
check_memory_usage()
print('\nChecking Reboot...\n')
check_reboot_required()
print('\nChecks finished\nExiting...')
