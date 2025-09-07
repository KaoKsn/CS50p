def main():
    due_amount = 50
    while True:
        print(f"Amount Due: {due_amount}")

        # Accept valid coins.
        coin = get_int("Insert Coin: ")

        match coin:
            # Check if a valid coin is entered.
            case 25 | 10 | 5:
                # Assure that the coin is not greater than the due amount.
                if due_amount - coin >= 0:
                    due_amount -= coin
                    print()
                    # If a total of $50 is paid
                    if due_amount == 0:
                        print("Change Owed: 0")
                        break
                else:
                    # Ensure the right amount of change is returned.
                    print(f"Change Owed: {coin-due_amount}")
                    break

            case _:
                print()
                continue


def get_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Select one from [$25, $10, $5]")


if __name__ == "__main__":
    main()
