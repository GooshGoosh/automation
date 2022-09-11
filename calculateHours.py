#!/usr/bin/env python3

# calculateHours.py - Reads a csv file that contains the days of the week and the hours worked on each day.


import csv


def read_file(fileLocation):
    csv.register_dialect('hoursDialect', skipinitialspace=True, strict=True)
    hoursFile = csv.DictReader(open(fileLocation), dialect='hoursDialect')
    hoursList = []
    for data in hoursFile:
        hoursList.append(data)
    return hoursList


def process_data(hoursList):
    hoursDict = {}
    for dict in hoursList:
        for day in dict:
            if day not in hoursDict:
                hoursDict[day] = float(dict[day])
            else:
                hoursDict[day] += float(dict[day])
    return hoursDict


def write_report(hoursDict, reportFile):
    with open(reportFile, 'w+') as file:
        for i in hoursDict:
            file.write('Total hours worked on {}: {:.1f}\n'.format(i, hoursDict[i]))
    file.close()

hoursList = read_file('/path/to/hours-worked.csv')
hoursDict = process_data(hoursList)
print(hoursList)
print()
print(hoursDict)
print()
write_report(hoursDict, '/path/to/hours-report.txt')
