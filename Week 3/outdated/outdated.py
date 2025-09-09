months = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
)


def main():
    get_date()


def get_date():
    while True:
        date = input("Date: ").strip().title()

        # If date exists,
        if date:

            # Handle formats of form MM/DD/YYYY
            if '/' in date:
                valid = number_format(date)
                if not valid:
                    continue
                else:
                    break

            # startswith() requires a *string* or a "tuple of strings" to iterate over.
            elif date.split()[0] in months:
                valid = string_format(date)
                if not valid:
                    continue
                else:
                    break


def number_format(date):
    date = date.split("/")

    # Ensure only MM, DD and YYYY exist.
    if len(date) != 3:
        return False

    # Avoid inputs of containing characters other than digits.
    for value in date:
        if not value.isnumeric():
            return False

    date = [int(value) for value in date]

    # Validate month.
    if date[0] <= 0 or date[0] > 12:
        return False
    # Validate day.
    elif date[1] <= 0 or date[1] > 31:
        return False
    # Validate CE.
    elif date[2] < 1:
        return False

    # If everything goes well, print the iso_format of the number.
    return iso_format(date)


def string_format(date):
    date = date.split()

    date_length = len(date)
    if date_length != 3:
        return False

    # Ensure ',' exists in the second format input. July 31, 2015
    month_length = len(date[1])

    if month_length < 2 or month_length > 3:
        return False

    if date[1][month_length - 1] != ',':
        return False

    # Remove ',' from July 31, 1980.
    if month_length == 2:
        date[1] = int(date[1][0])
    else:
        date[1] = int(date[1][0]+date[1][1])

    # Ensure month belongs to [1,31]
    if date[1] <= 0 or date[1] > 31:
        return False

    # Convert months to the corresponding numeric value.
    try:
        date[0] = months.index(date[0]) + 1
    except ValueError:
        return False

    date[2] = int(date[2])

    return iso_format(date)


def iso_format(date):
    # Order Correction
    date = [date[2], date[0], date[1]]

    # Add leading zeroes.
    for index in range(1, 3):
        date[index] = f"{date[index]:02}"

    date[0] = f"{date[0]}"

    # Add '-'
    date = '-'.join(date)
    print(date)

    return True


if __name__ == "__main__":
    main()
