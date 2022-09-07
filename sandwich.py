#!/usr/bin/env python3

# sandwich.py - A program that asks the user for their sandwich preferences.
# This program uses the PyInputPlus module to ensure valid input.
# The program will total the sandwich cost at the end once the user is finished building their sandwich.


import pyinputplus as pyip
import random
import sys


# Track the cost and number of sandwiches
total = 0.00
numOfSandwiches = 0
sandwichComponents = {'White': 0.50, 'Wheat': 0.40, 'Sourdough': 0.65,
                      'Chicken': 1.50, 'Turkey': 1.25, 'Ham': 1.50, 'Tofu': 1.00,
                      'Cheddar': 0.50, 'Swiss': 0.60, 'Mozzarella': 0.75,
                      'Mayo': 0.10, 'Mustard': 0.10, 'Lettuce': 0.15, 'Tomato': 0.15
                      }


def sandwich_maker():
    # Set global variables
    global total
    global numOfSandwiches
    global sandwichComponents
    sandwich = []
    price = 0.00
    
    answer = pyip.inputYesNo(prompt='\nWould you like to make a sandwich?\n')
    if answer == "no":
        print('\nOk, no sandwich for you. Goodbye!\n')
        sys.exit()
    
    while answer == "yes":
        #TODO: Using a dictionary, add a price for each option and add it to the total to calculate after the number of sandwiches has been ordered
        
        # Ask for the type of bread: wheat, white, sourdough
        bread = pyip.inputMenu(['White', 'Wheat', 'Sourdough'], prompt='\nWhat type of bread would you like?\n', numbered=True)
        sandwich.append(bread)
        price += sandwichComponents[bread]
        
        # Ask for the type of protein: chicken, turkey, ham, or tofu
        protein = pyip.inputMenu(['Chicken', 'Turkey', 'Ham', 'Tofu'], prompt='\nWhat type of protein would you like?\n', numbered=True)
        sandwich.append(protein)
        price += sandwichComponents[protein]
 
        # Ask if they want cheese
        cheese = pyip.inputYesNo(prompt='\nWould you like cheese?\n')
        
        # Ask for the type of cheese: cheddar, swiss, mozzarella
        if cheese == "yes":
            cheese = pyip.inputMenu(['Cheddar', 'Swiss', 'Mozzarella'], prompt='\nWhat kind of cheese would you like?\n', numbered=True)
            sandwich.append(cheese)
            price += sandwichComponents[cheese]
        
        # Ask if they want mayo, mustard, lettuce, or tomato
        condiments = pyip.inputYesNo(prompt='\nWould you like condiments/veggies?\n')
        while condiments == "yes":
            condiments = pyip.inputMenu(['Mayo', 'Mustard', 'Lettuce', 'Tomato'], prompt='\nWhich one of these would you like?\n', numbered=True)
            sandwich.append(condiments)
            price += sandwichComponents[condiments]
            condiments = pyip.inputYesNo(prompt='\nWould you like to add more condiments/veggies?\n')
        
        # Ask how many sandwiches they want (at least 1)
        print('\nYour current sandwich:')
        for item in sandwich:
            print(f'{item.ljust(12)}...${sandwichComponents[item]:.2f}')
                  
        numOfSandwiches += pyip.inputInt(prompt='\nHow many of these sandwiches would you like?\n', min=1)
        price *= numOfSandwiches
        total += price
        
        # Ask if they want to make another sandwich
        answer = pyip.inputYesNo(prompt='\nWould you like to make another sandwich?\n')
        

sandwich_maker()

# Total the amount and number of sandwiches
print(f'\nThe total cost of {numOfSandwiches} sandwiches: ${total:.2f}\n')
