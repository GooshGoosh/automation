#!/usr/bin/env python3

''' playChess.py - A program that takes a chess board (pieces and spaces) and writes them to a file. The file will be a json file and will be named after both players
followed by the date (mm-dd-yy) that the file was saved. The two player are given the option to either start a new game or load a game that was previously saved.
If the players decide to load from a previously saved game, they will be given a list of files in the 'chess-games' directory in the user home directory that will
allow them to type in the file that they would like to load. If the 'chess-games' directory is not found within the user's home directory, the directory will be
created.

The players will take turns and on each turn they will be given two options: move a piece on a specified space or save and exit the game. If the player chooses to move
a piece on a specified space, they will then be given the option to cancel the move and be brought back to the previous options or to choose a space that they would
like to move their piece. Players will have to select the space that they would like to interact with that contains the piece that they would like to move.
e.g. if the white queen is on space h3, the player would type in 'h3' and then type in the space that they would like to move it to such as 'h6'.
If the player chooses the option to save and quit, the program will save the current board configuration and number of moves for each player to a json file.
The current configuration of the chess board will be printed out to the screen after each player's turn.

WARNING: This program assumes that the player's know how to play chess and intend to play it fairly without exploiting the program. This program does not check if
any moves made by either player are legal or if the correct player is moving their intended piece (i.e. the black player moving the white pieces). The program only
ensures that the players interact with legal spaces on the chess board and do not try to move pieces to and from invalid board spaces such as z7 or r23.
'''

import json
import os
import time
import sys
import datetime
import pyinputplus as pyip


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
            
            for k, v in chessDicts[0].items():
                board[k] = v
            
            for k, v in chessDicts[1].items():
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
    dictsToJSON = [board, moves]
    
    
    print('Saving chess game to file...\n')
    time.sleep(1)

    jsonData = json.dumps(dictsToJSON, indent=4)
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
    
    
def 
    
    
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
