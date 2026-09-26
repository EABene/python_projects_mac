
def show_empty_board():
    print("| | | | | | | |\n" * 6, end = "")
    print("|1|2|3|4|5|6|7|")

def create_empty_board():
    board = [
        ["|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|"],
        ["|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|"],
        ["|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|"],
        ["|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|"],
        ["|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|"],
        ["|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|"],
        ["|", "1", "|", "2", "|", "3", "|", "4", "|", "5", "|", "6", "|", "7", "|"]
    ]
    return board

def print_board(board):
    for line in board:
        for symbol in line:
            print(symbol, end = "")
        print("")

def switch_player(current_player):
    if current_player == 1:
        current_player = 2
    elif current_player == 2:
        current_player = 1

def welcome_message():
    print("Welcome to Connect Four!")
    print("Player 1 will be \"0\"")
    print("Player 1 will be \"X\"")