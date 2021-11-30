import pytest


@pytest.mark.skip(reason="inbox module is not developed")
class TestInbox:

    def test_add1(self):
        a = 5
        b = 10
        assert (a+b) == 15

    def test_add2(self):
        a = 5
        b = 10
        assert (a+b) == 15

