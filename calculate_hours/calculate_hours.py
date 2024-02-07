'''
calculate_hours.py - Reads a csv file that contains the days of the week and the
hours worked on each day.
'''


import csv


def read_file(file_location):
    """Reads in the data from the CSV file.

    Args:
        file_location (str): Path to the CSV file.

    Returns:
        list: List of dictionaries containing the data from the CSV file.
    """
    csv.register_dialect('hoursDialect', skipinitialspace=True, strict=True)
    with open(file_location, 'r', encoding='UTF-8') as file:
        hours_file = csv.DictReader(file, dialect='hoursDialect',)
        hours_list = []
        for data in hours_file:
            hours_list.append(data)
    return hours_list


def process_data(hours_list):
    """Processes the data in the given list and transforms it into a single dict.

    Args:
        hours_list (list): List of dictionaries containing the data from the CSV file.

    Returns:
        dict: Dictionary of the number of hours worked for each day of the week.
    """
    hours_dict = {}
    for dct in hours_list:
        for day in dct:
            if day not in hours_dict:
                hours_dict[day] = float(dct[day])
            else:
                hours_dict[day] += float(dct[day])
    return hours_dict


def write_report(hours_dict, report_file):
    """Writes the results to a separate report file.

    Args:
        hours_dict (dict): The number of hours worked for each day of the week.
        report_file (str): Path to the desired save location for the report file.
    """
    with open(report_file, 'w+', encoding='UTF-8') as file:
        for i in hours_dict:
            file.write(f'Total hours worked on {i}: {hours_dict[i]:.1f}\n')
    file.close()


def main():
    """Main function to run the program.
    """
    hours_list = read_file('calculate_hours/hours-worked.csv')
    hours_dict = process_data(hours_list)
    print(hours_list)
    print()
    print(hours_dict)
    print()
    write_report(hours_dict, 'calculate_hours/hours-report.txt')


if __name__ == "__main__":
    main()
