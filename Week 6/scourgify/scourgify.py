import sys
import csv


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
    except PermissionError:
        sys.exit("Can't open file, Permission Denied")


def create_new_file(ofile):
    # List of dictionary of people with the following keys: "first", "last", "house".
    people = []

    # Read data from the old file to the memory.
    reader = csv.DictReader(ofile)
    for row in reader:
        person = {}

        # Split first and last name.
        name = row["name"].split(',')

        if len(name) != 2:
            sys.exit("Aborting write operation: Invalid Name Format")

        # Remove the leading space from the first name.
        name[1] = name[1].lstrip()

        # Ensure all the fields exist in before.csv
        if not name[0] or not name[1] or not row["house"]:
            sys.exit("Aborting write operation: Column value missing")

        # Add person to people.
        person = {
            "first": name[1],
            "last": name[0],
            "house": row["house"]
        }

        # append() takes references.
        people.append(person)

    # Writing to a new file.
    try:
        new_file = open(sys.argv[2], "w")
    except PermissionError:
        sys.exit("Can't open file to write, Permission Denied!")

    writer = csv.DictWriter(new_file, fieldnames=["First", "Last", "House"])
    # Write the column headings.
    writer.writeheader()

    for p in people:
        writer.writerow({"First": p["first"], "Last": p["last"], "House": p["house"]})


if __name__ == "__main__":
    main()
