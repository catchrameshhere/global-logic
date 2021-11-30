import pytest


@pytest.mark.parametrize("num1, num2, output", [(1, 2, 3), (5, 5, 10), (10, 20, 30), (20, 20, 50)])
def test_add(num1, num2, output):
    print("num1 = {}, num2 = {}, output = {}".format(num1, num2, output))
    assert num1+num2 == output

