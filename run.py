import random
# Import random function so that positions on board 
# can be randomised.
# 
ALPHA_NUMERO = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7
}
ONE_TO_EIGHT = ("1", "2", "3", "4", "5", "6", "7", "8")
board_size = 8
PLAYER_BOARD = [[" "]*8 for _ in range(board_size)]
PLAYER_BOARD_GUESS = [[" "]*8 for _ in range(board_size)]
COMPUTER_BOARD = [[" "]*8 for _ in range(board_size)]
COMPUTER_BOARD_GUESS = [[" "]*8 for _ in range(board_size)]
SHIPS = [2,3,3,4,5]

  

def show_board(board):
    """
    Makes and shows board for player to see progress
    """

    if board == PLAYER_BOARD or board == PLAYER_BOARD_GUESS or board == COMPUTER_BOARD:
        print("  A B C D E F G H")
        print("  - - - - - - - -")
        row_number = 1
        for row in board:
            print("%d|%s" % (row_number,f"|".join(row)))
            row_number +=1

def place_ships(board):
    """
    Places ships on board
    """
    for ship in SHIPS:
        while True:
            if board == COMPUTER_BOARD:
                direction = random.choice(["H", "V"])
                row = random.randint(0, board_size-1)
                col = random.randint(0, board_size-1)
                if make_sure_ship_fits(board, ship, direction, row, col):
                    if not no_ship_overlap(board, ship, direction, row, col):
                        print(direction, row, col)
                        if direction == "H":
                            for i in range(col, col + ship):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + ship):
                                board[i][col] = "X"
                        break
            else:
                print(f"Place your ship size: {ship} on grid")
                get_players_ship_position()
                
                break
            

def make_sure_ship_fits(board, ship, direction, row, col):
    """
    Checks ship co-ordinates doesn't exceed boudaries of board
    """
    if board == COMPUTER_BOARD:
        if direction == "H":
            if col + ship > board_size:
                return False
            else:
                return True
        else:
            if row + ship > board_size:
                return False
            else:
                return True

def no_ship_overlap(board, ship, direction, row, col):
    """
    Checks this ship doesn't overlap previous ships placed
    """
    if board == COMPUTER_BOARD:
        if direction == "H":
            for i in range(col, col + ship):
                if board[row][i] == "X":
                    return True
        else:
            for i in range(row, row + ship):
                if board[i][col] == "X":
                    return True
        return False
    else:
        print("player board overlap check")

        return False

def get_players_ship_position():
    while True:
        try:
            direction = input("What direction would you like to position your ship, (H) horizontal (V) Vertical\n").upper()
            while direction not in ("H", "V"):
                print("Incorrect choice, only H or V")
                break
            if direction =="H" or direction == "V":
                break
        except ValueError:
            print("Wrong nput Try 'H' or 'V'\n")
    while True:
        try:
            row = input(("Enter row you would like to place ship (1-8) \n"))
            while row not in ONE_TO_EIGHT:
                print("Wrong input, select a number between 1 and 8\n")
                break
            if row in ONE_TO_EIGHT:
                row = int(row) - 1
                break
        except ValueError:
            print("Wrong input, select a number between 1 and 8\n ")

    while True:
        try:
            col = input("Enter column you would like to place ship (A to H").upper()
            while col not in ALPHA_NUMERO.keys():
                print("Wrong input, enter A to H\n")
                break
            if col in ALPHA_NUMERO.keys():
                col = ALPHA_NUMERO[col]
                break
        except ValueError:
            print("Wrong input, enter letter between A and H\n")
    return row, col




    




scores = {"computer":0, "player":0}

class Board:
    """
    Board class sets board size, number of ships, player's name 
    and the board type: player or computer
    """

    def __init__(self, size, num_ships, name, type):
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

    def add_ship(self, x, y):
        if len(self.ships) >= self.num_ships:
            print("Error: you cannot add any more ships!")
        else:
            self.ships.append((x,y))
            if self.type == "player":
                self.board[x][y] = "@"
    
    def populate_board(size):
        """
        Position ships on grid in random positions
        """
    
        x, y = rand_coordinates(size)
        while (x, y) in self.ships:
            x, y = rand_coordinates(self.size)
        self.add_ship(x,y)


def random_point(size):
    """
    function to return random integer between 0 and size
    """

    return randint(0, size - 1)

def rand_coordinates(size):
    """
    creates two random numbers within the range 0 and board size
    """
    randomized = randint(0, size)
    print((randomized))
    return randint(0, size-1), randint(0, size-1)

def valid_coordinates(x, y, size):
    """
    Verifies guess co-ordinates entered by player
    """
    return ((0 <= x < size) and (0 <= y < size))
    


        




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
    

   


def welcome():
    """
    Display  instructions and information about game
    """
    print("="* 58)
    print(" WELCOME TO BATTLESHIP GAME\n")
    print(f"Board size: {size} X {size}.\n")
    print(f"Number of ships : {num_ships}.\n")
    print("="* 58)
    print("Instructions for Battleship")
    print("Player must guess co-ordinates of opponent's ships")
    print(f"Objective is to hit all of opponent's {num_ships} ships before opponent hits yours.")
    print(" Enter your guess as a row and colum number ")
    print("Top left is row : 0, column : 0\n")
    print("="* 58)
    print("@ = a ship on the battle grid\n")
    print("* = co-ordinates of a HIT")
    print("X = co-ordinates of a MISS")

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
    print("=" * 58)
    print(" Welcome to BATTLESHIPS!!")
    print(f" Board Size: {size}. Number of ships: {num_ships}")
    print(" Top left corner is row: 0, col: 0")
    print("=" * 58)
    print("=" * 24 + " Legend " + "=" * 24)
    player_name = input(" Please enter your name:\n")
    print("=" * 58)

    
    #computer_board = Board(size, num_ships, "Computer", type="computer")
    
    #player_board = Board(size, num_ships, player_name, type="player")

    board = COMPUTER_BOARD
    place_ships(board)
    board = PLAYER_BOARD
    place_ships(board)
    show_board(PLAYER_BOARD)
    show_board(COMPUTER_BOARD)


    for _ in range(num_ships):
        populate_board(player_board)
        populate_board(computer_board)
    
    computer_board.print()

    print("="* 58)
    
    Player_board.print()
    #play_game(computer_board, Player_board)
    
new_game()
size = 5
x, y = make_guess()
if valid_coordinates(x, y, size):
    print("co-ordinitates are within range")




