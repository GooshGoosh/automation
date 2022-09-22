#!/usr/bin/env python3

# operations.py - This program will give the user 10 mathematical questions based on the operator of their choosing.
# The user may also choose a "gauntlet" option which will give them 20 questions with 5 questions using each operator.
# The user will also have the option of specifying 1, 2, or 3-digit numbers for each question.
# The results will be printed to the screen once the test has concluded.


import random
import time
import pyinputplus as pyip


# Set program variables.
questions = 0
correctAnswers = 0
incorrectAnswers = 0


# Define program functions.
def single_add():
    global questions
    global correctAnswers
    global incorrectAnswers
    a = random.randint(0,9)
    b = random.randint(0,9)
    result = a + b
    print('-' * 20)
    answer = pyip.inputNum(prompt=f'\nWhat is {a} + {b}?\n')
    time.sleep(1)
    print(f'\nCorrect answer: {result}')
    time.sleep(2)
    questions += 1
    if result == answer:
        correctAnswers += 1
    else:
        incorrectAnswers += 1


def double_add():
    global questions
    global correctAnswers
    global incorrectAnswers
    a = random.randint(0,99)
    b = random.randint(0,99)
    result = a + b
    print('-' * 20)
    answer = pyip.inputNum(prompt=f'\nWhat is {a} + {b}?\n')
    time.sleep(1)
    print(f'\nCorrect answer: {result}')
    time.sleep(2)
    questions += 1
    if result == answer:
        correctAnswers += 1
    else:
        incorrectAnswers += 1
    
    
def triple_add():
    global questions
    global correctAnswers
    global incorrectAnswers
    a = random.randint(0,999)
    b = random.randint(0,999)
    result = a + b
    print('-' * 20)
    answer = pyip.inputNum(prompt=f'\nWhat is {a} + {b}?\n')
    time.sleep(1)
    print(f'\nCorrect answer: {result}')
    time.sleep(2)
    questions += 1
    if result == answer:
        correctAnswers += 1
    else:
        incorrectAnswers += 1
    

def single_sub():
    global questions
    global correctAnswers
    global incorrectAnswers
    a = random.randint(0,9)
    b = random.randint(0,9)
    result = a - b
    print('-' * 20)
    answer = pyip.inputNum(prompt=f'\nWhat is {a} - {b}?\n')
    time.sleep(1)
    print(f'\nCorrect answer: {result}')
    time.sleep(2)
    questions += 1
    if result == answer:
        correctAnswers += 1
    else:
        incorrectAnswers += 1
    

def double_sub():
    global questions
    global correctAnswers
    global incorrectAnswers
    a = random.randint(0,99)
    b = random.randint(0,99)
    result = a - b
    print('-' * 20)
    answer = pyip.inputNum(prompt=f'\nWhat is {a} - {b}?\n')
    time.sleep(1)
    print(f'\nCorrect answer: {result}')
    time.sleep(2)
    questions += 1
    if result == answer:
        correctAnswers += 1
    else:
        incorrectAnswers += 1
    

def triple_sub():
    global questions
    global correctAnswers
    global incorrectAnswers
    a = random.randint(0,999)
    b = random.randint(0,999)
    result = a - b
    print('-' * 20)
    answer = pyip.inputNum(prompt=f'\nWhat is {a} - {b}?\n')
    time.sleep(1)
    print(f'\nCorrect answer: {result}')
    time.sleep(2)
    questions += 1
    if result == answer:
        correctAnswers += 1
    else:
        incorrectAnswers += 1


def single_multi():
    global questions
    global correctAnswers
    global incorrectAnswers
    a = random.randint(0,9)
    b = random.randint(0,9)
    result = a * b
    print('-' * 20)
    answer = pyip.inputNum(prompt=f'\nWhat is {a} * {b}?\n')
    time.sleep(1)
    print(f'\nCorrect answer: {result}')
    time.sleep(2)
    questions += 1
    if result == answer:
        correctAnswers += 1
    else:
        incorrectAnswers += 1
        

def double_multi():
    global questions
    global correctAnswers
    global incorrectAnswers
    a = random.randint(0,99)
    b = random.randint(0,99)
    result = a * b
    print('-' * 20)
    answer = pyip.inputNum(prompt=f'\nWhat is {a} * {b}?\n')
    time.sleep(1)
    print(f'\nCorrect answer: {result}')
    time.sleep(2)
    questions += 1
    if result == answer:
        correctAnswers += 1
    else:
        incorrectAnswers += 1


