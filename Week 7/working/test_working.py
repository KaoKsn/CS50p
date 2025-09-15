from working import convert
import pytest


def main():
    test_standard()
    test_12()
    test_invalid()
    test_edge()


def test_standard():
    assert convert("5:00 AM to 9:00 AM") == "05:00 to 09:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:00 PM to 11:59 PM") == "21:00 to 23:59"
    assert convert("6 AM to 9 PM") == "06:00 to 21:00"
    assert convert("8 PM to 11:59 PM") == "20:00 to 23:59"
    assert convert("9:30 PM to 11 PM") == "21:30 to 23:00"


def test_12():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12:59 AM to 12:10 PM") == "00:59 to 12:10"
    assert convert("12:40 AM to 12 PM") == "00:40 to 12:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"


def test_invalid():
    with pytest.raises(ValueError):
        convert("12:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("18:00 AM to 13:00 PM")


def test_edge():
    with pytest.raises(ValueError):
        convert("05:00 AM to 9:00 PM")
    with pytest.raises(ValueError):
        convert(" to ")
    with pytest.raises(ValueError):
        convert("5:00 AM 9:00 PM")


if __name__ == "__main__":
    main()
