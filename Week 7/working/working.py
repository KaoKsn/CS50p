import re

# Doesn't handle 0X:XX Format.

def main():
    try:
        print(convert(input("Hours: ")))
    except (EOFError, KeyboardInterrupt):
        print()
    '''
    except ValueError:
        print("Invalid Format or(and) Time")

    # check50 only expects: raise ValueError
    '''


def convert(duration_12hr):
    if duration := re.search(r"^([0-9]|1[0-2])(:[0-5][0-9])? (AM|PM) to ([0-9]|1[0-2])(:[0-5][0-9])? (AM|PM)$", duration_12hr):

        # Start time analysis.
        start_time = convert_to_24(duration.group(1), duration.group(2), duration.group(3))

        # End time analysis.
        end_time = convert_to_24(duration.group(4), duration.group(5), duration.group(6))

        # Return 24hr format converted duration of work.
        return f"{start_time} to {end_time}"

    else:
        raise ValueError


def convert_to_24(hours, minutes, denomination):
    hours = int(hours)
    # Handle AM
    if denomination == "AM":
        return f"{hours % 12:02d}{minutes}" if minutes else f"{hours % 12:02d}:00"

    # Handle PM.
    else:
        return f"{hours % 12 + 12}{minutes}" if minutes else f"{hours % 12 + 12}:00"


if __name__ == "__main__":
    main()
