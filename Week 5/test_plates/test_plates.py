from plates import is_valid

'''
Their version of plates.py doesn't accept:
       1. Trailing and leading whitespaces.
       2. Doesn't handle inputs like "", " ".
'''


def main():
    test_valid_plates()
    test_numbers_inbetween()
    test_plate_length()
    test_not_starting_with_alphabets()
    test_has_punctuations()
    test_numeric_part_startWith_0()


def test_valid_plates():
    case_strings = ["CS50", "AbxYzR", "xC", "Hi555"]
    for s in case_strings:
        assert is_valid(s) == True


def test_numbers_inbetween():
    case_strings = ["Cs50p", "Ki5xy"]
    for s in case_strings:
        assert is_valid(s) == False


def test_plate_length():
    case_strings = ["A", "Namaste"]
    for s in case_strings:
        assert is_valid(s) == False


def test_not_starting_with_alphabets():
    case_strings = ["1CS50", "C250", "12CSP"]
    for s in case_strings:
        assert is_valid(s) == False


def test_has_punctuations():
    case_strings = ["CS-50", "!C250", "12CSP&"]
    for s in case_strings:
        assert is_valid(s) == False


def test_numeric_part_startWith_0():
    case_strings = ["CS025", "CSS02", "CSSx0", "CSRxY0", "CxYAz0"]
    for s in case_strings:
        assert is_valid(s) == False


if __name__ == "__main__":
    main()
