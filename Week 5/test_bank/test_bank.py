from bank import value


def main():
    test_no_payback()
    test_partial_payback()
    test_complete_payback()
#   test_edge_cases()


def test_no_payback():
    case_strings = ["Hello Sir  ", "hello Sir ", "hello ", "HelLo"]
    for s in case_strings:
        assert value(s) == 0


def test_partial_payback():
    case_strings = ["Hey Sir  ", "hoWdy Sir ", "hEylo ", "Hide"]
    for s in case_strings:
        assert value(s) == 20

def test_complete_payback():
    case_strings = ["What's up? ", "Namaste  ", "0 ", "123 x"]
    for s in case_strings:
        assert value(s) == 100


'''
def test_edge_cases():
    case_strings = [" ", ""]
    for s in case_strings:
        assert value(s) == None
'''


if __name__ == "__main__":
    main()
