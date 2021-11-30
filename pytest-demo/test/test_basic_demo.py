import pytest


def test_add():
    a = 5
    b = 10
    result = a + b
    assert (result == 15) # to validate the test conditions


@pytest.mark.regression
def test_mul():
    a = 7
    assert (a * a) == 49
