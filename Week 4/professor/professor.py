from random import randint
from sys import exit


def main():
    level = get_level()

    play_at(level)


def get_level():
    while True:
        try:
            # Handle invalid strings for int() conversion.
            lvl = int(input("Level: ").strip())
        except ValueError:
            continue
        else:
            # Only accept positive integers [1,3].
            if lvl not in [1, 2, 3]:
                continue
            else:
                return lvl


def play_at(level):
    score = 0

    # Generate question.
    for _ in range(10):
        x, y = generate_integer(level), generate_integer(level)

        # Evaluate answers:
        right = False

        for attempt in range(3):
            try:
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                continue

            # Check only if answer has a value.
            if answer == (x + y):
                right = True
                break
            else:
                print("EEE")

        # Display the right answer on being wrong more than thrice.
        if not right:
            print(f"{x} + {y} = {x + y}")
        else:
            score += 1

    # Print score at the end.
    print(f"Score: {score}")


def generate_integer(level):
    # In case of level = 1, 10*0 = 1.
    if level == 1:
        random_int = randint(0, 9)
    else:
        random_int = randint(10**(level-1), 10**level - 1)
    return random_int


if __name__ == "__main__":
    main()
