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
    pass

#Function for getting the ships location
def get_ship_location():
    pass

#Function to count the hits a ship receives
def count_hit_ships():
    pass

#The start of the game
create_ships()
turns = 10
while turns > 0:

