#Legend of what things are going to be
#X for placing the ships and hit battleship
# ' ' available for space
# '-' for missed shot

#initial imports
from random import randint

#The different boards
#Hidden board will hold the ships
#Guess board will hold hits or misses
PLAYER_BOARD = [[" "] * 8 for x in range(8)]
COMPUTER_BOARD = [[" "] * 8 for i in range(8)]
PLAYER_GUESS_BOARD = [[" "] * 8 for x in range(8)]
COMPUTER_GUESS_BOARD = [[" "] * 8 for x in range(8)]

#The length of the ships
LENGTH_OF_SHIPS = [2,3,3,4,5]
#A way to convert letters to numbers
letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

#Function to print the boards
def print_board(board):
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

#function to place the ships
def place_ships(board):
    for ship_length in LENGTH_OF_SHIPS:
        while True:
            if board == COMPUTER_BOARD:
                orientation, row, column = random.choice(["H", "V"]), random.randint(0,7), random.randint(0,7)
                if check_ship_fit(ship_length, row, column, orientation):

#function to check if ship fits
def check_ship_fit(SHIP_LENGTH, row, column, orientation):
    if orientation == "H":
        if column + SHIP_LENGTH > 8:
            return False
        else
            return True
    else:
        if row + SHIP_LENGTH > 8:
            return False
        else: 
            return True

#Function to create ships
def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"

#Function for getting the ships location
def get_ship_location():
    row = input("Enter the row of the ship: ").upper()
    while row not in "12345678":
        print('Not an appropriate choice, please select a valid row')
        row = input("Enter the row of the ship: ").upper()
    column = input("Enter the column of the ship: ").upper()
    while column not in "ABCDEFGH":
        print('Not an appropriate choice, please select a valid column')
        column = input("Enter the column of the ship: ").upper()
    return int(row) - 1, letters_to_numbers[column]

#Function to count the hits a ship receives
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

#The start of the game
create_ships(HIDDEN_BOARD)
turns = 10
while turns > 0:
    print('Welcome to Battleship')
    print_board(GUESS_BOARD)
    row, column = get_ship_location()
    if GUESS_BOARD[row][column] == '-':
        print('You have already guessed that')
    elif HIDDEN_BOARD[row][column] == 'X':
        print('Congratulations, you have hit the battleship')
        GUESS_BOARD[row][column] = 'X'
        turns -= 1
    else:
        print('Sorry, you missed')
        GUESS_BOARD[row][column] = '-'
        turns -= 1
    if count_hit_ships(GUESS_BOARD) == 5:
        print('Congratulations, you have sunk all the battleships')
        break
    print('You have ' + str(turns) + ' turns remaining')
    if turns == 0:
        print('Game Over')
        break