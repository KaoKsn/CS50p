import inflect


def main():
    names = get_names()

    adieu_to(names)


def get_names():
    names = []
    while True:
        try:
            name = input("Name: ").strip().title()

        except (KeyboardInterrupt, EOFError):
            print()
            break

        else:
            # Ensure that a single name is input everytime.
            if not len(name.split()) == 1:
                continue

            # Append to the list of names.
            names.append(name)

    return names


def adieu_to(names):
    # Ensure names is a non-empty list.
    if names:
        print("Adieu, adieu, to ", end='')

        # Single name.
        if len(names) == 1:
            print(names[0])

        # Multiple names.
        else:
            inflector = inflect.engine()
            names = inflector.join(names)
            print(names)


if __name__ == "__main__":
    main()
