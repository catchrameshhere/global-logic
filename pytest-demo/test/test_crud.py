import pytest


def create_user():
    user = "ramesh"
    yield user
    delete_user(user)


def delete_user():
    pass


def test_create_user():
    user = create_user()
    # print("'user used is = {}'".format(user))
    assert False
