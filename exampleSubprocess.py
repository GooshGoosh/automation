#!/usr/bin/env python3

# exampleSuubprocess.py - A test case of the subprocess.run provided by the subprocess module.
# Captures the output of the ls command and displays the return code, the data after decoding,
# and the data after being processed as a list.

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
