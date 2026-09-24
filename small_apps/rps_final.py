import random
import sys

def one_round():
    user_input = input("Enter Schere, Stein oder Papier >> ")
    choices = ["Schere", "Stein", "Papier"]
    computer_choice = random.choice(choices)
    result = ""

    if user_input == "exit":
        print("Exit sequence...")
        sys.exit(0)
    elif user_input not in choices:
        print("invalid input.")
    elif user_input == "Schere":
        solver = {
            "Schere": "draw",
            "Stein": "you lose",
            "Papier": "you win"
        }
        print(f"Computer choice: {computer_choice}")
        result = solver[computer_choice]
        print(result)
    elif user_input == "Stein":
        solver = {
            "Schere": "you win",
            "Stein": "draw",
            "Papier": "you lose"
        }
        print(f"Computer choice: {computer_choice}")
        result = solver[computer_choice]
        print(result)
    elif user_input == "Papier":
        solver = {
            "Schere": "you lose",
            "Stein": "you win",
            "Papier": "draw"
        }
        print(f"Computer choice: {computer_choice}")
        result = solver[computer_choice]
        print(result)
    return(result)

# def main():
user_score = 0
computer_score = 0
result = ""
while user_score < 3 and computer_score < 3:
    result = one_round()
    if result == "you win":
        user_score = user_score + 1
    elif result == "you lose":
        computer_score = computer_score + 1
    if user_score < 3 and computer_score < 3:
        print(f"Score: You: {user_score}, Computer: {computer_score}")
    print("-" * 20)

if user_score > computer_score:
    print("YOU WIN !!!")
elif user_score < computer_score:
    print("Match lost... :(")
print(f"Final result: You: {user_score}, Computer: {computer_score}")
print("-" * 20)