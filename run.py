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
BOARD_SIZE = 8
SHIPS = [2,3,3,4,5]
player_board = [[" "]*8 for _ in range(BOARD_SIZE)]
player_board_guess = [[" "]*8 for _ in range(BOARD_SIZE)]
computer_board = [[" "]*8 for _ in range(BOARD_SIZE)]
computer_board_guess = [[" "]*8 for _ in range(BOARD_SIZE)]

def reset():
    """
    Reset boards data for start and to play again
    """
    player_board = [[" "] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    player_board_guess = [[" "] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    computer_board = [[" "] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    computer_board_guess = [[" "] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    print(computer_board)



def show_board(board):
    """
    Makes and shows board for player to see progress
    """
    print(board[0])

    if board == player_board or board == player_board_guess or board == computer_board:
        print("  A B C D E F G H")
        print("  - - - - - - - -")
        row_number = 1
        for row in board:
            print(f"%d|%s" % (row_number, "|".join(row)))
            row_number += 1


def place_ships(board):
    """
    Places ships on board
    """
    for ship in SHIPS:
        while True:
            if board == computer_board:
                direction = random.choice(["H", "V"])
                row = random.randint(0, BOARD_SIZE-1)
                col = random.randint(0, BOARD_SIZE-1)
                if make_sure_ship_fits(board, ship, direction, row, col):
                    if not no_ship_overlap(board, ship, direction, row, col):
                        if direction == "H":
                            for i in range(col, col + ship):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + ship):
                                board[i][col] = "X"
                        break
            else:
                print(f"Place your ship size: {ship} on grid")
                direction, row, col = get_players_ship_position()
                if make_sure_ship_fits(board, ship, direction, row, col):
                    if not no_ship_overlap(board, ship, direction, row, col):
                        if direction == "H":
                            for i in range(col, col + ship):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + ship):
                                board[i][col] = "X"
                        break
#                break
            

def make_sure_ship_fits(board, ship, direction, row, col):
    """
    Checks ship co-ordinates doesn't exceed boudaries of board
    """
    if board == computer_board:
        if direction == "H":
            if col + ship > (BOARD_SIZE - 1):
                return False
            else:
                return True
        else:
            if row + ship > (BOARD_SIZE - 1):
                return False
            else:
                return True
    else:
        if direction == "H":
            if col + ship > (BOARD_SIZE - 1):
                print("The ship cannot go of the board\nTry another location\n")
                return False
            else:
                return True
        else:
            if row + ship > (BOARD_SIZE - 1):
                print("The ship cannot go of the board\nTry another location\n")
                return False
            else:
                return True



def no_ship_overlap(board, ship, direction, row, col):
    """
    Checks this ship doesn't overlap previous ships placed
    """
    if board == computer_board:
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
        if direction == "H":
            for i in range(col, col + ship):
                if board[row][i] == "X":
                    print("Wrong entry, ship cannot go ever another\nTry again\n")
                    return True
        else:
            for i in range(row, row + ship):
                if board[i][col] == "X":
                    print("Wrong entry, ship cannot go over another\nTry again\n")
                    return True
        return False


def get_players_ship_position():
    while True:
        try:
            direction = input("Enter direction you would like to position your ship, (H) horizontal (V) Vertical\n").upper()
            while direction not in ("H", "V"):
                print("Incorrect choice, only H or V")
                break
            if direction == "H" or direction == "V":
                break
        except ValueError:
            print("Wrong input Try 'H' or 'V'\n")
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
            print("Wrong input, select a number between 1 and 8\n")
    while True:
        try:
            col = input("Enter column you would like to place ship (A to H)\n").upper()
            while col not in ALPHA_NUMERO.keys():
                print("Wrong input, enter A to H\n")
                break
            if col in ALPHA_NUMERO.keys():
                col = ALPHA_NUMERO[col]
                break
        except ValueError:
            print("Wrong input, enter letter between A and H\n")
    return direction, row, col

def hit_ship_check(board):
    """
    Check for hit
    """




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


def new_game():
    """
    Starts a new game, set board size, number of ships,
    resets scores and initialises boards.
    """
    reset()
    board = computer_board
    place_ships(board)
    show_board(board)
    board = player_board
    place_ships(board)
    show_board(board)


    



    
new_game()

