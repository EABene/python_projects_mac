from helpers import show_empty_board, create_empty_board, print_board
from game import play

# Connect Four game
# 7 x 6 board

board = create_empty_board()
print_board(board)
board[5][1] = "0"
board[2][13] = "X"
print_board(board)
play()
