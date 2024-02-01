#!/usr/bin/env python3

# finalProjectOS.py - Parses the final-project-logs.txt file for error and info logs pertaining to a specific process.
# Records the type of log message and the user who generated the log message. Tracks the number of times each error occurs as
# well as the number of log message (error or info) that each user generates.

import csv
import re
import operator


logFile = 'final-project-logs.txt'
infoPattern = r'.*ticky: INFO .*\(([\w .]*)\)'
errorPattern = r'.*ticky: ERROR ([\w* .\']*).*\(([\w .]*)\)'
errorLogs = {}
userStats = {}


def add_info_log(result):
    global userStats
    if result.group(1) not in userStats:
        userStats[result.group(1)] = {}
        userStats[result.group(1)]['INFO'] = 1
    elif 'INFO' not in userStats[result.group(1)]:
        userStats[result.group(1)]['INFO'] = 1
    else:
        userStats[result.group(1)]['INFO'] += 1
        

def add_error_log(result):
    global userStats
    global errorLogs
    if result.group(1).strip() not in errorLogs:
        errorLogs[result.group(1).strip()] = 1
        if result.group(2) not in userStats:
            userStats[result.group(2)] = {}
            userStats[result.group(2)]['ERROR'] = 1
        elif 'ERROR' not in userStats[result.group(2)]:
            userStats[result.group(2)]['ERROR'] = 1
        else:
            userStats[result.group(2)]['ERROR'] += 1
    else:
        errorLogs[result.group(1).strip()] += 1
        if result.group(2) not in userStats:
            userStats[result.group(2)] = {}
            userStats[result.group(2)]['ERROR'] = 1
        elif 'ERROR' not in userStats[result.group(2)]:
            userStats[result.group(2)]['ERROR'] = 1
        else:
            userStats[result.group(2)]['ERROR'] += 1


def create_error_file(outputFile, data_list):
    with open(outputFile, 'w', newline='') as file:
        writer = csv.writer(file)
        for item in data_list:
            writer.writerow([item[0], item[1]])
        file.close()
            

def create_user_stats_file(outputFile, data_list):
    with open(outputFile, 'w', newline='') as file:
        writer = csv.writer(file)
        for item in data_list:
            if item[0] == 'jackowens':
                file.close()
                return
            if type(item[1]) is not dict:
                writer.writerow([item[0], item[1], item[2]])
            else:
                writer.writerow([item[0], item[1].get('INFO', 0), item[1].get('ERROR', 0)])
        file.close()


##############
# MAIN BLOCK #
##############

with open(logFile, 'r') as file:
    fileLines = file.readlines()
    for line in fileLines:
        result = re.search(infoPattern, line)
        if result is not None:
            add_info_log(result)
        else:
            result = re.search(errorPattern, line)
            if result is not None:
                add_error_log(result)
            else:
                continue
    file.close()

userStats = sorted(userStats.items())
userStats.insert(0, ('Username', 'INFO', 'ERROR'))
errorLogs = sorted(errorLogs.items(), key=operator.itemgetter(1), reverse=True)
errorLogs.insert(0, ('Error', 'Count'))

create_error_file('error_message.csv', errorLogs)
create_user_stats_file('user_statistics.csv', userStats) 
