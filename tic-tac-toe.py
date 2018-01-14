# Tic-Tac-Toe

import random

def drawBoard(board):
    # This function prints out the board that it passed.

    # "board" is a list of 10 strings representing the board (ignore index 0).
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def inputPlayerLetter():
    # Lets the player type which letter they want to be.
    # Returns a list with the players letter as the first item and the computer's letter as the second.
    letter=''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

         # the first element in the list is the players letter; the second is the computers letter.
        if letter == 'X':
            return['X', 'O']
        else:
            return['O', 'X']

def whoGoesFirst():
    # Randomly choose  which player goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo,le):
    # Given a board and a players letter, this function returns True if that player has won.
    print(0)

def getPlayerMove(theBoard):
    print('TODO')
    return 1

def getComputerMove(theBoard, computerLetter):
    print('TODO')
    return 0

def main():
    print("Welcome to Tic-Tac-Toe!")
    while True:
        theBoard = [' '] * 10
        playerLetter, computerLetter = inputPlayerLetter()
        turn = whoGoesFirst()
        print('The ' + turn + ' will go first!')
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == 'player':
                # Player's turn
                drawBoard(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard,playerLetter,move)
            else:
                # Computer's turn
                move = getComputerMove(theBoard, computerLetter)
                makeMove(theBoard,computerLetter,move)

if __name__ == "__main__":
    main()