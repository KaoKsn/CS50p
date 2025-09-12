from fuel import convert, gauge
import pytest


''' test_fuel.py implementation of fuel.py in the pset{cs50p's version} '''


def main():
    test_division_by_0()
    test_negative_fractions()
    test_strings()
    test_improper_fractions()
    test_percent_to_int()

    test_empty()
    test_partial_guage()
    test_full()


# Test convert().
def test_division_by_0():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")


def test_negative_fractions():
    # Although, -2/-3 is mathematically valid, the pset states " each of X and Y are positive integers " and, cs50p's fuel.py doesn't handle it.
    case_strings = ["-3/5", "2/-3"]
    for s in case_strings:
        with pytest.raises(ValueError):
            convert(s)


def test_strings():
    case_strings = ["cat/1", "cat/dog", "1/cat"]
    for s in case_strings:
        with pytest.raises(ValueError):
            convert(s)


def test_improper_fractions():
    with pytest.raises(ValueError):
        convert("6/5")


def test_percent_to_int():
    assert convert("2/3") == 67


# Test guage().
def test_empty():
    guage_values = [1, 0]
    for value in guage_values:
        assert gauge(value) == "E"


def test_partial_guage():
    guage_values = [2, 98, 50]
    for value in guage_values:
        assert gauge(value) == f"{value}%"


def test_full():
    guage_values = [99, 100]
    for value in guage_values:
        assert gauge(value) == "F"


if __name__ == "__main__":
    main()
