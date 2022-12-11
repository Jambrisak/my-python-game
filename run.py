#Legend of what things are going to be
#X for placing the ships and hit battleship
# ' ' available for space
# '-' for missed shot

#initial imports
from random import randint

#The different boards
#Hidden board will hold the ships
#Guess board will hold hits or misses
HIDDEN_BOARD = [[' '] * 8 for x in range(8)]
GUESS_BOARD = [[' '] * 8 for x in range(8)]

#A way to convert letters to numbers
letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

#Function to print the boards
def print_board(board):
    print('     A B C D E F G H')
    print('     ---------------')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

#Function to create ships
def create_ships():
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0,7), randint(0,7)
        board[ship_row][ship_column] = 'X'

#Function for getting the ships location
def get_ship_location():
    row = input('Please enter a ship row 1-8')
    while row not in '12345678':
        print('Please enter a valid row')
        row = input('Please enter a ship row 1-8')
    column = input('Please enter a ship column A-H').upper()
    while column not in 'ABCDEFGH':
        print('Please enter a valid column')
        column = input('Please enter a ship column A-H').upper()
    return int(row) - 1, letters_to_numbers[column]

#Function to count the hits a ship receives
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count

#The start of the game
create_ships()
turns = 10
#while turns > 0:

