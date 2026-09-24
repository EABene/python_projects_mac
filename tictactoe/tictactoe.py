from layouts import create_board, print_current_board

WIN_LINES = [
    [(0, 0), (0, 2), (0, 4)], # rows
    [(1, 0), (1, 2), (1, 4)],
    [(2, 0), (2, 2), (2, 4)],
    [(0, 0), (1, 0), (2, 0)], # columns
    [(0, 2), (1, 2), (2, 2)],
    [(0, 4), (1, 4), (2, 4)],
    [(0, 0), (1, 2), (2, 4)], # diagonals
    [(0, 4), (1, 2), (2, 0)]
]

def game_over_check(board):
    for line in WIN_LINES:
        fields = []
        for position in line:
            row = position[0]
            col = position[1]
            fields.append(board[row][col])

        a = fields[0]
        b = fields[1]
        c = fields[2]

        if a != " " and a == b == c:
            return a
        
    return None

def modify_board(field, player, board):
    field_translator = {
    "1": (0, 0), "2": (0, 2), "3": (0, 4),
    "4": (1, 0), "5": (1, 2), "6": (1, 4),
    "7": (2, 0), "8": (2, 2), "9": (2, 4),
    }
    if player == 1:
        symbol = "O"
    if player == 2:
        symbol = "X"
    if field not in field_translator:
        return 1
    row, col = field_translator[field]
    if board[row][col] != " ":
        return 1
    else:
        board[row][col] = symbol
        return 0

def board_full(board):
    for line in board:
        for field in line:
            if field == " ":
                return False
    return True

def player_turn(player, board):
    if player == 1:
        prompt = "Player 1s turn (O) >> "
    else:
        prompt = "Player 2s turn (X) >> "

    while True:
        print_current_board(board)
        field = input(prompt)
        if modify_board(field, player, board) == 0:
            return 

def tictactoe():
    board = create_board()
    player = 1

    while game_over_check(board) is None and not board_full(board):
        if player == 1:
            player_turn(1, board)
            player = 2
        elif player == 2:
            player_turn(2, board)
            player = 1
        
    print("Final board:")
    print_current_board(board)
    result = game_over_check(board)
    if result == "O":
        print("Player 1 won the game!")
    elif result == "X":
        print("Player 2 won the game!")
    else:
        print("game ends in a draw")
        
    """
    board = create_board()
    print_current_board(board)
    modify_board("2", 1, board)
    print_current_board(board)
    """