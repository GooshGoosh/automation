#!/usr/bin/env python3

import shutil
import sys


def check_disk_usage(disk, minAbsolute, minPercent):
	# Returns True if there is enough free disk space, False otherwise
	du = shutil.disk_usage(disk)

	# Calculate the percentage of free space
	percentFree = 100 * du.free / du.total

	# Calculate how many free gigabytes
	gigabytesFree = du.free / 2**30
	if percentFree < minPercent or gigabytesFree < minAbsolute:
		return False
	return True


if not check_disk_usage("/", 10, 10):
	print("ERROR: Not enough disk space.")
	sys.exit(1)

print("Everything ok.")
sys.exit(0)

