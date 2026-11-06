import pytest
import requests

from config import BASE_URL_API, EMAIL, PASSWORD
from api.test_data import generate_user_data


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

    response = requests.delete(
        f"{base_url}/deleteAccount",
        data={"email": user_details["email"], "password": user_details["password"]},
        timeout=10,
    )

    data = response.json()

    assert data["responseCode"] == 200
    assert data["message"] == "Account deleted!"


@pytest.fixture
def create_user(base_url):
    user = generate_user_data()

    response = requests.post(f"{base_url}/createAccount", data=user, timeout=10)

    response_data = response.json()

    assert response_data["message"] == "User created!"

    data = {"email": user["email"], "password": user["password"]}

    return data


@pytest.fixture
def update_user(base_url):
    user = generate_user_data()

    create_response = requests.post(f"{base_url}/createAccount", data=user, timeout=10)

    create_response_data = create_response.json()

    assert create_response_data["message"] == "User created!"

    yield user

    delete_response = requests.delete(
        f"{base_url}/deleteAccount",
        data={"email": user["email"], "password": user["password"]},
        timeout=10,
    )

    delete_response_data = delete_response.json()

    assert delete_response_data["responseCode"] == 200
    assert delete_response_data["message"] == "Account deleted!"
