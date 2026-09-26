
COLUMNS = {
    "1": [(5, 0), (4, 0), (3, 0), (2, 0), (1, 0), (0, 0)], 
    "2": [(5, 1), (4, 1), (3, 1), (2, 1), (1, 1), (0, 1)],
    "3": [(5, 2), (4, 2), (3, 2), (2, 2), (1, 2), (0, 2)],
    "4": [(5, 3), (4, 3), (3, 3), (2, 3), (1, 3), (0, 3)],
    "5": [(5, 4), (4, 4), (3, 4), (2, 4), (1, 4), (0, 4)],
    "6": [(5, 5), (4, 5), (3, 5), (2, 5), (1, 5), (0, 5)],
    "7": [(5, 6), (4, 6), (3, 6), (2, 6), (1, 6), (0, 6)]
}

VALID_COLUMNS = ["1", "2", "3", "4", "5", "6", "7"]

def show_empty_board():
    print("| | | | | | | |\n" * 6, end = "")
    print("|1|2|3|4|5|6|7|")

def create_empty_board():
    board = [
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "]
    ]
    return board

def print_board(board):
    for line in board:
        for symbol in line:
            print("|", end = "")
            print(symbol, end = "")
        print("|")

def print_helper_line():
    print("|1|2|3|4|5|6|7|")

def switch_player(current_player):
    if current_player == 1:
        current_player = 2
    elif current_player == 2:
        current_player = 1

def welcome_message():
    print("Welcome to Connect Four!")
    print("Player 1 will be \"0\"")
    print("Player 1 will be \"X\"")

