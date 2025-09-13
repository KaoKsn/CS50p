import sys
import csv


'''
    In version 2, handle:
    1. Error reading and writing the csv file.
    2. Handle PermissionError while both reading and writing the csv file.
    3. Validate that fields name, house are present in the input file.
'''


def main():

    # Handle invalid command-line arguments.
    validate_command_line_args()

    ofile = get_file(sys.argv[1])

    create_new_file(ofile)

    # Close old file.
    ofile.close()


def validate_command_line_args():
    length = len(sys.argv)

    if length in [1, 2]:
        sys.exit("Too few command-line arguments")
    elif length > 3:
        sys.exit("Too many command-line arguments")


def get_file(cli_input):
    # Handle invalid extension. {Generalize the case: test.txt.cSv}
    if not sys.argv[1].lower().endswith('.csv'):
        sys.exit("Invalid file extension! File must end with '.csv'")

    # Output file validation.
    elif not sys.argv[2].lower().endswith('.csv'):
        sys.exit("Invalid file extension! File must end with '.csv'")

    # Check if file exists.
    try:
        return open(cli_input)
    except FileNotFoundError:
        sys.exit("File does not exist")


def create_new_file(ofile):
    # List of dictionary of people with the following keys: "first", "last", "house".
    people = []

    # Read data from the old file to the memory.
    reader = csv.DictReader(ofile)
    for row in reader:
        person = {}

        # Split first and last name.
        name = row["name"].split(',')
        # Remove the leading space from the first name.
        name[1] = name[1].lstrip()

        # Add person to people.
        person = {
            "first": name[1],
            "last": name[0],
            "house": row["house"]
        }

        # append() takes references.
        people.append(person)

    # Writing to a new file.
    with open(sys.argv[2], "w") as new_file:
        writer = csv.DictWriter(new_file, fieldnames=["first", "last", "house"])
        # Write the column headings.
        writer.writeheader()

        for p in people:
            writer.writerow({"first": p["first"], "last": p["last"], "house": p["house"]})


if __name__ == "__main__":
    main()
