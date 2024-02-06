#!/usr/bin/env python3

# sshFailedLogins.py - Parses the auth.log file found in the /var/log directory for ssh login failures for any user.
# The date/time, the username for the 'Failed password for [user], and the IP of the login attempt are saved to
# a specified output file in the user's home directory.

import re
import os
import sys
import operator


# Search through a given log file using a given regex pattern and save the results in a list to return.
def search_log(LOG_FILE, regex_pattern):
    returned_logs = []
    user_stats = {}
    with open(LOG_FILE, mode='r', encoding='UTF-8') as file:
        for log in file.readlines():
            result = re.search(regex_pattern, log)
            if result is None:
                continue
            else:
                returned_logs.append('Date/Time: {}; User: {}; Source IP: {}\n'.format(result.group(1), result.group(2), result.group(3)))
                if result.group(2) not in user_stats:
                    user_stats[result.group(2)] = 1
                else:
                    user_stats[result.group(2)] += 1
        file.close()
    return returned_logs, user_stats


# Write the results of the search_log function to a new file.
def create_file(output_file, log_list, userDict):
    with open(output_file, 'w') as file:
        file.write('FAILED SSH LOGIN ATTEMPTS PER USER\n')
        for user in userDict:
            file.write('{}: {}\n'.format(user[0], user[1]))
        file.write('-' * 20 + '\n')
        for log in log_list:
            file.write(log)
        file.close()
    print('Parsed log file saved as {}'.format(output_file))
    

def main():    
    if len(sys.argv) != 3:
        print('Usage: sshFailedLogins.py [/path/to/auth.log] [output file]')
        sys.exit(0)

    LOG_FILE = sys.argv[1]
    output_file = os.path.join(os.path.expanduser('~'), sys.argv[2])
    regex_pattern = r'^(\w{3}\s+\d{1,2} \d{2}:\d{2}:\d{2}).*Failed password for (\w*) from (\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b)'

    if not os.path.exists(LOG_FILE):
        print('Log file \'{}\' does not exist. Exiting...'.format(LOG_FILE))
        sys.exit(0)
    elif os.path.exists(output_file):
        input = input('WARNING: The file \'{}\' already exists! Would you like to overwrite? (y/n): '.format(output_file))
        if input.lower() != 'y':
            print('Exiting...')
            sys.exit(0)

    returned_logs, user_stats = search_log(LOG_FILE, regex_pattern)
    user_stats = sorted(user_stats.items(), key=operator.itemgetter(1), reverse=True)
    create_file(output_file, returned_logs, user_stats)
    sys.exit(0)


if __name__ == "__main__":
    main()
