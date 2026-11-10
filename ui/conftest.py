import pytest

from test_data import generate_user_data


@pytest.fixture
def new_user():
    return generate_user_data()
