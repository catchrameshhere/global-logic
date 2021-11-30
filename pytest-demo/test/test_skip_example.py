import pytest

d = 11


def test_add1():
    a = 5
    b = 10
    assert (a+b) == 15


@pytest.mark.skip(reason="Bug number = 12345")
def test_add2():
    a = 5
    b = 10
    assert (a+b) != 15


@pytest.mark.skipif(d == 10, reason="d is 10")
def test_add3():
    a = 5
    b = 10
    assert (a+b) == 15
