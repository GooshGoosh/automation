#!/usr/bin/env python3

# eldenRing.py - Mini Elden Ring-based game that lets the user fight the tutorial boss Soldier of Godrick
# and a majority of the field, mini, and main bosses from Elden Ring. Uses random numbers to decide if the Tarnished won/lost the fight.
#
# TODO:
# Similar to rock, paper, scissors; The player chooses either 'Attack', 'Block', or 'Roll' as an action.
# The boss will randomly get assigned 'Quick Attack', 'Delay Attack', 'Grab Attack'. 
# The winning order is as follows:
# Attack > Delay Attack, Attack = Quick Attack, Attack = Grab Attack
# Block > Quick Attack, Block > Delay Attack, Block < Grab Attack
# Roll > Quick Attack, Roll > Grab Attack, Roll > Delay Attack
#
# Allows class selection via pyinputplus module and a list of .csv files stored in /home/user/Documents/elden_ring/classes.
# The .csv file contains the class name followed by each stat and their values for each Elden Ring starting class (e.g. Vig,0).
# The stats are followed by the 6 equipment slots for the character including Right Hand, Left Hand, Helm, Torso, Wrists, and Legs.
 

import random
import sys
import os
import time
import pyinputplus as pyip
import csv


def grace(): 
    global playerCurrentHealth 
                                        
    print('\nRest...')                                                      # Rest and prepare for the next battle.
    time.sleep(3)
    playerCurrentHealth = playerMaxHealth                                   # Heal the player's current health to their max health.
    print('Fully healed and preparing for next battle...')
    time.sleep(2)
    print('-' * 30)


def field_boss():
    global playerCurrentHealth
    bossHealth = 500                                                            # Set the boss health and attack rating.
    bossAttack = 15
    bossFile = open(os.path.join(bossesPath, 'field-boss-list.txt'))            # Read the field boss list file and create a list of field bosses.
    bossList = bossFile.readlines()
    bossFile.close()
    boss = random.choice(bossList)                                              # Grab a random boss from the provided list for the player to battle.

    print('\n' + boss, end='')
    while playerCurrentHealth > 0 and bossHealth > 0:
        bossAction = random.randint(1, 2)
        print(f'\nPlayer HP: {playerCurrentHealth}')                            # Print current player and boss health.
        print(f'Boss HP: {bossHealth}')
        print('-' * 30)
        playerAction = pyip.inputInt('\nEnter a 1 or 2: ', min=1, max=2)        # Have the player input a 1 or a 2.

        if int(playerAction) == bossAction:                                     # Check player and boss actions.
            print (f'\nYou deal {playerAttack} damage!\n')                      # If player won, then player deals damage to boss. 
            bossHealth -= playerAttack 
            time.sleep(1.5)       
        else:                                                                   
            print (f'\nYou take {bossAttack} damage!\n')                        # If boss won, then boss deals damage to player.
            playerCurrentHealth -= bossAttack
            time.sleep(1.5)
    if playerCurrentHealth <= 0:                                                # Check if the player's current health is at or below 0.
        print('\nYOU DIED\n')                                                   # If so, then exit the program.
        time.sleep(1)
        sys.exit(0)
    else:
        print('\nENEMY FELLED\n')
        time.sleep(1)


def mini_boss():
    global playerCurrentHealth
    bossHealth = 800                                                            # Set the boss health and attack rating.
    bossAttack = 20
    bossFile = open(os.path.join(bossesPath, 'mini-boss-list.txt'))             # Read the mini boss list file and create a list of mini bosses.
    bossList = bossFile.readlines()
    bossFile.close()
    boss = random.choice(bossList)                                              # Grab a random boss from the provided list for the player to battle.

    print('\n' + boss, end='')
    while playerCurrentHealth > 0 and bossHealth > 0:
        bossAction = random.randint(1, 2)
        print(f'\nPlayer HP: {playerCurrentHealth}')                            # Print current player and boss health.
        print(f'Boss HP: {bossHealth}')
        print('-' * 30)
        playerAction = pyip.inputInt('\nEnter a 1 or 2: ', min=1, max=2)        # Have the player input a 1 or a 2.

        if int(playerAction) == bossAction:                                     # Check player and boss actions.
            print (f'\nYou deal {playerAttack} damage!\n')                      # If player won, then player deals damage to boss. 
            bossHealth -= playerAttack 
            time.sleep(1.5)       
        else:                                                                   
            print (f'\nYou take {bossAttack} damage!\n')                        # If boss won, then boss deals damage to player.
            playerCurrentHealth -= bossAttack
            time.sleep(1.5)
    if playerCurrentHealth <= 0:                                                # Check if the player's current health is at or below 0.
        print('\nYOU DIED\n')                                                   # If so, then exit the program.
        time.sleep(1)
        sys.exit(0)
    else:
        print('\nENEMY FELLED\n')
        time.sleep(1)


