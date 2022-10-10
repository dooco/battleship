import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset = True)
from clear_screen import clear

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
    

def get_a_key(event):
    while True:
        if event.key.isalpha() or event.key.isdigit():
            print(event.key)
            return event.key



def show_board(board):
    """
    Makes and shows board for player to see progress
    """
    if board == player_board or board == player_board_guess or board == computer_board_guess:
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
                direction = get_direction()
                row, col = get_position()
                if make_sure_ship_fits(board, ship, direction, row, col):
                    if not no_ship_overlap(board, ship, direction, row, col):
                        if direction == "H":
                            for i in range(col, col + ship):
                                board[row][i] = "X"
                                welcome()
                                show_board(board)
                        else:
                            for i in range(row, row + ship):
                                board[i][col] = "X"
                                welcome()
                                show_board(board)
                        break

            

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


def get_direction():
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
    return direction


def get_position():
    while True:
        try:
            print("Enter row you would like to place ship (1-8\n")
            row = input(("Enter row you would like to place ship (1-8) \n"))
            #row = get_a_key(event)
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
    return row, col


def make_move(board):
    """
    puts bomb on board
    """
    if board == player_board_guess:
        row, col = get_position()
        if board[row][col] == "@" or board[row][col] == "X":
            print("Computer's Guess board\n")
            show_board(computer_board_guess)
            print("\nYour Guess board\n")
            show_board(player_board_guess)
            print("You have already guessed that position. Go again")
            make_move(board)
        elif computer_board[row][col] == "X":
            board[row][col] = "X"
        else:
            board[row][col] = "@"
    else:
        row, col = random.randint(0, BOARD_SIZE-1), random.randint(0, BOARD_SIZE-1)
        if board[row][col] == "@" or board[row][col] == "X":
            make_move(board)
        elif player_board[row][col] == "X":
            board[row][col] = "X"
        else:
            board[row][col] = "@"

    
def hit_ship_check(board):
    """
    Check for hit
    """
    player_hit = 0
    computer_hit = 0
    if board == player_board_guess:
        for row in board:
            for col in row:
                if col == "X":
                    player_hit += 1
        return player_hit
    elif board == computer_board_guess:
        for row in board:
            for col in row:
                if col == "X":
                    computer_hit += 1
        return computer_hit




def welcome():
    """
    Display  instructions and information about game
    """
    clear()
    print("\n")
    print(colorama.Fore.RED + "#########      ###  ########### ########### ###        ##########  ######   ###    ###  #########  #########")
    print(colorama.Fore.RED + "###    ###   ### ###    ###         ###     ###      " +
          "  ###       ###    ### ###    ###     ###     ###    ### ")
    print(colorama.Fore.RED + "###    ###  ###   ###   ###         ###     ###      " +
          "  ###       ###        ###    ###     ###     ###    ###")
    print(colorama.Fore.RED + "#########  ###########  ###         ###     ###      " +
          "  ########  ########## ##########     ###     #########")
    print(colorama.Fore.RED + "###    ### ###     ###  ###         ###     ###      " +
          "  ###              ### ###    ###     ###     ###")
    print(colorama.Fore.RED + "###    ### ###     ###  ###         ###     ###      " +
          "  ###       ###    ### ###    ###     ###     ###")
    print(colorama.Fore.RED + "#########  ###     ###  ###         ###     ##########" +
          " ########## ########  ###    ###  #########  ###")
    print(" ")
    print(colorama.Fore.RED + "="* 110)
    
    print(f"\n")
    print(f"\n")
    print("="* 110)
    print("Instructions for Battleship")
    print("Player must guess co-ordinates of opponent's ships")
    print(f"Objective is to hit all of opponent's ships ships before opponent hit yours.")
    print("Enter your guess as a row number between 1 and 8 and ")
    print("Enter your colum letter between 'A' and 'H'\n")
    print("="* 110)
    print("@ = a ship on the battle grid\n")
    print("* = co-ordinates of a ")
    print("X = co-ordinates of a HIT")


def new_game():
    """
    Starts a new game, set board size, number of ships,
    resets scores and initialises boards.
    """
    
    welcome()
    place_ships(computer_board)
    print("Place your ships")
    place_ships(player_board)
    
    while True:
        while True:
            print("Player's guess board\n")
            welcome()
            show_board(player_board_guess)
            make_move(player_board_guess)
            break
        if hit_ship_check(player_board_guess) == 17:
            welcome()
            show_board(player_board_guess)
            print(("You have won\n"))
#           score_plus()
#           increase player score on table
            quit()
        while True:            
            welcome()
            print("Computer's guess board\n")
            show_board(computer_board_guess)
            make_move(computer_board_guess)
            break
       
        if hit_ship_check(computer_board_guess) == 17:
            welcome()
            show_board(computer_board_guess)
            print(("You have Lost\n"))
            print("Computer has won\n")
            quit()

            

    



    



    
new_game()

