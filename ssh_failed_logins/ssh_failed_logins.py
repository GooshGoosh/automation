'''
ssh_failed_logins.py - Parses the auth.log file found in the /var/log directory
for ssh login failures for any user. The date/time, the username for the failed
password for [user], and the IP of the login attempt are saved to a specified
output file in the user's home directory.
'''



import re
import os
import sys
import operator


def search_log(log_file, regex_pattern):
    """Search through the given log file using the given regex pattern and return
    the results as a list.

    Args:
        log_file (str): Path/name of the log file to search.
        regex_pattern (str): Regex pattern to match in the log file.

    Returns:
        list: List of matches found in the log file.
    """
    returned_logs = []
    user_stats = {}
    with open(log_file, mode='r', encoding='UTF-8') as file:
        for log in file.readlines():
            result = re.search(regex_pattern, log)
            if result is None:
                continue

            returned_logs.append(f'Date/Time: {result.group(1)}; \
                User: {result.group(2)}; Source IP: {result.group(3)}\n')
            if result.group(2) not in user_stats:
                user_stats[result.group(2)] = 1
            else:
                user_stats[result.group(2)] += 1
        file.close()
    return returned_logs, user_stats


# Write the results of the search_log function to a new file.
def create_file(output_file, log_list, user_data):
    """Write the results of the search_log function to a new file.

    Args:
        output_file (str): Path/name of the output file.
        log_list (str): Path/name of the log file searched.
        user_data (list): List of tuples containing the matched user data.
    """
    with open(output_file, 'w', encoding='UTF-8') as file:
        file.write('FAILED SSH LOGIN ATTEMPTS PER USER\n')
        for user in user_data:
            file.write(f'{user[0]}: {user[1]}\n')
        file.write('-' * 20 + '\n')
        for log in log_list:
            file.write(log)
        file.close()
    print(f'Parsed log file saved as {output_file}')


def main():
    """Main function to run the program.
    """
    if len(sys.argv) != 3:
        print('Usage: ssh_failed_logins.py [/path/to/auth.log] [output file]')
        sys.exit(0)

    log_file = sys.argv[1]
    output_file = os.path.join(os.path.expanduser('~'), sys.argv[2])
    regex_pattern = re.compile(r'''
                               ^(\w{3}\s+\d{1,2} \d{2}:\d{2}:\d{2}).    # Timestamp
                               *Failed password for (\w*) from
                               (\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b)      # IP Address
                               ''')

    if not os.path.exists(log_file):
        print(f'Log file \'{log_file}\' does not exist. Exiting...')
        sys.exit(0)
    elif os.path.exists(output_file):
        overwrite_input = input(f'WARNING: The file \'{output_file}\' already exists! \
            Would you like to overwrite? (y/n): ')
        if overwrite_input.lower() != 'y':
            print('Exiting...')
            sys.exit(0)

    returned_logs, user_stats = search_log(log_file, regex_pattern)
    user_stats = sorted(user_stats.items(), key=operator.itemgetter(1), reverse=True)
    create_file(output_file, returned_logs, user_stats)
    sys.exit(0)


if __name__ == "__main__":
    main()