def triple_multi():
    global questions
    global correctAnswers
    global incorrectAnswers
    a = random.randint(0,999)
    b = random.randint(0,999)
    result = a * b
    print('-' * 20)
    answer = pyip.inputNum(prompt=f'\nWhat is {a} * {b}?\n')
    time.sleep(1)
    print(f'\nCorrect answer: {result}')
    time.sleep(2)
    questions += 1
    if result == answer:
        correctAnswers += 1
    else:
        incorrectAnswers += 1
        

def single_div():
    global questions
    global correctAnswers
    global incorrectAnswers
    a = random.randint(0,9)
    b = random.randint(0,9)
    result = int(a / b)
    print('-' * 20)
    answer = pyip.inputNum(prompt=f'\nWhat is {a} / {b}?\n')
    time.sleep(1)
    print(f'\nCorrect answer: {result}')
    time.sleep(2)
    questions += 1
    if result == answer:
        correctAnswers += 1
    else:
        incorrectAnswers += 1
        

def double_div():
    global questions
    global correctAnswers
    global incorrectAnswers
    a = random.randint(0,99)
    b = random.randint(0,99)
    result = int(a / b)
    print('-' * 20)
    answer = pyip.inputNum(prompt=f'\nWhat is {a} / {b}?\n')
    time.sleep(1)
    print(f'\nCorrect answer: {result}')
    time.sleep(2)
    questions += 1
    if result == answer:
        correctAnswers += 1
    else:
        incorrectAnswers += 1
        

def triple_div():
    global questions
    global correctAnswers
    global incorrectAnswers
    a = random.randint(0,999)
    b = random.randint(0,999)
    result = int(a / b)
    print('-' * 20)
    answer = pyip.inputNum(prompt=f'\nWhat is {a} / {b}?\n')
    time.sleep(1)
    print(f'\nCorrect answer: {result}')
    time.sleep(2)
    questions += 1
    if result == answer:
        correctAnswers += 1
    else:
        incorrectAnswers += 1


def main():
    # Get the user's desired test mode and the max number of digits for each number.
    print()
    testMode = pyip.inputMenu(['Addition', 'Subtraction', 'Multiplication', 'Division', 'All'], numbered=True)
    numOfDigits = pyip.inputMenu(['1-digit', '2-digit', '3-digit'], numbered=True, prompt="\nSelect the max number of digits for each number:\n")


    # Call program functions based on the user's settings.
    if testMode == "Addition":
        if numOfDigits == "1-digit":
            while questions < 10:
                single_add()
        elif numOfDigits == "2-digit":
            while questions < 10:
                double_add()
        elif numOfDigits == "3-digit":
            while questions < 10:
                triple_add()

    if testMode == "Subtraction":
        if numOfDigits == "1-digit":
            while questions < 10:
                single_sub()
        elif numOfDigits == "2-digit":
            while questions < 10:
                double_sub
        elif numOfDigits == "3-digit":
            while questions < 10:
                triple_sub()
                    
    if testMode == "Multiplication":
        if numOfDigits == "1-digit":
            while questions < 10:
                single_multi()
        elif numOfDigits == "2-digit":
            while questions < 10:
                double_multi()
        elif numOfDigits == "3-digit":
            while questions < 10:
                triple_multi()
                    
    if testMode == "Division":
        if numOfDigits == "1-digit":
            while questions < 10:
                single_div()
        elif numOfDigits == "2-digit":
            while questions < 10:
                double_div()
        elif numOfDigits == "3-digit":
            while questions < 10:
                triple_div()

    if testMode == "All":
        if numOfDigits == "1-digit":
            while questions < 20:
                single_add()
                single_sub()
                single_multi()
                single_div()
        elif numOfDigits == "2-digit":
            while questions < 20:
                double_add()
                double_sub()
                double_multi()
                double_div()
        elif numOfDigits == "3-digit":
            while questions < 20:
                triple_add()
                triple_sub()
                triple_multi()
                triple_div()


    # Print results of test.
    print()
    print('-' * 30)
    print('\nHere are your results:')
    print(f'Questions: {questions}')
    print(f'Correct answers: {correctAnswers}')
    print(f'Incorrect answers: {incorrectAnswers}')
    time.sleep(5)


if __name__ == "__main__":
    main()
