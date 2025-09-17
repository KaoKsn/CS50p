from jar import Jar
import pytest

def main():
    test_init()
    test_str()
    test_deposit()
    test_withdraw()


# Test if jar handles constructor calls.
def test_init():
    with pytest.raises(ValueError):
        Jar(-3)
    
    jar_1 = Jar()
    assert jar_1.capacity == 12
    assert jar_1.size == 0

    jar_2 = Jar(20)
    assert jar_2.capacity == 20
    assert jar_2.size == 0


def test_str():
    # Ensure str prints the correct size of the jar.
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(6)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪"
    jar.withdraw(2)
    assert str(jar) == "🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(14)
    with pytest.raises(ValueError):
        jar.deposit(15)


def test_withdraw():
    jar = Jar(3)
    jar.deposit(2)
    with pytest.raises(ValueError):
        jar.withdraw(3)


if __name__ == "__main__":
    main()
