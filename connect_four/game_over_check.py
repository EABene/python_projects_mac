import helpers as h

def game_over_check(board, curr_move):
    if horizontal_check(board, curr_move)or vertical_check(board, curr_move) or left_diagonal_check(board, curr_move) or right_diagonal_check(board, curr_move):
        return True
    return False

def horizontal_check(board, curr_move):
    symbol = board[curr_move]
    row, col = curr_move
    if col > 0:
     while symbol == board[row][col - 1]:
         col -= 1
    if board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3]:
        return True
    return False

def vertical_check(board, curr_move):
    symbol = board[curr_move]
    row, col = curr_move
    if row <= 2:
        if board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col]:
            return True
    return False

#TODO
def left_diagonal_check(board, curr_move):
    symbol = board[curr_move]
    row, col = curr_move
    if col > 0:
         while symbol == board[row][col - 1]:
             col -= 1
    if board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3]:
            return True
    return False

def right_diagonal_check():
    pass