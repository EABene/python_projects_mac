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

def valid_move(move, board):
    if move not in VALID_COLUMNS:
        return False
    row, col = COLUMNS[move][-1]
    if board[0][col] != " ":
        return False
    return True

def insert_in_board(move, board, symbol):
    columns = COLUMNS[move]
    i = 0
    while board[columns[i]] != " ":
        i += 1
    board[columns[i]] = symbol

def game_over_check(board, move):
    curr_column = COLUMNS[move]
    row, col = COLUMNS[move]
    while board[row][col] != " ":
        row -= 1
    row += 1
    curr_symbol = board[row][col]
    counter = 1
    

def play_one_game():
    play_ongoing = True
    curr_player = 1
    move = ""
    board = h.create_empty_board()
    
    while play_ongoing:
        symbol = "0" if curr_player == 1 else "X" # ternary
        while not valid_move(move, board):
            move = input(f"Player {curr_player} {symbol} move:")
            if move == "exit":
                print("Game aborted")
                break
            if valid_move(move, board) == False:
                print("Invalid move. Try again")
                continue
        insert_in_board(move, board, symbol)
        game_over_check(board, move)
        h.switch_player(curr_player)



    # check if game is won or drawn
    # if not, other players turn

print(COLUMNS["3"][0])