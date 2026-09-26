# connect four game functionality
import helpers as h
import game_over_check as goc

def valid_move(move, board):
    if move not in h.VALID_COLUMNS:
        return False
    row, col = h.COLUMNS[move][-1]
    if board[0][col] != " ":
        return False
    return True

def insert_in_board(move, board, symbol):
    columns = h.COLUMNS[move]
    i = 0
    while board[columns[i]] != " ":
        i += 1
    board[columns[i]] = symbol
    return columns[i]

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
        curr_move = insert_in_board(move, board, symbol)
        goc.game_over_check(board, curr_move)
        h.switch_player(curr_player)



    # check if game is won or drawn
    # if not, other players turn

print(h.COLUMNS["3"][0])