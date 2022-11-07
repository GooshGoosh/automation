#!/usr/bin/env python3

# TODO: Create a program that takes a chess board (pieces and spaces) and writes them to a file. The file will be a csv file and will be named after both players.
# The program will give two players the option to start a new game or to load a game from a file.
# Optional: the program will print a chess board to the screen after each player moves a piece.

import json
import os
import time
import sys
import datetime


def loadBoard():
    # Set the path to look for saved chess games.
    userHome = os.path.expanduser('~')
    chessDir = os.path.abspath(os.path.join(userHome, 'chess-games'))
    board = {}
    moves = {}
    
    # Check if the chess directory already exists and, if not, create it.
    if not os.path.isdir(chessDir):
        os.makedirs(chessDir)
    
    # Check if the players have a saved game file.
    time.sleep(0.5)
    answer = ''
    while answer.lower() != 'yes' and answer.lower() != 'no':
        answer = input('Do you have a saved game that you would like to load? (yes/no) > ')
    
    if answer == 'no':
        print('Loading default chess board...\n')
        time.sleep(1)
        
        board = {
            '1a': 'wr', '1b': 'wk', '1c': 'wb', '1d': 'WK', '1e': 'wq', '1f': 'wb', '1g': 'wk', '1h': 'wr',
            '2a': 'wp', '2b': 'wp', '2c': 'wp', '2d': 'wp', '2e': 'wp', '2f': 'wp', '2g': 'wp', '2h': 'wp',
            '3a': '  ', '3b': '  ', '3c': '  ', '3d': '  ', '3e': '  ', '3f': '  ', '3g': '  ', '3h': '  ',
            '4a': '  ', '4b': '  ', '4c': '  ', '4d': '  ', '4e': '  ', '4f': '  ', '4g': '  ', '4h': '  ',
            '5a': '  ', '5b': '  ', '5c': '  ', '5d': '  ', '5e': '  ', '5f': '  ', '5g': '  ', '5h': '  ',
            '6a': '  ', '6b': '  ', '6c': '  ', '6d': '  ', '6e': '  ', '6f': '  ', '6g': '  ', '6h': '  ',
            '7a': 'bp', '7b': 'bp', '7c': 'bp', '7d': 'bp', '7e': 'bp', '7f': 'bp', '7g': 'bp', '7h': 'bp',
            '8a': 'br', '8b': 'bk', '8c': 'bb', '8d': 'BK', '8e': 'bq', '8f': 'bb', '8g': 'bk', '8h': 'br'
        }   # Dictionary for a new, freshly set up chess board.
        
        moves = {'playerWhite': 0, 'playerBlack': 0}
        
    elif answer == 'yes':
        try:
            print()
            print(os.listdir(chessDir))
            chessFile = input('\nWhich of these games would you like to load? Input MUST match a file name EXACTLY: ')
            
            print('Loading chess board from file...\n')
            with open(os.path.join(chessDir, chessFile), 'r') as file:
                chessDicts = json.load(file)
            
            for k, v in chessDicts['Spaces'].items():
                board[k] = v
            
            for k, v in chessDicts['Moves'].items():
                moves[k] = v
                
            time.sleep(1)
        except FileNotFoundError:
            print('A file for the given name was not found.\n')
            sys.exit(1)
        
    return board, moves
    
    
def saveBoard(board, moves, player1, player2):
    # Set the path to look for saved chess games.
    userHome = os.path.expanduser('~')
    chessDir = os.path.abspath(os.path.join(userHome, 'chess-games'))
    today = datetime.datetime.now()
    formatTime = today.strftime("%m-%d-%y")
    fileName = '{}-{}-chess-{}.json'.format(player1.lower(), player2.lower(), formatTime)
    
    
    print('Saving chess game to file...\n')
    time.sleep(1)

    jsonData = json.dumps(board, indent=4)
    with open(os.path.join(chessDir, fileName), 'w') as file:
        file.write(jsonData)
    
    print('Chess game saved in {} as {}'.format(chessDir, fileName))
    
    
def printBoard(board):
    # Create a list of dictionaries for each row of chess board spaces.
    listOfSpaces = [
        {   '1a': board['1a'], '1b': board['1b'], '1c': board['1c'], '1d': board['1d'],
            '1e': board['1e'], '1f': board['1f'], '1g': board['1g'], '1h': board['1h']},
        {   '2a': board['2a'], '2b': board['2b'], '2c': board['2c'], '2d': board['2d'],
            '2e': board['2e'], '2f': board['2f'], '2g': board['2g'], '2h': board['2h']},
        {   '3a': board['3a'], '3b': board['3b'], '3c': board['3c'], '3d': board['3d'],
            '3e': board['3e'], '3f': board['3f'], '3g': board['3g'], '3h': board['3h']},
        {   '4a': board['4a'], '4b': board['4b'], '4c': board['4c'], '4d': board['4d'],
            '4e': board['4e'], '4f': board['4f'], '4g': board['4g'], '4h': board['4h']},
        {   '5a': board['5a'], '5b': board['5b'], '5c': board['5c'], '5d': board['5d'],
            '5e': board['5e'], '5f': board['5f'], '5g': board['5g'], '5h': board['5h']},
        {   '6a': board['6a'], '6b': board['6b'], '6c': board['6c'], '6d': board['6d'],
            '6e': board['6e'], '6f': board['6f'], '6g': board['6g'], '6h': board['6h']},
        {   '7a': board['7a'], '7b': board['7b'], '7c': board['7c'], '7d': board['7d'],
            '7e': board['7e'], '7f': board['7f'], '7g': board['7g'], '7h': board['7h']},
        {   '8a': board['8a'], '8b': board['8b'], '8c': board['8c'], '8d': board['8d'],
            '8e': board['8e'], '8f': board['8f'], '8g': board['8g'], '8h': board['8h']}       
    ]
    
    # Print the column headers for the chess board.
    print('  | A  | B  | C  | D  | E  | F  | G  | H  |')
    print('-' * 43)
    
    # Loop through the list and each dictionary to print the piece that occupies the space
    # or blank if there is no piece present in the space.
    for dict in listOfSpaces:
        print('{} | '.format(int((listOfSpaces.index(dict))) + 1), end='')      # Print the row headers.
        for k, v in dict.items():
            print('{} | '.format(v), end='')
        print('\n' + ('-' * 43))
    print()
    
    
def main():
    
    # Clear the screen and get player names for while/black.
    os.system('cls' if os.name == 'nt' else 'clear')
    playerWhite = input('Enter a player name for White: ')
    time.sleep(0.5)
    playerBlack = input('Enter a player name for Black: ')
    time.sleep(0.5)
    print('Player 1: {}'.format(playerWhite))
    print('Player 2: {}'.format(playerBlack))
    
    chessBoard, playerMoves = loadBoard()
    
    printBoard(chessBoard)
    
    saveBoard(chessBoard, playerMoves, playerWhite, playerBlack)
    
    
if __name__ == "__main__":
    main()
