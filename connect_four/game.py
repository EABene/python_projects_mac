# connect four game functionality
import helpers as h

COLUMNS = {
    "1": [(5, 1), (4, 1), (3, 1), (2, 1), (1, 1), (0, 1)], 
    "2": [(5, 3), (4, 3), (3, 3), (2, 3), (1, 3), (0, 3)],
    "3": [(5, 5), (4, 5), (3, 5), (2, 5), (1, 5), (0, 5)],
    "4": [(5, 7), (4, 7), (3, 7), (2, 7), (1, 7), (0, 7)],
    "5": [(5, 9), (4, 9), (3, 9), (2, 9), (1, 9), (0, 9)],
    "6": [(5, 11), (4, 11), (3, 11), (2, 11), (1, 11), (0, 11)],
    "7": [(5, 13), (4, 13), (3, 13), (2, 13), (1, 13), (0, 13)],
}

VALID_COLUMNS = ["1", "2", "3", "4", "5", "6", "7"]

def make_move(player):
    pass

def welcome_message():
    print("Welcome to Connect Four!")
    print("Player 1 will be \"0\"")
    print("Player 1 will be \"X\"")

def valid_move(move, board):
    if move not in VALID_COLUMNS:
        return False
    row, col = COLUMNS[move][-1]
    if board[0][col] != " ":
        return False
    return True

def insert_in_board(move, board):


def play_one_game():
    play_ongoing = True
    curr_player = 1
    move = ""
    board = h.create_empty_board()
    
    while play_ongoing:
        symbol = "0" if curr_player == 1 else "X" # ternary
        while not valid_move(move):
            move = input(f"Player {curr_player} {symbol} move:")
            if move == "exit":
                print("Game aborted")
                break
        insert_in_board(move, board)
        h.switch_player(curr_player)


    # write move into board if legal
    # check if game is won or drawn
    # if not, other players turn

