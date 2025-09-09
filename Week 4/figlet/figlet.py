from pyfiglet import figlet_format, FigletFont
from sys import exit, argv


def main():
    # Command Line input validation.

    arg_length = len(argv)

    # Accept a maximum of 2 and minium of 0 arguments.
    if arg_length not in [1, 3]:
        exit(figlet_format("Invalid Usage!", font="small_slant"))

    # If, font provided,
    elif arg_length == 3:
        # Ensure the right switch is used.
        if argv[1] not in ['-f', '--font']:
            exit(figlet_format("Invalid Usage!", font="small_slant"))

        # Check validity of the font.
        if argv[2] not in FigletFont.getFonts():
            exit(figlet_format("Invalid Font!", font="small_slant"))

        font = argv[2]

    else:
        font = "standard"

    plain_text = input("Input: ").strip()

    print(figlet_format(plain_text, font=font))


if __name__ == "__main__":
    main()
