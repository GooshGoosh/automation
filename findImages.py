#!/usr/bin/env python3

import os
from PIL import Image
import sys


imageDirectory = sys.argv[1]

def main():
	print()
	for file in os.listdir(imageDirectory):
		try:
			im = Image.open(os.path.join(imageDirectory, file))
		except IOError:
			continue

		print('{} is an image file in {}'.format(file, imageDirectory))
		im.close()
	print()

if __name__ == "__main__":
	main()

