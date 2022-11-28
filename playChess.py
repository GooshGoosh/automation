#!/usr/bin/env python3

''' playChess.py - A program that takes a chess board (pieces and spaces) and writes them to a file. The file will be a json file and will be named after both players
followed by the date (mm-dd-yy) that the file was saved. The two player are given the option to either start a new game or load a game that was previously saved.
If the players decide to load from a previously saved game, they will be given a list of files in the 'chess-games' directory in the user home directory that will
allow them to type in the file that they would like to load. If the 'chess-games' directory is not found within the user's home directory, the directory will be
created.

The players will take turns and on each turn they will be given two options: move a piece on a specified space or save and exit the game. If the player chooses to move
a piece on a specified space, they will then be given a prompt to select a space (piece) that they would like to move and then to choose a space that they would
like to move their piece to. Players will have to select the space that they would like to interact with that contains the piece that they would like to move.
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


def load_board():
    # Set the path to look for saved chess games.
    userHome = os.path.expanduser('~')
    chessDir = os.path.abspath(os.path.join(userHome, 'chess-games'))
    board = {}
    moves = {}
    removedFromPlay = {}
    
    # Check if the chess directory already exists and, if not, create it.
    if not os.path.isdir(chessDir):
        os.makedirs(chessDir)
    
    # Check if the players have a saved game file.
    time.sleep(0.5)
    if len(os.listdir(chessDir)) == 0:
        answer = 'no'
        print('No saved games found.')
        time.sleep(0.25)
    else:
        answer = ''
        
    while answer.lower() != 'yes' and answer.lower() != 'no':
        answer = input('Do you have a saved game that you would like to load? (yes/no) > ')
    
    if answer == 'no':
        print('Loading default chess board...\n')
        time.sleep(1)
        
        board = {
            'a1': 'wr', 'b1': 'wk', 'c1': 'wb', 'd1': 'WK', 'e1': 'wq', 'f1': 'wb', 'g1': 'wk', 'h1': 'wr',
            'a2': 'wp', 'b2': 'wp', 'c2': 'wp', 'd2': 'wp', 'e2': 'wp', 'f2': 'wp', 'g2': 'wp', 'h2': 'wp',
            'a3': '  ', 'b3': '  ', 'c3': '  ', 'd3': '  ', 'e3': '  ', 'f3': '  ', 'g3': '  ', 'h3': '  ',
            'a4': '  ', 'b4': '  ', 'c4': '  ', 'd4': '  ', 'e4': '  ', 'f4': '  ', 'g4': '  ', 'h4': '  ',
            'a5': '  ', 'b5': '  ', 'c5': '  ', 'd5': '  ', 'e5': '  ', 'f5': '  ', 'g5': '  ', 'h5': '  ',
            'a6': '  ', 'b6': '  ', 'c6': '  ', 'd6': '  ', 'e6': '  ', 'f6': '  ', 'g6': '  ', 'h6': '  ',
            'a7': 'bp', 'b7': 'bp', 'c7': 'bp', 'd7': 'bp', 'e7': 'bp', 'f7': 'bp', 'g7': 'bp', 'h7': 'bp',
            'a8': 'br', 'b8': 'bk', 'c8': 'bb', 'd8': 'BK', 'e8': 'bq', 'f8': 'bb', 'g8': 'bk', 'h8': 'br'
        }   # Dictionary for a new, freshly set up chess board.
        
        moves = {'playerWhite': 0, 'playerBlack': 0}
        
        removedFromPlay = {'removedWhite': [], 'removedBlack': []}
        
    elif answer == 'yes':
        try:
            print()
            # Output a list of saved games in the chess directory.
            chessFile = pyip.inputMenu(os.listdir(chessDir), numbered=True, prompt="Which of these games would you like to load? Type in the number that corresponds to your saved game: \n", blank=True)
            
            print('Loading chess board from file...\n')
            with open(os.path.join(chessDir, chessFile), 'r') as file:
                chessDicts = json.load(file)
            
            for k, v in chessDicts[0].items():
                board[k] = v
            
            for k, v in chessDicts[1].items():
                moves[k] = v
                
            for k, v in chessDicts[2].items():
                removedFromPlay[k] = v
                
            time.sleep(1)
        except FileNotFoundError:
            print('A file for the given name was not found.\n')
            sys.exit(1)
        
    return board, moves, removedFromPlay
    
    
def save_board(board, moves, removedPieces, player1, player2):
    # Set the path to look for saved chess games.
    userHome = os.path.expanduser('~')
    chessDir = os.path.abspath(os.path.join(userHome, 'chess-games'))
    today = datetime.datetime.now()
    formatTime = today.strftime("%m-%d-%y")
    fileName = '{}-{}-chess-{}.json'.format(player1.lower(), player2.lower(), formatTime)
    dictsToJSON = [board, moves, removedPieces]
    
    
    print('Saving chess game to file...\n')
    time.sleep(1)

    jsonData = json.dumps(dictsToJSON, indent=4)
    with open(os.path.join(chessDir, fileName), 'w') as file:
        file.write(jsonData)
    
    print('Chess game saved in {} as {}'.format(chessDir, fileName))
    
    
def print_board(board, removedPieces, player1, player2):
    rowNum = 8
    os.system('cls' if os.name == 'nt' else 'clear')
    print('White: {}'.format(player1))
    print('Black: {}'.format(player2))
    print('\n')
    
    # Create a list of dictionaries for each row of chess board spaces.
    listOfSpaces = [
        {   'a8': board['a8'], 'b8': board['b8'], 'c8': board['c8'], 'd8': board['d8'],
            'e8': board['e8'], 'f8': board['f8'], 'g8': board['g8'], 'h8': board['h8']},
        {   'a7': board['a7'], 'b7': board['b7'], 'c7': board['c7'], 'd7': board['d7'],
            'e7': board['e7'], 'f7': board['f7'], 'g7': board['g7'], 'h7': board['h7']},
        {   'a6': board['a6'], 'b6': board['b6'], 'c6': board['c6'], 'd6': board['d6'],
            'e6': board['e6'], 'f6': board['f6'], 'g6': board['g6'], 'h6': board['h6']},
        {   'a5': board['a5'], 'b5': board['b5'], 'c5': board['c5'], 'd5': board['d5'],
            'e5': board['e5'], 'f5': board['f5'], 'g5': board['g5'], 'h5': board['h5']},
        {   'a4': board['a4'], 'b4': board['b4'], 'c4': board['c4'], 'd4': board['d4'],
            'e4': board['e4'], 'f4': board['f4'], 'g4': board['g4'], 'h4': board['h4']}, 
        {   'a3': board['a3'], 'b3': board['b3'], 'c3': board['c3'], 'd3': board['d3'],
            'e3': board['e3'], 'f3': board['f3'], 'g3': board['g3'], 'h3': board['h3']}, 
        {   'a2': board['a2'], 'b2': board['b2'], 'c2': board['c2'], 'd2': board['d2'],
            'e2': board['e2'], 'f2': board['f2'], 'g2': board['g2'], 'h2': board['h2']},
        {   'a1': board['a1'], 'b1': board['b1'], 'c1': board['c1'], 'd1': board['d1'],
            'e1': board['e1'], 'f1': board['f1'], 'g1': board['g1'], 'h1': board['h1']}     
    ]
    
    # Print the column headers for the chess board.
    print('  | A  | B  | C  | D  | E  | F  | G  | H  |')
    print('-' * 43)
    
    # Loop through the list and each dictionary to print the piece that occupies the space
    # or blank if there is no piece present in the space.
    for dict in listOfSpaces:
        print('{} | '.format(rowNum), end='')      # Print the row headers.
        rowNum -= 1
        for k, v in dict.items():
            print('{} | '.format(v), end='')
        print('\n' + ('-' * 43))
    print()
    
    print('White pieces removed from play: {}'.format(', '.join(removedPieces['removedWhite'])))
    print('Black pieces removed from play: {}'.format(', '.join(removedPieces['removedBlack'])))
    print()
        
    
def chess_turns(chessBoard, playerMoves, removedPieces, playerWhite, playerBlack):
    whiteFinalRankSpaces = ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8']
    blackFinalRankSpaces = ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']
    pieceMoved = ''
    
    while True:
        if playerMoves['playerWhite'] == playerMoves['playerBlack']:
            time.sleep(0.75)
            print_board(chessBoard, removedPieces, playerWhite, playerBlack)
            print('{}\'s turn...\n'.format(playerWhite))
            startingSpace = ''
            destinationSpace = ''
            move = pyip.inputMenu(['Move Piece', 'Save and Exit'], numbered=True)
            
            if move == 'Move Piece':
                while startingSpace not in chessBoard.keys():
                    startingSpace = pyip.inputStr(prompt='\nType the space that the piece you would like to move resides in (e.g. a2) > ')
                    pieceMoved = chessBoard[startingSpace]
                while destinationSpace not in chessBoard.keys() and destinationSpace != startingSpace:
                    destinationSpace = pyip.inputStr(prompt='\nType the space that you would like to move the piece to (e.g. a3) > ')
                if chessBoard[destinationSpace] != '  ':
                    removedPieces['removedBlack'].append(chessBoard[destinationSpace])
                chessBoard[destinationSpace] = chessBoard[startingSpace]
                chessBoard[startingSpace] = '  '
                
                if pieceMoved == 'wp' and destinationSpace in whiteFinalRankSpaces:                 # Check if a white pawn has reached its final rank and is due for a promotion.
                    print('\nYour pawn is due for a promotion!')
                    time.sleep(0.75)
                    chessBoard = pawn_promotion(chessBoard, destinationSpace, player='white')       # Call the function to promote a pawn.
                    removedPieces['removedWhite'].append(pieceMoved)                                # Add a pawn to the removed pieces list for white pieces.
                    
                playerMoves['playerWhite'] += 1
            elif move == 'Save and Exit':
                save_board(chessBoard, playerMoves, removedPieces, playerWhite, playerBlack)
                sys.exit(0)
        elif playerMoves['playerWhite'] > playerMoves['playerBlack']:
            time.sleep(0.75)
            print_board(chessBoard, removedPieces, playerWhite, playerBlack)
            print('{}\'s turn...\n'.format(playerBlack))
            startingSpace = ''
            destinationSpace = ''
            move = pyip.inputMenu(['Move Piece', 'Save and Exit'], numbered=True)
            
            if move == 'Move Piece':
                while startingSpace not in chessBoard.keys():
                    startingSpace = pyip.inputStr(prompt='\nType the space that the piece you would like to move resides in (e.g. a7) > ')
                    pieceMoved = chessBoard[startingSpace]
                while destinationSpace not in chessBoard.keys() and destinationSpace != startingSpace:
                    destinationSpace = pyip.inputStr(prompt='\nType the space that you would like to move the piece to (e.g. a6) > ')
                if chessBoard[destinationSpace] != '  ':
                    removedPieces['removedWhite'].append(chessBoard[destinationSpace])
                chessBoard[destinationSpace] = chessBoard[startingSpace]
                chessBoard[startingSpace] = '  '
                
                if pieceMoved == 'bp' and destinationSpace in blackFinalRankSpaces:                 # Check if a black pawn has reached its final rank and is due for a promotion.
                    print('\nYour pawn is due for a promotion!')
                    time.sleep(0.75)
                    chessBoard = pawn_promotion(chessBoard, destinationSpace, player='black')       # Call the function to promote a pawn.
                    removedPieces['removedBlack'].append(pieceMoved)                                # Add a pawn to the removed pieces list for black pieces.
                    
                playerMoves['playerBlack'] += 1
            elif move == 'Save and Exit':
                save_board(chessBoard, playerMoves, removedPieces, playerWhite, playerBlack)
                sys.exit(0)
        else:
            print('\nERROR: Black has more moves taken than White! Exiting program with an error!')
            sys.exit(1)
 
 
def pawn_promotion(chessBoard, pawnSpace, player):
    if player == 'white':
        promotion = pyip.inputMenu(['wq', 'wk', 'wb', 'wr'], numbered=True, prompt='\nWhat would you like to promote your pawn to?\n')      # Ask player what to promote their pawn to.
        chessBoard[pawnSpace] = promotion                                                                                                   # Promote pawn to new piece.
    else:
        promotion = pyip.inputMenu(['bq', 'bk', 'bb', 'br'], numbered=True, prompt='\nWhat would you like to promote your pawn to?\n')      # Ask player what to promote their pawn to.
        chessBoard[pawnSpace] = promotion                                                                                                   # Promote pawn to new piece.
    
    return chessBoard
    
                
    
def main():
    
    # Clear the screen and get player names for white/black.
    os.system('cls' if os.name == 'nt' else 'clear')
    playerWhite = input('Enter a player name for White: ')
    time.sleep(0.5)
    playerBlack = input('Enter a player name for Black: ')
    time.sleep(0.5)
    print('Player 1: {}'.format(playerWhite))
    print('Player 2: {}'.format(playerBlack))
    
    chessBoard, playerMoves, removedPieces = load_board()
    chess_turns(chessBoard, playerMoves, removedPieces, playerWhite, playerBlack)
    
    
if __name__ == "__main__":
    main()
