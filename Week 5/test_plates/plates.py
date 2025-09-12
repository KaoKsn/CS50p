from string import punctuation

# ***** Input of "CS 50" is valid since the question only expects the plates to not have punctuations. ****


def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s = s.strip().upper()
    length = len(s)

    # Should start with atleast two letters.
    if not s[0:2].isalpha():
        return False
    # If 2 character long,
    if length == 2:
        return True

    # Should be of length between [2,6]
    elif not 2 < length <= 6:
        return False
    # Should not contain any special character.
    elif any(char in punctuation for char in s):
        return False



    # Numbers can't be used in the middle of the plate and must not start with 0.
    numeric_part = ""
    been_through_digit = False
    for char in s[2:length]:
        # If s[2] is a digit, s[2+] can't be alphabets.
        if char.isdigit():
            numeric_part += char
            been_through_digit = True

        elif char.isalpha():
            # Check if the alphabet appears after a digit.
            if been_through_digit:
                return False

    if numeric_part != "" and numeric_part[0] == '0':
        return False

    return True


if __name__ == "__main__":
    main()
