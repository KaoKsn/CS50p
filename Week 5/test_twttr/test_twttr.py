from twttr import shorten
from string import punctuation


def main():
    test_mixed()
    test_numbers()
    test_specialchars()


def test_lower():
    assert shorten("twitter") == "twttr"


def test_mixed():
    assert shorten("AeiOu") == ""
    assert shorten("Twi TtEr") == "Tw Ttr"
    assert shorten("CS50P") == "CS50P"
    assert shorten("") == ""
    assert shorten("cs") == "cs"


def test_numbers():
    assert shorten("0") == "0"
    assert shorten("1.02") == "1.02"
    assert shorten("Ivp101") == "vp101"


def test_specialchars():
    assert shorten(punctuation) == punctuation


if __name__ == "__main__":
    main()
