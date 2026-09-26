# Connect Four game
# 7 x 6 board
import game as g
import helpers as h


def main():
    h.welcome_message()
    while True:
        g.play_one_game()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Bye!")
            break


if __name__ == "__main__":
    main()