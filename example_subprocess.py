'''
example_subprocess.py - A test case of the subprocess.run provided by the subprocess
module. Captures the output of the ls command and displays the return code, the data
after decoding, and the data after being processed as a list.
'''


import subprocess


result = subprocess.run(['ls'], capture_output=True, check=False)
print(f'\nReturn code: {result.returncode}')

decoded_output = result.stdout.decode()
print(f'Decoded output type: {type(decoded_output)}')
print(decoded_output)

decoded_output = result.stdout.decode().split()
print(f'Decoded output type after split: {type(decoded_output)}')

for i in decoded_output:
    print(f'File in current directory: {i}')
print('\nFinished')
