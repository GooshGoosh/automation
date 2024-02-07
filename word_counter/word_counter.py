'''
word_counter.py - Reads in a text file and searches through to find words of a
specific length (e.g. 4-letter words, 5-letter words, etc.) and creates a csv
file of the word length, the number of n-letter words in the text, and the number
of different lines that those n-letter words appear within the text.
'''


import csv
import re


TEXT_FILE = 'word_counter/moby-dick.txt'
OUTPUT_FILE = 'word_counter/moby-dick-words.csv'
list_of_data = []
HEADERS = ['Word Length', 'Num of Words', 'Num of Lines']


def read_text_file(text_file):
    """Reads the text from the given file.

    Args:
        TEXT_FILE (str): Path to a text file.

    Returns:
        list: Lines from the given text file.
    """
    with open(text_file, 'r', encoding='UTF-8') as file:
        file_lines = file.readlines()
    file.close()
    return file_lines


def remove_newlines(line_list):
    """Removes newlines from the given list of text.

    Args:
        line_list (list): Text lines from a text file.

    Returns:
        list: New list of text lines without newlines.
    """
    new_list = [i.strip() for i in line_list]
    return new_list


def one_letter_words(text):
    """Searches for one-letter words in the given text list.

    Args:
        text (list): List of text lines to search through.

    Returns:
        tuple: Data for the letter count, number of matches, and number of lines
        searched through.
    """
    global list_of_data
    num_of_lines, matches = 0, 0
    for line in text:
        result = re.findall(r'\b[a-zA-Z]{1}\b', line)
        if len(result) > 0:
            matches += len(result)
            num_of_lines += 1
    data = (1, matches, num_of_lines)
    list_of_data.append(data)
    return data


def two_letter_words(text):
    """Searches for two-letter words in the given text list.

    Args:
        text (list): List of text lines to search through.

    Returns:
        tuple: Data for the letter count, number of matches, and number of lines
        searched through.
    """
    global list_of_data
    num_of_lines, matches = 0, 0
    for line in text:
        result = re.findall(r'\b[a-zA-Z]{2}\b', line)
        if len(result) > 0:
            matches += len(result)
            num_of_lines += 1
    data = (2, matches, num_of_lines)
    list_of_data.append(data)
    return data


def three_letter_words(text):
    """Searches for three-letter words in the given text list.

    Args:
        text (list): List of text lines to search through.

    Returns:
        tuple: Data for the letter count, number of matches, and number of lines
        searched through.
    """
    global list_of_data
    num_of_lines, matches = 0, 0
    for line in text:
        result = re.findall(r'\b[a-zA-Z]{3}\b', line)
        if len(result) > 0:
            matches += len(result)
            num_of_lines += 1
    data = (3, matches, num_of_lines)
    list_of_data.append(data)
    return data


def four_letter_words(text):
    """Searches for four-letter words in the given text list.

    Args:
        text (list): List of text lines to search through.

    Returns:
        tuple: Data for the letter count, number of matches, and number of lines
        searched through.
    """
    global list_of_data
    num_of_lines, matches = 0, 0
    for line in text:
        result = re.findall(r'\b[a-zA-Z]{4}\b', line)
        if len(result) > 0:
            matches += len(result)
            num_of_lines += 1
    data = (4, matches, num_of_lines)
    list_of_data.append(data)
    return data


def five_letter_words(text):
    """Searches for five-letter words in the given text list.

    Args:
        text (list): List of text lines to search through.

    Returns:
        tuple: Data for the letter count, number of matches, and number of lines
        searched through.
    """
    global list_of_data
    num_of_lines, matches = 0, 0
    for line in text:
        result = re.findall(r'\b[a-zA-Z]{5}\b', line)
        if len(result) > 0:
            matches += len(result)
            num_of_lines += 1
    data = (5, matches, num_of_lines)
    list_of_data.append(data)
    return data


def six_letter_words(text):
    """Searches for six-letter words in the given text list.

    Args:
        text (list): List of text lines to search through.

    Returns:
        tuple: Data for the letter count, number of matches, and number of lines
        searched through.
    """
    global list_of_data
    num_of_lines, matches = 0, 0
    for line in text:
        result = re.findall(r'\b[a-zA-Z]{6}\b', line)
        if len(result) > 0:
            matches += len(result)
            num_of_lines += 1
    data = (6, matches, num_of_lines)
    list_of_data.append(data)
    return data


def seven_letter_words(text):
    """Searches for seven-letter words in the given text list.

    Args:
        text (list): List of text lines to search through.

    Returns:
        tuple: Data for the letter count, number of matches, and number of lines
        searched through.
    """
    global list_of_data
    num_of_lines, matches = 0, 0
    for line in text:
        result = re.findall(r'\b[a-zA-Z]{7}\b', line)
        if len(result) > 0:
            matches += len(result)
            num_of_lines += 1
    data = (7, matches, num_of_lines)
    list_of_data.append(data)
    return data


def generate_csv(data, output_file, headers):
    """Generates a csv file of the data given.

    Args:
        data (list): List of tuples of data found from the letter count searches.
        output_file (str): Path/name of the output file.
        headers (list): Headers for the CSV file.
    """
    with open(output_file, 'w', newline='', encoding='UTF-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)
        file.close()


def generate_report(csv_file):
    """Generates a report of the data read from the CSV file and prints it to the
    screen.

    Args:
        csv_file (str): Path/name to the CSV file to read from.
    """
    with open(csv_file, 'r', encoding='UTF-8') as file:
        dict_reader = csv.DictReader(file)
        for row in dict_reader:
            print(f"There are {row['Num of Words']} {row['Word Length']}-letter words \
                in the file that appear on {row['Num of Lines']} different lines.")
        file.close()


def main():
    """Main function to run the program.
    """
    try:
        text_file_lines = read_text_file(TEXT_FILE)
        text_file_lines = remove_newlines(text_file_lines)
        one_letter_words(text_file_lines)
        two_letter_words(text_file_lines)
        three_letter_words(text_file_lines)
        four_letter_words(text_file_lines)
        five_letter_words(text_file_lines)
        six_letter_words(text_file_lines)
        seven_letter_words(text_file_lines)
        generate_csv(list_of_data, OUTPUT_FILE, HEADERS)
        generate_report(OUTPUT_FILE)
    except FileNotFoundError:
        print(f"\nFile '{TEXT_FILE}' does not exist\n")


if __name__ == "__main__":
    main()
