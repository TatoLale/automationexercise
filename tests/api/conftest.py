import pytest
import requests

from src.config import BASE_URL_API, EMAIL, PASSWORD
from src.test_data import generate_user_data


@pytest.fixture
def base_url():
    return BASE_URL_API


@pytest.fixture
def login_credentials():
    login_credentials = {"email": EMAIL, "password": PASSWORD}
    return login_credentials


@pytest.fixture
def delete_user(base_url):
    user_details = generate_user_data()

    yield user_details

    requests.delete(
        f"{base_url}/deleteAccount",
        data={"email": user_details["email"], "password": user_details["password"]},
        timeout=10,
    )


@pytest.fixture
def create_user(base_url):
    user = generate_user_data()

    response = requests.post(f"{base_url}/createAccount", data=user, timeout=10)

    assert response.status_code == 200

    response_data = response.json()

    assert response_data["message"] == "User created!"

    data = {"email": user["email"], "password": user["password"]}

    return data


@pytest.fixture
def update_user(base_url):
    user = generate_user_data()

    create_response = requests.post(f"{base_url}/createAccount", data=user, timeout=10)

    assert create_response.status_code == 200

    create_response_data = create_response.json()

    assert create_response_data["message"] == "User created!"

    yield user

    requests.delete(
        f"{base_url}/deleteAccount",
        data={"email": user["email"], "password": user["password"]},
        timeout=10,
    )
