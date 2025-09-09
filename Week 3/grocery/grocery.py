def main():
    # Print the items in the list, after getting the required items.
    print_list(get_items())


def get_items():
    grocery_list = {}
    while True:
        # Get item name and convert it all to lower.
        try:
            words_in_item = input().strip().upper().split()

        # If Ctrl + D/C then,
        except (EOFError, KeyboardInterrupt):
            print()
            break

        else:
            # Ensure non-empty list.
            if words_in_item:
                # Handle valid cases like '   foo   baz  '
                item = ' '.join(words_in_item)

                # Update list.

                # If item already exists, increment quantity.
                if item in grocery_list:
                    grocery_list[item] += 1
                # Else, add item to the grocery grocery_list(dict).
                else:
                    grocery_list[item] = 1
    return grocery_list


def print_list(grocery_list):
    # sorted(dict.items()) - List of Tuples.
    # dict.keys() - List of keys.

    for item in sorted(grocery_list.keys()):
        print(f"{grocery_list[item]} {item}")


if __name__ == "__main__":
    main()
