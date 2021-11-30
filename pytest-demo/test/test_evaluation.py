import pytest


def test_add_two_numbers():
    a = 5
    b = 10
    result = a + b
    assert result == 15


def test_add_three_numbers():
    a = 5
    b = 10
    c = 15
    result = a + b + c
    assert result == 30
