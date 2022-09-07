#!/usr/bin/env python3

import subprocess


result = subprocess.run(['ls'], capture_output=True)
print('\nReturn code: {}'.format(result.returncode))
decodedOutput = result.stdout.decode()
print('Decoded output type: {}'.format(type(decodedOutput)))
print(decodedOutput)
decodedOutput = result.stdout.decode().split()
print('Decoded output type after split: {}'.format(type(decodedOutput)))
for i in decodedOutput:
    print('File in current directory: {}'.format(i))
print('\nFinished')
