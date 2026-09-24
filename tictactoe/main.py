from layouts import print_board_help
from tictactoe import tictactoe 
import sys

# game start
print("Welcome to Tic-Tac-Toe!")
print("Options:")
print("Show board layout -> help")
print("Start game -> start")
print("End app -> exit")

print_board_help()
tictactoe()

"""
# menu handling
valid_input = ["help", "start", "exit", "status"]
user = input(">> ") TODO PUT IN LOOP
while user != "exit":
    if user not in valid_input:
        print("Invalid input.")
    if user == "help":
        print_board_layout()
    if user == "exit":
        print("Exit sequence initiated...")
        sys.exit(0)
    if user == "start":
        tictactoe()
"""
