#!/usr/bin/env python3

# checkSudoCommands.py - Takes the path to the auth.log file and parses it for the date/time, user, and command that was run
# with sudo privileges. The data is written to a file and the path to the output file can be specified; 
# defaults to the same directory that the script was run in.

import os
import sys
import re


# Write the results of the search_log function to a new file.
def create_file(outputFile, logList):
    with open(outputFile, 'w') as file:
        for log in logList:
            file.write(log)
        file.close()
    print('Parsed log file saved as {}'.format(outputFile))


# Search through a given log file using a given regex pattern and save the results in a list to return.
def search_log(logFile, regexPattern):
    returnedLogs = []
    with open(logFile, mode='r', encoding='UTF-8') as file:
        for log in file.readlines():
            result = re.search(regexPattern, log)
            if result is None:
                continue
            else:
                returnedLogs.append('Date/Time: {}; User: {}; Command: {}\n'.format(result.group(1), result.group(2), result.group(3)))
        file.close()
    return returnedLogs


def main():
    # Check if 2 command line arguments are given with the program call.
    if len(sys.argv) != 3:
        print('Usage: checkSudoCommands.py [path/to/auth.log] [output file]')
        sys.exit(0)

    logFile = sys.argv[1]
    outputFile = os.path.join(os.path.expanduser('~'), sys.argv[2])
    regexPattern = r'^(\w{3} \d{2} \d{2}:\d{2}:\d{2}).*sudo:\s+(\w+).*COMMAND=(.*$)'

    # Check if the log file to read exists and if the output file already exists.
    if not os.path.exists(logFile):
        print('Log file \'{}\' does not exist.\nExiting...'.format(logFile))
        sys.exit(0)
    elif os.path.exists(outputFile):
        input = input('WARNING: The file ' + outputFile + ' already exists! Would you like to overwrite? (Y/N): ')
        if input.lower() != 'y':
            print('Exiting...')
            sys.exit(0)

    returnedLogs = search_log(logFile, regexPattern)
    create_file(outputFile, returnedLogs)
    sys.exit(0)


if __name__ == "__main__":
    main()
