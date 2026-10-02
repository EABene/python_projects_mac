
def print_lower():
    print("abcdefghijklmnop")

def print_upper():
    print("ABCDEFGHIJKLMNOP")

def print_numbers():
    print("0123456789")

match input("Print lower, upper or numbers? >> "):

    case "lower":
        print_lower()
    case "upper":
        print_upper()
    case "numbers":
        print_numbers()
    case _:
        print("Invalid input")

