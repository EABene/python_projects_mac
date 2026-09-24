def print_board_help():
    print("1|2|3")
    print("-+-+-")
    print("4|5|6")
    print("-+-+-")
    print("7|8|9")

def empty_board():
    print(" | | ")
    print("-+-+-")
    print(" | | ")
    print("-+-+-")
    print(" | | ")

def create_board():
    board = [[" ", "|", " ", "|", " "],
            [" ", "|", " ", "|", " "],
            [" ", "|", " ", "|", " "]]
    return(board)

def print_current_board(board):
    for line in board:
        for field in line:
            print(field, end="")
        print("")