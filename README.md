# A Battleships Game
Portfolio Project 3 Python Essentials - Code Institute

# About
This game is of [battleships](http://battleship-game.net/), a well known game originally made on paper after WWI. This version differs from many others in that it is for one user against the computer with randomly generated battleship locations of one square. This game was made in haste and following a tutorial due to the creator having a time constraints because of the projects deadline and because of personal issues. It was made to showcase that the creator understand how to build a simple battleship game and to showcase a passable degree of knowledge for it. It was not intended to reach for a higher grade but only in the hope of achieving a passing grade so that the creator could take a well earned break from work / CI due to being put under (creators own chosen) stress.

# How To Play
The game will start by asking the user to place its ships on the board, and then the game will start. The user is the first one to start playing.
## Breakdown on starting procedure
The game will then request that the user enters a column and row number (essentially, co-ordinates) of the location they suspect a battleship is laid. If that location is on a battleship, it is a hit and marked as "#". If the location is not on a battleship, it is a miss and marked as "*". 
The computer and user will take ten turns to find all 4 of the ships, should all 10 turns be taken without finding 4 ships, the game will state who has had the most hits and display them as the winner. 

# Features
![image of battleships app](./README%20Assets/Starting%20Screen.png)

## Existing Features
- The user must press enter to continue to the next turn to allow them to properly see what is happening at each turn
- The game accepts user input for co-ordinates they wish to fire at
- The game is played against the computer

## Future Features
- Use the username throughout the game rather than just in the welcoming statement so that the user can be more personally celebrated or commiserated at the end of the game.
- The game keeps count of turns and displays this to the user
- Allow the user to choose to play against a other (local) player or the computer
- Allow the user to dictate the number of ships and the board size

# Testing
## Manual Testing
When i ran into this error message in the console.
    - [Running] python -u "c:\Users\jambr\OneDrive\Dokument\GitHub\my-python-game\run.py"
    - Traceback (most recent call last):
    - File "c:\Users\jambr\OneDrive\Dokument\GitHub\my-python-game\run.py", line 168, in <module>
    - place_ships(COMPUTER_BOARD)
    - File "c:\Users\jambr\OneDrive\Dokument\GitHub\my-python-game\run.py", line 36, in place_ships
    - orientation, row, column = random.choice(["H", "V"]), random.randint(0,7), random.randint(0,7)
    - NameError: name 'random' is not defined
I had to retrace my steps and find the faulty lines and then correct it

## Bugs/Updates after Testing
After depolying the game i found out that the some of the lines were faulty, due to naming mistakes and such so i had to rename and check my spelling. This caused a bug that would not start the game.

## Validator Testing
- Fully passed the [PEP8 online validator](http://pep8online.com/) with the result "All right"

# Deployment
This project was deployed using Code Institute's mock terminal for Heroku.

The steps for deployment are as follows:
- Fork or clone this repository
- Create a new Heroku app
- Set the buildpacks to Python and NodeJS in that order
- Link the Heroku app to the repository
- Click on Deploy

# Credits
- This project uses the [Code Institute student template](https://github.com/Code-Institute-Org/python-essentials-template) for deploying the third portfolio project, the Python command-line project.
- The idea of using battleships is a suggested one by the Code Institute with "Ultimate Battleships" as inspiration.
- Thank you to my friend, Jodie Clark, for providing user feedback: your points were invaluable.
- Brian Macharia for mentor support and finishing touches.