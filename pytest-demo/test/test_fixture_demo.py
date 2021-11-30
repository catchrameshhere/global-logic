import pytest


# @pytest.fixture
# def create_user():
#     user = "dan"
#     yield user
#     print("user deleted successfully")


def test_update_user(create_user):
    u1 = create_user
    print("user = {}".format(u1))
