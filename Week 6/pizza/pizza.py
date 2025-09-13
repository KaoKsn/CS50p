import sys
import csv
from tabulate import tabulate


def main():

    # Handle invalid command-line arguments.
    validate_command_line_args()

    menu_file, file = get_file(sys.argv[1])

    print_menu(menu_file)

    # Close file.
    file.close()


def validate_command_line_args():
    length = len(sys.argv)

    if length == 1:
        sys.exit("Too few command-line arguments")
    elif length > 2:
        sys.exit("Too many command-line arguments")


def get_file(cli_input):
    # Handle invalid extension. {Generalize the case: test.txt.CsV}
    if not cli_input.lower().endswith('.csv'):
        sys.exit("Invalid file extension! File must end with '.csv'")

    # Check if file exists.
    try:
        file = open(cli_input)
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        return csv.DictReader(file), file


def print_menu(menu_file):
    # Goes through every line as a dict and uses "keys" as the Column name.
    print(tabulate(menu_file, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()
