import re

'''
    Using re module
'''

def main():
    try:
        print(is_valid(input("What's your email address? ").strip()))
    except (EOFError, KeyboardInterrupt):
        print()


def is_valid(mail):
    if re.search(r"^[\w.]+@{1}(?:\w+\.)+\w+$", mail):
        return "Valid"

    return "Invalid"


if __name__ == "__main__":
    main()
