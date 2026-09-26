import helpers as h
import game_over_check as goc


def valid_move(move, board):
    if move not in h.VALID_COLUMNS:
        return False
    col = int(move) - 1
    return board[0][col] == " "  # top cell empty -> column not full


def insert_in_board(move, board, symbol):
    for row, col in h.COLUMNS[move]:  # bottom to top
        if board[row][col] == " ":
            board[row][col] = symbol
            return row, col


def play_one_game():
    board = h.create_empty_board()
    curr_player = 1

    while True:
        symbol = h.SYMBOLS[curr_player]
        h.print_board(board)

        move = input(f"Player {curr_player} ({symbol}) move: ").strip()
        if move == "exit":
            print("Game aborted")
            return
        if not valid_move(move, board):
            print("Invalid move. Try again")
            continue  # same player again

        curr_move = insert_in_board(move, board, symbol)

        if goc.game_over_check(board, curr_move):
            h.print_board(board)
            print(f"Player {curr_player} ({symbol}) wins!")
            return
        if goc.board_full(board):
            h.print_board(board)
            print("It's a draw!")
            return

        curr_player = h.switch_player(curr_player)