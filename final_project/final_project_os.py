'''
final_project_os.py - Parses the final-project-logs.txt file for error and info
logs pertaining to a specific process. Records the type of log message and the
user who generated the log message. Tracks the number of times each error occurs
as well as the number of log message (error or info) that each user generates.
'''



import csv
import re
import operator


LOG_FILE = 'final-project-logs.txt'
INFO_PATTERN = r'.*ticky: INFO .*\(([\w .]*)\)'
ERROR_PATTERN = r'.*ticky: ERROR ([\w* .\']*).*\(([\w .]*)\)'
error_logs = {}
user_stats = {}


def add_info_log(regex_result):
    """Tracks the amount of INFO logs for each user in the given regex match results.

    Args:
        regex_result (re.Match): Match results for the INFO_PATTERN regex.
    """
    global user_stats
    if regex_result.group(1) not in user_stats:
        user_stats[regex_result.group(1)] = {}
        user_stats[regex_result.group(1)]['INFO'] = 1
    elif 'INFO' not in user_stats[regex_result.group(1)]:
        user_stats[regex_result.group(1)]['INFO'] = 1
    else:
        user_stats[regex_result.group(1)]['INFO'] += 1


def add_error_log(regex_result):
    """Tracks the amount of ERROR logs for each user in the given regex match results.

    Args:
        regex_result (re.Match): Match results for the ERROR_PATTERN regex.
    """
    global user_stats
    global error_logs
    if regex_result.group(1).strip() not in error_logs:
        error_logs[regex_result.group(1).strip()] = 1
        if regex_result.group(2) not in user_stats:
            user_stats[regex_result.group(2)] = {}
            user_stats[regex_result.group(2)]['ERROR'] = 1
        elif 'ERROR' not in user_stats[regex_result.group(2)]:
            user_stats[regex_result.group(2)]['ERROR'] = 1
        else:
            user_stats[regex_result.group(2)]['ERROR'] += 1
    else:
        error_logs[regex_result.group(1).strip()] += 1
        if regex_result.group(2) not in user_stats:
            user_stats[regex_result.group(2)] = {}
            user_stats[regex_result.group(2)]['ERROR'] = 1
        elif 'ERROR' not in user_stats[regex_result.group(2)]:
            user_stats[regex_result.group(2)]['ERROR'] = 1
        else:
            user_stats[regex_result.group(2)]['ERROR'] += 1


def create_error_file(output_file, data_list):
    """Creates an output file of the ERRORS found in the log.

    Args:
        output_file (str): Path/name of the output file.
        data_list (list): User ERROR data from the log file.
    """
    with open(output_file, 'w', newline='', encoding='UTF-8') as file:
        writer = csv.writer(file)
        for item in data_list:
            writer.writerow([item[0], item[1]])
        file.close()


def create_user_stats_file(output_file, data_list):
    """Creates an output file of the ERROR and INFO for users from the log file.

    Args:
        output_file (str): Path/name of the output file.
        data_list (list): User ERROR and INFO data from the log file.
    """
    with open(output_file, 'w', newline='', encoding='UTF-8') as file:
        writer = csv.writer(file)
        for item in data_list:
            if item[0] == 'jackowens':
                file.close()
                return
            if not isinstance(item[1], dict):
                writer.writerow([item[0], item[1], item[2]])
            else:
                writer.writerow([item[0], item[1].get('INFO', 0), item[1].get('ERROR', 0)])
        file.close()


def main():
    """Main function to run the program.
    """
    with open(LOG_FILE, 'r', encoding='UTF-8') as file:
        file_lines = file.readlines()
        for line in file_lines:
            result = re.search(INFO_PATTERN, line)
            if result is not None:
                add_info_log(result)
            else:
                result = re.search(ERROR_PATTERN, line)
                if result is not None:
                    add_error_log(result)
                else:
                    continue
        file.close()

    sort_user_stats = sorted(user_stats.items())
    sort_user_stats.insert(0, ('Username', 'INFO', 'ERROR'))
    sort_error_logs = sorted(error_logs.items(), key=operator.itemgetter(1), reverse=True)
    sort_error_logs.insert(0, ('Error', 'Count'))

    create_error_file('error_message.csv', sort_error_logs)
    create_user_stats_file('user_statistics.csv', sort_user_stats)


if __name__ == "__main__":
    main()