def main_boss():
    global playerCurrentHealth
    bossHealth = 1200                                                               # Set the boss health and attack rating.
    bossAttack = 25
    bossFile = open(os.path.join(bossesPath, 'main-boss-list.txt'))                 # Read the main boss list file and create a list of main bosses.
    bossList = bossFile.readlines()
    bossFile.close()
    boss = random.choice(bossList)                                                  # Grab a random boss from the provided list for the player to battle.

    print('\n' + boss, end='')
    while playerCurrentHealth > 0 and bossHealth > 0:
        bossAction = random.randint(1, 2)
        playerAction = pyip.inputInt('\nEnter a number 1-2: ', min=1, max=2)        # Have the player input a 1 or 2.                   
        if int(playerAction) == bossAction:                                         # Check player and boss actions.
            print (f'\nYou deal {playerAttack} damage!\n')                          # If player won, then player deals damage to boss. 
            bossHealth -= playerAttack 
            time.sleep(1.5)       
        else:                                                                   
            print (f'\nYou take {bossAttack} damage!\n')                            # If boss won, then boss deals damage to player.
            playerCurrentHealth -= bossAttack
            time.sleep(1.5)
    if playerCurrentHealth <= 0:                                                    # Check if the player's current health is at or below 0.
        print('\nYou Died')
        print('Put these foolish ambitions to rest.\n')                             # Print a boss victory dialogue after defeating the player.
        time.sleep(3)                                                               # Let the player read the message before the program exits.
        sys.exit(0)
    elif bossHealth <= 0:
        print('\nGREAT ENEMY FELLED')                                               # Check if boss or player won. Print a boss death dialogue if the player won.
        print('''
        I shall remember thee, Tarnished.
        Smouldering with thy meagre flame.
        Cower in Fear. Of the Night.
        ''')
        time.sleep(3)                                                               # Let the player read the message before the program exits.
        sys.exit(0)


##################
# VARIABLE BLOCK #
##################

playerMaxHealth = 0         # Store the player's max health.
playerCurrentHealth = 0     # Store the player's current health.
playerAttack = 0            # Store the player's attack rating of their weapon(s).
playerShield = False        # Store the status of a shield in the player's left hand.

# Get the name of the currently logged in user and create a path to the directory
# that stores the Elden Ring class .csv files.
user = os.getlogin()
bossesPath = os.path.abspath(f'./elden_ring/bosses/')
classesPath = os.path.abspath(f'./elden_ring/classes/')
starterWeaponsPath = os.path.abspath(f'./elden_ring/weapons/starter-weapons.csv')

stats = {
    'Class:': "",
    'Vig:': 0,
    'Mnd:': 0,
    'End:': 0,
    'Str:': 0,
    'Dex:': 0,
    'Int:': 0,
    'Fth:': 0,
    'Arc:': 0
}   # Dictionary to store the player's stats.

equipment = {
    'Right Hand:': "",
    'Left Hand:': "",
    'Helm:': "",
    'Torso:': "",
    'Wrists:': "",
    'Legs:': ""
}   # Dictionary to track the player's current equipment.

inventory = {
    
}   # Dictionary to track the player's inventory.


#########################
# CLASS SELECTION BLOCK #
#########################


# Clear the screen.
os.system('cls' if os.name == 'nt' else 'clear')                    

character = pyip.inputMenu(['Astrologer', 'Bandit', 'Confessor', 'Hero', 'Prisoner',            # Create a menu of the classes for the player to choose from.
                            'Prophet', 'Samurai', 'Vagabond', 'Warrior', 'Wretch',
                            'Quit'], numbered=True)

