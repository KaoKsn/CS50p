from numb3rs import validate

'''
    cs50p's version of validate() in numb3rs.py returns boolean True/False.
    Failing to comply with this leads to a return value of 1.
'''


def main():
    test_standard()
    test_4_bytes()
    test_leading_zeroes()
    test_out_of_bound()
    test_zero()
    test_v6()
    test_strings()


def test_standard():
    assert validate("127.0.0.1") == True
    assert validate("101.1.90.209") == True
    assert validate("255.249.233.209") == True


def test_4_bytes():
    assert validate("90.1.90.1209") == False
    assert validate("20.1000.90.209") == False


def test_leading_zeroes():
    assert validate("101.8.90.001") == False
    assert validate("19.09.21.10") == False
    assert validate("255.019.83.70") == False


def test_out_of_bound():
    assert validate("101.3.90.256") == False


def test_zero():
    assert validate("0.1.9.205") == True
    assert validate("0.0.0.0") == True


def test_strings():
    assert validate("string") == False
    assert validate("1.1.1.1a") == False


def test_v6():
    assert validate("2001:9db0:32:0000:5cd0:3212") == False


if __name__ == "__main__":
    main()
