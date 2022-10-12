import random
import re
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset = True)
from clear_screen import clear
import gspread
from google.oauth2.service_account import Credentials
SCOPE = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file',
         'https://www.googleapis.com/auth/drive']
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("dooco_battleship")




def print_winning_list(win_list):
    """
    get the player entries, password and score 
    """
    
    if len(win_list) > 5:
        del win_list[5:]
    print("Top 5 winners")
    print("Player Name" + " "*6 + "Score")
    for each in win_list:
        print('{:12}:{:>8}'.format(str(each[0]), str(each[2])))
    return win_list


def create_new_player():
    """
    Creates a new user
    """
    while True:
        new_player = input("Please enter your player name (12 characters max):\n")
        if len(new_player) < 12 and new_player.isalnum():
            return new_player
            break
        print("Must be alphanumeric and less than 12 characters\n")


def get_passwd():
    """
    Get a password at least 6 chars, one upper case, one lower case
    one digit, one sp[ecial character.

    Code credit to stack overflow
    """
    while True:
        pword = input("Enter a password at least 6 chars, one upper case," + 
        " one lower case one digit, one sp[ecial character:\n ")
        if (re.match(
            "(?=.{6,})" + 
        "(?=.*[A-Z].*)" +
        "(?=.*[a-z].*)" +
        "(?=.*\d.*)" +
        "(?=.*[\!\@\#\$\%\^\&\*].*)(?=^[\!\@\#\$\%\^\&\*a-zA-Z0-9]+$)" +
        "^.*$", pword)):
            print("good")
            return pword
            break
        
    



# Import random function so that positions on board 
# can be randomised.
# 
ALPHA_NUMERO = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
ONE_TO_EIGHT = ("1", "2", "3", "4", "5", "6", "7", "8")
BOARD_SIZE = 8
SHIPS = [2,3,3,4,5]
PLAYER_COL = colorama.Fore.BLUE
COMPUTER_COL = colorama.Fore.RED
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
    if (board == player_board) or (board == player_board_guess):
        board_col = PLAYER_COL
    else:
        board_col = COMPUTER_COL
    print(board_col + "  A B C D E F G H")
    print(board_col + "  - - - - - - - -")
    row_number = 1
    for row in board:
        print(board_col + "%d|%s" % (row_number, f"{board_col}|".join(row)))
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
    print(colorama.Fore.RED + "="* 110)
    print("\n")
    print(colorama.Fore.RED + "#########      ###  ########### ########### ###        #########   ######   ###    ###  #########  #########")
    print(colorama.Fore.RED + "###    ###   ### ###    ###         ###     ###      " +
          "  ###       ###    ### ###    ###     ###     ###    ### ")
    print(colorama.Fore.RED + "###    ###  ###   ###   ###         ###     ###      " +
          "  ###       ###        ###    ###     ###     ###    ###")
    print(colorama.Fore.RED + "#########  ###########  ###         ###     ###      " +
          "  ########  ########## ##########     ###     #########")
    print(colorama.Fore.RED + "###    ### ###     ###  ###         ###     " +
          "###        ###              ### ###    ###     ###     ###")
    print(colorama.Fore.RED + "###    ### ###     ###  ###         ###     " +
          "###        ###       ###    ### ###    ###     ###     ###")
    print(colorama.Fore.RED + "#########  ###     ###  ###         ###     " +
          "########## #########  ########  ###    ###  #########  ###")
    print(" ")
    print(colorama.Fore.RED + "="* 110)
    print("\n")
    print(PLAYER_COL + "Instructions for Battleship")
    print("\n")
    print(COMPUTER_COL + "="* 110)
    print(PLAYER_COL + "Player must guess co-ordinates of opponent's ships")
    print(PLAYER_COL + "Objective is to hit all of opponent's ships before" + 
    " opponent hits all of yours.\n")
    print(PLAYER_COL + "Enter your guess as a row number between 1 and 8 and ")
    print(PLAYER_COL + "Enter your colum letter between 'A' and 'H'\n") 
    print(PLAYER_COL + "@ = co-ordinates of a MISS\n")
    print(PLAYER_COL + "X = co-ordinates of a HIT")
    print(COMPUTER_COL + "="* 110)


def new_game():
    """
    Starts a new game, set board size, number of ships,
    resets scores and initialises boards.
    """
    win_list = []
    hi_score = SHEET.worksheet("nam_pas_scr")
    score = hi_score.get_values()
    for i in score:
        win_list.append(i)
    print_winning_list(win_list)
    new_player = create_new_player()
    matching = [s for s in win_list if new_player in s]
    if not matching:
        print("H U R R A Y   Y O U R   N A M E  I S   A V A I L A B L E")
    print(new_player)
    quit()
    
    welcome()
    place_ships(computer_board)
    print("Place your ships")
    place_ships(player_board)
    
    while True:
        while True:
            
            welcome()
            print(COMPUTER_COL + "\nComputer's guess board\n")
            show_board(computer_board_guess)
            print(PLAYER_COL + "\nPlayer's guess board\n")
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
            
            make_move(computer_board_guess)
            break
       
        if hit_ship_check(computer_board_guess) == 17:
            welcome()
            show_board(computer_board_guess)
            print(("You have Lost\n"))
            print("Computer has won\n")
            quit()


            

    



    



    
new_game()