if character == 'Quit':
    sys.exit()                                                                                  # Exit the program if the player chooses the 'Quit' option.
    
print('Loading class...')                                                                       # "Load" the class and clear the screen
time.sleep(0.5)
os.system('cls' if os.name == 'nt' else 'clear')


character = character.lower()                                                                   # Set the character/class choice to all lowercase letters.
with open(os.path.join(classesPath, character + '.csv')) as csvfile:                            # Join the path to the classes .csv files and the chosen class
    classReader = csv.reader(csvfile)                                                           # to get the .csv for the chosen class.
    for row in classReader:
        if row[0] in stats.keys():                                                              # Store the player's stats
            if row[0] == "Class:":
                stats[row[0]] = row[1]
            else:
                stats[row[0]] = int(row[1])                                              
        elif row[0] in equipment.keys():                                                        # Fill the slots for the player's equipment.
            equipment[row[0]] = row[1]
csvfile.close()

with open(starterWeaponsPath) as csvfile:                                                       # Search through the starter weapons file to find the weapon
    weaponReader =csv.reader(csvfile)                                                           # that is in the player's right hand and give the player that
    for row in weaponReader:                                                                    # weapon's attack rating.
        if row[0] == equipment['Right Hand:']:                                                  
            playerAttack = int(row[1])
        if row[0] == equipment['Left Hand:']:                                                   # If the player is holding another weapon in their left hand,
            playerAttack += (int(row[1]) / 2)                                                   # Increase the player's attack rating by half of the left-handed weapon.
csvfile.close()

playerMaxHealth = (stats['Vig:'] * 10)                                                          # Get the player's max health.
playerCurrentHealth = playerMaxHealth                                                           # Set the player's current health equal to max health.
if "shield" in equipment['Left Hand:'].lower():                                                 # Determine if the player has a shield in their left hand.
    playerShield = True

for k, v in stats.items():                                                                      # Print the player's stats.
    print(k.ljust(7, ' ') + str(v))
print(f'\nHP: {playerMaxHealth}')
print(f'Attack: {playerAttack}') 
print('-' * 30)

for k, v in equipment.items():                                                                  # Print the player's currently equipped items.
    print(k.ljust(12,' ') + v)
print('-' * 30)

time.sleep(3)                                                                                   # Let the player read the chosen class' stats.
input("Press 'ENTER' to continue...")                                                           # Wait for the player to hit 'ENTER' to initiate the first battle.


#####################
# BOSS BATTLE BLOCK #
#####################

# Soldier of Godrick
print('\nSoldier of Godrick')                                               # Print the boss name.
bossHealth = 300                                                            # Set the boss health.
bossAttack = 10                                                             # Set the boss attack rating.
while playerCurrentHealth > 0 and bossHealth > 0:
    bossAction = random.randint(1, 2)                                       # Get boss action.
    print(f'\nPlayer HP: {playerCurrentHealth}')                            # Print current player and boss health.
    print(f'Boss HP: {bossHealth}')
    print('-' * 30)
    playerAction = pyip.inputInt('\nEnter a 1 or 2: ', min=1, max=2)        # Have the player input a 1 or a 2.

    if int(playerAction) == bossAction:                                     # Check player and boss actions.
        print (f'\nYou deal {playerAttack} damage!\n')                      # If player won, then player deals damage to boss. 
        bossHealth -= playerAttack 
        time.sleep(1.5)       
    else:                                                                   
        print (f'\nYou take {bossAttack} damage!\n')                        # If boss won, then boss deals damage to player.
        playerCurrentHealth -= bossAttack
        time.sleep(1.5)
        
if playerCurrentHealth <= 0:                                                # Check if the player's health is at or below 0.
    print('\nYOU DIED\n')                                                   # If so, then exit the program.
    time.sleep(1)
    sys.exit(0)
else:
    print('\nENEMY FELLED\n')
    time.sleep(1)

grace()             # Rest.

field_boss()        # Field boss.

grace()             # Rest.

mini_boss()         # Mini boss.

grace()             # Rest.

main_boss()         # Main Boss
