from random import randint
from sys import exit


def main():
    level = get_pint("Level: ")

    play_at(level)


def get_pint(inp_str):
    while True:
        try:
            p_int = int(input(inp_str).strip())
        except ValueError:
            continue
        else:
            # Only accept positive integers.
            if not p_int > 0:
                continue
            else:
                return p_int


def play_at(level):
    while True:
        # Generate a random number from [1, level].
        rand = randint(1, level)

        # Get a positive integer guess.
        guess = get_pint("Guess: ")

        # Give user feedback.
        feedback(guess, rand)


def feedback(guess, rand):
    if rand > guess:
        print("Too small!")
    elif rand < guess:
        print("Too large!")
    else:
        exit("Just right!")


if __name__ == "__main__":
    main()
