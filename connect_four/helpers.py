ROWS = 6
COLS = 7

# "1" -> [(5, 0), (4, 0), ..., (0, 0)]  (bottom to top)
COLUMNS = {
    str(col + 1): [(row, col) for row in range(ROWS - 1, -1, -1)]
    for col in range(COLS)
}

VALID_COLUMNS = list(COLUMNS.keys())

SYMBOLS = {1: "O", 2: "X"}


def create_empty_board():
    return [[" "] * COLS for _ in range(ROWS)]


def print_board(board):
    print()
    for line in board:
        print("|" + "|".join(line) + "|")
    print_helper_line()


def print_helper_line():
    print("|" + "|".join(VALID_COLUMNS) + "|")


def switch_player(current_player):
    return 2 if current_player == 1 else 1


def welcome_message():
    print("Welcome to Connect Four!")
    print(f'Player 1 will be "{SYMBOLS[1]}"')
    print(f'Player 2 will be "{SYMBOLS[2]}"')
    print('Type a column number (1-7) to drop a piece, or "exit".')