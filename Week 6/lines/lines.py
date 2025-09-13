import sys


def main():

    # Handle invalid command-line arguments.
    validate_command_line_arg()

    program = get_file(sys.argv[1])

    print_total_lines_in(program)

    # Close file.
    program.close()

def validate_command_line_arg():
    length = len(sys.argv)

    if length == 1:
        sys.exit("Too few command-line arguments")
    elif length > 2:
        sys.exit("Too many command-line arguments")


def get_file(cli_input):
    # Handle invalid extension. {Generalize the case: test.txt.pY}
    if not cli_input.lower().endswith(".py"):
        sys.exit("Invalid file extension! File must end with '.py'")

    # Check if file exists.
    try:
        file = open(cli_input)
    except FileNotFoundError:
        sys.exit("File does not exit")
    else:
        return file


def print_total_lines_in(program):
    total_lines = 0
    for line in program:
        if line.strip() == '' or line.strip().startswith("#"):
            continue
        else:
            total_lines += 1
    print(total_lines)


if __name__ == "__main__":
    main()
