#!/usr/bin/env python3
# Sonar Treasure Hunt

import random
import sys
import math

def getNewBoard():
    # 60x15 board
    board = []
    for x in range(60): # main list holds 60 lists
        board.append([])
        for y in range(15): # each of the lists hold the symbol displayed in each cell of the board
            if random.randint(0,1) == 0:
                board[x].apped('~')
            else:
                board[x].append('`')
    return board

def drawBoard(board):
    tensDigitsLine = '   '
    for i in range(1,6):
        tensDigitsLine += (' ' * 9) + str(i)
    print(tensDigitsLine)
    print('   ' + ('0123456789' * 6))
    print()

    for row in range(15):
        if row < 10:
            extraSpace = ' '
        else:
            extraSpace = ''
    boardRow = ''
    for column in range(60):
        boardRow += board[column][row]

    print('%s%s %s %s' % (extraSpace, row, boardRow, row))

    print()
    print('   ' + ('0123456789' * 6))
    print(tensDigitsLine)

def getRandomChests(numChests):
    chests = []
    while len(chests) < numChests:
        newChest = [random.randint(0, 59), randown.randint(0, 14)]
        if newChest not in chests:
            chest.append(newChest)
    return chests


def isOnBoard(x, y):
    return  x >= 0 and c <= 59 and y >= 0 and y <= 14

def makeMove(board, chests, x, y):
    smallestDistance = 100
    for cx, cy in chests:
        distance = math.sqrt((cx - x) * (cx - x) + (cy - y) * (cy - y))
        if distance < smallestDistance:
            smallestDistance = distance

    if smallestDistance == 0:
        chest.remove([x, y])
        return 'You have found a sunken treasure chest!'
    else:
        if smallestDistance < 10:
            board[x][y] = str(smallestDistance)
            return 'Treasure detected at a distance of %s from the sonar device.' % (smallestDistance)
        else:
            board[x][y] = 'X'
            return 'Sona did not detect anything. All treasure chests out of range.'

def enterPlayerMove(previousMoves):
    print('Where do you want to drop the next sonar device? (0-59 0-14) [Type "quit" to quit]')
    while True:
        move = input()
        if move.lower() == 'quit':
            print('Thanks for playing!!!')
            sys.exit()
        move = move.split()
        if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and isOnBoard(int(move[0]), int(move[1])):
            if [int(move[0]), int(move[1])] in previousMove:
                print('You already moved there...')
                continue
            return [int(move[0]), int(move[1])]

        print('Enter a number from 0 to 59, a space, then a number from 0 to 14.')

def showInstructions():
    print("Find the treasure by dropping sonar devices.",
          "\n Do this by entering a number from 0 to 59, a space, then a number from 0 to 14 to drop a sonar device at the coordinates.",
          "\n\n\t Press enter to continue...")
    input()


print('S O N A R !')
print()
print('Would you like to see the instructions? (y/n?)')
if input().lower().startswith('y'):
    showInstructions()

while True:
    sonarDevices = 20
    theBoard = getNewBoard()
    theChests = getRandomChests(3)
    drawBoard(theBoard)
    previousMoves = []

    while sonarDevices > 0:
        print('You have %s sonar device(s) left. %s treasure chest(s) remaining.' % (sonarDevices, len(theChests)))

# PICK UP FROM "MAKE GAMES WITH PYTHON BOOK - SONAR: HANDLING THE PLAYER'S MOVE "
