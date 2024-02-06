'''
check_sudo_commands.py - Takes the path to the auth.log file and parses it for
the date/time, user, and command that was run with sudo privileges. The data is
written to a file and the path to the output file can be specified; defaults to
the same directory that the script was run in.
'''


import os
import sys
import re


def create_file(output_file, log_list):
    """Writes the results of the search_log function to a new file.

    Args:
        output_file (str): The path and name of the output file.
        log_list (list): Data from the search_log output.
    """
    with open(output_file, 'w', encoding='UTF-8') as file:
        for log in log_list:
            file.write(log)
        file.close()
    print(f'Parsed log file saved as {output_file}')


def search_log(LOG_FILE, regex_pattern):
    """Search through a given log file using a given regex pattern and save the
    results in a list to return.

    Args:
        LOG_FILE (str): The path to the log file.
        regex_pattern (str): Regex pattern to use to search the log file.

    Returns:
        list: Matches found for the given regex in the log file.
    """
    returned_logs = []
    with open(LOG_FILE, mode='r', encoding='UTF-8') as file:
        for log in file.readlines():
            result = re.search(regex_pattern, log)
            if result is None:
                continue
            else:
                returned_logs.append(f'Date/Time: {result.group(1)}; \
                    User: {result.group(2)}; Command: {result.group(3)}\n')
        file.close()
    return returned_logs


def main():
    """The main function to run the program.
    """
    # Check if 2 command line arguments are given with the program call.
    if len(sys.argv) != 3:
        print('Usage: checkSudoCommands.py [path/to/auth.log] [output file]')
        sys.exit(0)

    LOG_FILE = sys.argv[1]
    output_file = os.path.join(os.path.expanduser('~'), sys.argv[2])
    regex_pattern = r'^(\w{3} \d{2} \d{2}:\d{2}:\d{2}).*sudo:\s+(\w+).*COMMAND=(.*$)'

    # Check if the log file to read exists and if the output file already exists.
    if not os.path.exists(LOG_FILE):
        print(f'Log file \'{LOG_FILE}\' does not exist.\nExiting...')
        sys.exit(0)
    elif os.path.exists(output_file):
        overwrite = input(f'WARNING: The file {output_file} already exists! \
            Would you like to overwrite? (Y/N): ')
        if overwrite.lower() != 'y':
            print('Exiting...')
            sys.exit(0)

    returned_logs = search_log(LOG_FILE, regex_pattern)
    create_file(output_file, returned_logs)
    sys.exit(0)


if __name__ == "__main__":
    main()
