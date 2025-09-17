from seasons import verify_dob, minutes_elapsed_since
import pytest
from datetime import date


def main():
    test_standard()
    test_invalid()
    test_future()

def test_standard():
    assert verify_dob("2025-09-16") == date(2025,9,16)


def test_invalid():
    date_list = ["2025-9-16", " ", "2025/09/16", "20/09/2002", "2024-14-23", "2024-11-31", "17"]
    for value in date_list:
        with pytest.raises(SystemExit):
            verify_dob(value)


def test_future():
    # Generate a future time.
    today = date.today()
    i = 1
    while True:
        try:
            future_date = date(today.year + i, today.month, today.day)
        except ValueError:
            i += 1
            continue
        else:
            break

    with pytest.raises(SystemExit):
        minutes_elapsed_since(future_date)


if __name__ == "__main__":
    main()
