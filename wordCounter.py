#!/usr/bin/env python3

# wordCounter.py - Reads in a text file and searches through to find words of a specific length (e.g. 4-letter words, 5-letter words, etc.)
# and creates a csv file of the word length, the number of n-letter words in the text, and the number of different lines that those
# n-letter words appear within the text.


import csv
import re
import os


textFile = 'moby-dick.txt'
outputFile = 'moby-dick-words.csv'
listOfData = []
headers = ['Word Length', 'Num of Words', 'Num of Lines']


def read_text_file(textFile):
    with open(textFile, 'r') as file:
        fileLines = file.readlines()
    file.close()
    return fileLines


def remove_newlines(list):
    newList = [i.strip() for i in list]
    return newList


def one_letter_words(text):
    global listOfData
    numOfLines, matches = 0, 0
    for line in text:
        result = re.findall(r'\b[a-zA-Z]{1}\b', line)
        if len(result) > 0:
            matches += len(result)
            numOfLines += 1
    data = (1, matches, numOfLines)
    listOfData.append(data)
    return data


def two_letter_words(text):
    global listOfData
    numOfLines, matches = 0, 0
    for line in text:
        result = re.findall(r'\b[a-zA-Z]{2}\b', line)
        if len(result) > 0:
            matches += len(result)
            numOfLines += 1
    data = (2, matches, numOfLines)
    listOfData.append(data)
    return data


def three_letter_words(text):
    global listOfData
    numOfLines, matches = 0, 0
    for line in text:
        result = re.findall(r'\b[a-zA-Z]{3}\b', line)
        if len(result) > 0:
            matches += len(result)
            numOfLines += 1
    data = (3, matches, numOfLines)
    listOfData.append(data)
    return data


def four_letter_words(text):
    global listOfData
    numOfLines, matches = 0, 0
    for line in text:
        result = re.findall(r'\b[a-zA-Z]{4}\b', line)
        if len(result) > 0:
            matches += len(result)
            numOfLines += 1
    data = (4, matches, numOfLines)
    listOfData.append(data)
    return data


def five_letter_words(text):
    global listOfData
    numOfLines, matches = 0, 0
    for line in text:
        result = re.findall(r'\b[a-zA-Z]{5}\b', line)
        if len(result) > 0:
            matches += len(result)
            numOfLines += 1
    data = (5, matches, numOfLines)
    listOfData.append(data)
    return data


def six_letter_words(text):
    global listOfData
    numOfLines, matches = 0, 0
    for line in text:
        result = re.findall(r'\b[a-zA-Z]{6}\b', line)
        if len(result) > 0:
            matches += len(result)
            numOfLines += 1
    data = (6, matches, numOfLines)
    listOfData.append(data)
    return data


def seven_letter_words(text):
    global listOfData
    numOfLines, matches = 0, 0
    for line in text:
        result = re.findall(r'\b[a-zA-Z]{7}\b', line)
        if len(result) > 0:
            matches += len(result)
            numOfLines += 1
    data = (7, matches, numOfLines)
    listOfData.append(data)
    return data


def generate_csv(data, outputFile, headers):
    with open(outputFile, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)
        file.close()


def generate_report(csvFile):
    with open(csvFile, 'r') as file:
        dictReader = csv.DictReader(file)
        for row in dictReader:
            print('There are {} {}-letter words in the file that appear on {} different lines.'.format(row['Num of Words'],row['Word Length'],row['Num of Lines']))
        file.close()
        

def main():
    try:
        textFileLines = read_text_file(textFile)
        textFileLines = remove_newlines(textFileLines)
        oneLetterWords = one_letter_words(textFileLines)
        twoLetterWords = two_letter_words(textFileLines)
        threeLetterWords = three_letter_words(textFileLines)
        fourLetterWords = four_letter_words(textFileLines)
        fiveLetterWords = five_letter_words(textFileLines)
        sixLetterWords = six_letter_words(textFileLines)
        sevenLetterWords = seven_letter_words(textFileLines)
        generate_csv(listOfData, outputFile, headers)
        generate_report(outputFile)
    except FileNotFoundError:
        print("\nFile does not exist\n")


if __name__ == "__main__":
    main()
