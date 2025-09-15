from um import count
import pytest


def main():
    test_standard()
    test_case_insensitivity()
    test_edge()


def test_standard():
    assert count("um") == 1
    assert count("  um") == 1
    assert count("This is a simple ,um, um... tree") == 2


def test_case_insensitivity():
    assert count("Um") == 1


def test_inbetween_words():
    assert count("Yum.. Yummy, um") == 1


def test_edge():
    assert count("") == 0
    assert count(" ") == 0
    assert count("Umm") == 0

if __name__ == "__main__":
    main()
