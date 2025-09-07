from sys import exit

def main():
    # Accepting time
    time_input = input("What time is it? ")

    time = convert(time_input)
    meal_type(time)


def sanitize(time):
    time = time.strip().split(":")
    index = 0

    # Inputs like ' 17  :  30 '
    for value in time:
        time[index] = value.strip()

        # For time = '1   3:  3 0' types.
        time_length = len(time[index].split())
        split_time = time[index].split()
        if (time_length != 1):
            time[index] = ""
            for index in range(time_length):
                time[index] += split_time[index]

        index += 1

    # Find the time format.
    format_24 = format(time)

    hours = float(time[0])

    denomination, minutes = '', ''
    if format_24:
        minutes = float(time[1])
    else:
        index = 0
        for x in time[1]:
            # Handles cases like 12:xyz
            if index < 2 and x.isdigit():
                minutes += x
            else:
                # Standardize denomination.
                denomination += x.lower()
            index += 1

        if minutes != '':
            minutes = float(minutes)
        else:
            print()
            exit("Enter a valid minute value!")

    return hours, minutes, format_24, denomination


def convert(time):
    hours, minutes, format_24, denomination = sanitize(time)

    if format_24:
        # Ensuring 24 hour format.
        if 0 <= hours < 24 and 0 <= minutes < 60:
            return hours + round(minutes/60, 2)
        else:
            print("Invalid Time!")
            return -1

    else:
        if 1 <= hours <= 12 and 0 <= minutes < 60:
            match denomination:
                case "am" | "a.m":
                    if hours == 12:
                        hours = 0
                    return hours + round(minutes/60, 2)
                case "pm" | "p.m":
                    if hours != 12:
                        hours += 12
                    return hours + round(minutes/60, 2)
                case _:
                    exit("Invalid denomination\nUse: ['am','pm','a.m','p.m']")


def format(time):
    if time[0].isnumeric():
        if time[1].isnumeric():
            return True
        else:
            return False

    else:
        exit("Format: (X)X:XX or (X)X:XX a/p.m")


def meal_type(time):
    # Print meal type for the time
    if 7.00 <= time <= 8.00:
        print("breakfast time")
    elif 12.00 <= time <= 13.00:
        print("lunch time")
    elif 18.00 <= time <= 19.00:
        print("dinner time")

    '''
    else:
        print("No meal for this time")
    '''


if __name__ == "__main__":
    main()
