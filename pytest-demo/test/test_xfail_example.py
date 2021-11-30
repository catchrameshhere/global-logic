import pytest


def test_add1():
    a = 5
    b = 10
    assert (a+b) == 15


# @pytest.mark.xfail(run=False)
# @pytest.mark.xfail(strict=True)
@pytest.mark.xfail
def test_add2():
    a = 5
    b = 10
    assert (a+b) != 15
