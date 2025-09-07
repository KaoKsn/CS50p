def main():
    answer = input("What is the answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

    if validate(answer):
        print("Yes")
    else:
        print("No")


def validate(answer):
    match answer:
        case "forty-two" | "forty two" | "42":
            return True
        case _:
            return False

    '''
    if answer in ["forty-two", "forty two", "42"]:
            return True
        else:
            return False
    '''


if __name__ == "__main__":
    main()
