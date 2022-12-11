#initial imports
import random
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
                    #check if the ships overlaps
                    if ship_overlaps(board, row, column, orientation, ship_length) == False:
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + ship_length):
                                board[i][column] = "X"
                        break
            else:
                place_ship = True
                print('Place the ship with a length of ' + str(ship_length))
                row, column, orientation = user_input(place_ship)
                if check_ship_fit(ship_length, row, column, orientation):
                    #check if the ships overlaps
                        if ship_overlaps(board, row, column, orientation, ship_length) == False:
                            if orientation == "H":
                                for i in range(column, column + ship_length):
                                    board[row][i] = "X"
                            else:
                                for i in range(row, row + ship_length):
                                    board[i][column] = "X"
                            print_board(PLAYER_BOARD)
                            break 

#function to check if ship fits
def check_ship_fit(SHIP_LENGTH, row, column, orientation):
    if orientation == "H":
        if column + SHIP_LENGTH > 8:
            return False
        else:
            return True
    else:
        if row + SHIP_LENGTH > 8:
            return False
        else: 
            return True

#function to check if ships overlaps
def ship_overlaps(board, row, column, orientation, ship_length):
    if orientation == "H":
        for i in range(column, column + ship_length):
            if board[row][i] == "X":
                return True
    else:
        for i in range(row, row + ship_length):
            if board[i][column] == "X":
                return True
    return False

#function to check the users input
def user_input(place_ship):
    if place_ship == True:
        while True:
            try: 
                orientation = input("Enter orientation (H or V): ").upper()
                if orientation == "H" or orientation == "V":
                    break
            except TypeError:
                print('Enter a valid orientation H or V')
        while True:
            try: 
                row = input("Enter the row 1-8 of the ship: ")
                if row in '12345678':
                    row = int(row) - 1
                    break
            except ValueError:
                print('Enter a valid letter between 1-8')
        while True:
            try: 
                column = input("Enter the column of the ship: ").upper()
                if column in 'ABCDEFGH':
                    column = letters_to_numbers[column]
                    break
            except KeyError:
                print('Enter a valid letter between A-H')
        return row, column, orientation 
    else:
        while True:
            try: 
                row = input("Enter the row 1-8 of the ship: ")
                if row in '12345678':
                    row = int(row) - 1
                    break
            except ValueError:
                print('Enter a valid letter between 1-8')
        while True:
            try: 
                column = input("Enter the column of the ship: ").upper()
                if column in 'ABCDEFGH':
                    column = letters_to_numbers[column]
                    break
            except KeyError:
                print('Enter a valid letter between A-H')
        return row, column 

#function to check if ships took a hit
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

#function for the user and computers turn
def turn(board):
    if board == PLAYER_GUESS_BOARD:
        row, column = user_input(PLAYER_GUESS_BOARD)
        if board[row][column] == "-":
            turn(board)
        elif board[row][column] == "X":
            turn(board)
        elif COMPUTER_BOARD[row][column] == "X":
            board[row][column] = "X"
        else:
            board[row][column] = "-"
    else:
        row, column = random.randint(0,7), random.randint(0,7)
        if board[row][column] == "-":
            turn(board)
        elif board[row][column] == "X":
            turn(board)
        elif PLAYER_BOARD[row][column] == "X":
            board[row][column] = "X"
        else:
            board[row][column] = "-"


#Calling the functions
place_ships(COMPUTER_BOARD)
print_board(COMPUTER_BOARD)
print_board(PLAYER_BOARD)
place_ships(PLAYER_BOARD)

#While loop for the player and computer turns
while True:
    while True:
        print('Guess a battleship location')
        print_board(PLAYER_GUESS_BOARD)
        turn(PLAYER_GUESS_BOARD)
        break
    if count_hit_ships(PLAYER_GUESS_BOARD) == 17:
        print("you Win!")
        break
    while True:
        turn(COMPUTER_GUESS_BOARD)
        break
    print_board(PLAYER_GUESS_BOARD)
    if count_hit_ships(COMPUTER_GUESS_BOARD) == 17:
        print("Sorry, the computer won.")
        break