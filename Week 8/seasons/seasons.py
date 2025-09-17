from datetime import date
import sys
import inflect


def main():
    dob = input("Date of Birth: ").strip()

    # YYYY-MM-DD format.
    dob = verify_dob(dob)

    # Print minutes in words, since 00:00 on DOB and 00:00 today.
    inflector = inflect.engine()
    minutes_in_words = inflector.number_to_words(minutes_elapsed_since(dob), andword = "") + " minutes"
    print(minutes_in_words.capitalize())

def verify_dob(dob):
    try:
        dob = date.fromisoformat(dob)
    except ValueError as msg:
        print("Format: YYYY-MM-DD")
        sys.exit(msg)

    return dob


def minutes_elapsed_since(dob):
    today = date.today()

    if (today-dob).days < 0:
        sys.exit("Date from future!")

    # "-" overloaded in module datetime.
    return (today - dob).days * 24 * 60


if __name__ == "__main__":
    main()
