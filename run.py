
from random import randint
from unicodedata import name # Import random function so that positions on board 
# can be randomised.
# 
scores = {"computer":0, "player":0}

class Board:
    """
    Board class sets board size, number of ships, player's name 
    and the board type: player or computer
    """

    def __init__(self, size, num_ships, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print(self):
        for row in self.board:
            print(" ".join(row))

    def guess(self, x, y):
        self.guesses.append((x,y))
        self.board[x][y] = "X"

        if (x,y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"

    def add_ship(self, x, y, type = "computer"):
        if len(self.ships) >= self.num_ships:
            print("Error: you cannot add any more ships!")
        else:
            self.ships.append((x,y))
            if self.type == "player":
                self.board[x][y] = "@"

def random_point(size):
    """
    function to return random integer between 0 and size
    """
    return randint(0, size - 1)

def valid_coordinates(x, y, size):
    """
    Verifies guess co-ordinates entered by player
    """
    return ((0 <= x < size) and (0 <= y < size))
    

def populate_board(board):
    return True #to get code to work



def make_guess():
    """
    Get x and y guess co-ordinates from player
    """
    while True:
        try:
            print("=" * 58)
            x = int(input(f"Enter row in range 0 - {size - 1}: \n"))
            y = int(input(f"Enter column in range 0 - {size - 1}: \n"))
            break
        except ValueError:
            print("Error, Row and Column must be valid numbers\n")
    return(x, y)
    

   



def play_game(computer_board, Player_board):
    return True #to get code to work


def new_game():
    """
    Starts a new game, set board size, number of ships,
    resets scores and initialises boards.
    """
    size = 5
    num_ships = 4
    scores["computer"] = 0
    scores["player"] = 0
    print("-" * 35)
    print(" Welcome to ULIIMATE BATTLESHIPS!!")
    print(f" Board Size: {size}. Number of ships: {num_ships}")
    print("Top left corner is row: 0, col: 0")
    print("-" * 35)
    player_name = input("Please enter your name:\n")
    print("-" * 35)

    computer_board = Board(size, num_ships, "Computer", type = "computer")
    Player_board = Board(size, num_ships, player_name, type = "player")

    for _ in range(num_ships):
        populate_board(player_board)
        populate_board(computer_board)

    play_game(computer_board, Player_board)

#new_game()
size = 5
x, y = make_guess()
if valid_coordinates(x, y, size):
    print("co-ordinitates are within range")



