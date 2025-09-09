menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    process_order()


def process_order():
    total = 0
    while True:
        # Get item name in title-case.
        try:
            words_in_item = input("Item: ").strip().title().split()

        # If Ctrl + D/C then,
        except (EOFError, KeyboardInterrupt):
            print()
            break

        else:
            # Handle valid cases like '   Baja   Taco  '
            item = ' '.join(words_in_item)

            # Update total.
            if item in menu:
                total += menu[item]
                print(f"Total: ${total:.2f}")


if __name__ == "__main__":
    main()
