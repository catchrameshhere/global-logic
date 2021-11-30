import pytest


@pytest.fixture
def create_user():
    user = "elaine"
    yield user
    print("user deleted successfully")