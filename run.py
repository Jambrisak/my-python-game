#initial imports
import random
from random import randint

#The different boards
#Hidden board will hold the ships
#Guess board will hold hits or misses
the_players_board = [[" "] * 8 for x in range(8)]
the_computers_board = [[" "] * 8 for i in range(8)]
the_players_guesses = [[" "] * 8 for x in range(8)]
the_computers_guesses = [[" "] * 8 for x in range(8)]

#The length of the ships
the_different_ships = [2,3,3,4,5]
#A way to convert letters to numbers
convert_Letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

#Function to print the boards
def print_the_game_board(board):
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

#function to place the ships
def placements_of_the_ships(board):
    for ship_length in the_different_ships:
        while True:
            if board == the_computers_board:
                orientation, row, column = random.choice(["H", "V"]), random.randint(0,7), random.randint(0,7)
                if does_ship_fit(ship_length, row, column, orientation):
                    #check if the ships overlaps
                    if does_the_ship_overlap(board, row, column, orientation, ship_length) == False:
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
                row, column, orientation = the_players_input(place_ship)
                if does_ship_fit(ship_length, row, column, orientation):
                    #check if the ships overlaps
                        if does_the_ship_overlap(board, row, column, orientation, ship_length) == False:
                            if orientation == "H":
                                for i in range(column, column + ship_length):
                                    board[row][i] = "X"
                            else:
                                for i in range(row, row + ship_length):
                                    board[i][column] = "X"
                            print_the_game_board(the_players_board)
                            break 

#function to check if ship fits
def does_ship_fit(SHIP_LENGTH, row, column, orientation):
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
def does_the_ship_overlap(board, row, column, orientation, ship_length):
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
def the_players_input(place_ship):
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
                    column = convert_Letters_to_numbers[column]
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
                    column = convert_Letters_to_numbers[column]
                    break
            except KeyError:
                print('Enter a valid letter between A-H')
        return row, column 

#function to check if ships took a hit
def how_many_hits_on_ship(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

#function for the user and computers turn
def game_turn(board):
    if board == the_players_guesses:
        row, column = the_players_input(the_players_guesses)
        if board[row][column] == "-":
            game_turn(board)
        elif board[row][column] == "X":
            game_turn(board)
        elif the_computers_board[row][column] == "X":
            board[row][column] = "X"
        else:
            board[row][column] = "-"
    else:
        row, column = random.randint(0,7), random.randint(0,7)
        if board[row][column] == "-":
            game_turn(board)
        elif board[row][column] == "X":
            game_turn(board)
        elif the_players_board[row][column] == "X":
            board[row][column] = "X"
        else:
            board[row][column] = "-"


#Calling the functions
placements_of_the_ships(the_computers_board)
print_the_game_board(the_computers_board)
print_the_game_board(the_players_board)
placements_of_the_ships(the_players_board)

#While loop for the player and computer turns
while True:
    while True:
        print('Guess a battleship location')
        print_the_game_board(the_players_guesses)
        game_turn(the_players_guesses)
        break
    if how_many_hits_on_ship(the_players_guesses) == 17:
        print("you Win!")
        break
    while True:
        game_turn(the_computers_guesses)
        break
    print_the_game_board(the_players_guesses)
    if how_many_hits_on_ship(the_computers_guesses) == 17:
        print("Sorry, the computer won.")
        break