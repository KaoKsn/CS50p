from plates import is_valid


def main():
    test_valid_plates()
    test_numbers_inbetween()
    test_plate_length()
    test_not_starting_with_alphabets()
    test_has_punctuations()
    test_numeric_part_startWith_0()
    test_edge_cases()


def test_valid_plates():
    case_strings = [" CS50 ", "AbxYzR ", "xC ", "Hi555"]
    for s in case_strings:
        assert is_valid(s) == True


def test_numbers_inbetween():
    case_strings = [" Cs50p ", "Ki5xy "]
    for s in case_strings:
        assert is_valid(s) == False


def test_plate_length():
    case_strings = ["A ", "Namaste"]
    for s in case_strings:
        assert is_valid(s) == False


def test_not_starting_with_alphabets():
    case_strings = [" 1CS50 ", " C250", " 12CSP"]
    for s in case_strings:
        assert is_valid(s) == False


def test_has_punctuations():
    case_strings = ["  CS-50 ", "!C250", "12CSP&  "]
    for s in case_strings:
        assert is_valid(s) == False


def test_numeric_part_startWith_0():
    assert is_valid(" CS025") == False


def test_edge_cases():
    case_strings = [" ", ""]
    for s in case_strings:
        assert is_valid(s) == False


if __name__ == "__main__":
    main()
