import pytest
import requests

from config import BASE_URL_API
from test_data import generate_user_data

AD_DOMAINS = (
    "googlesyndication.com",
    "doubleclick.net",
    "googleadservices.com",
    "adservice.google.com",
)


@pytest.fixture
def new_user():
    return generate_user_data()


@pytest.fixture
def registered_user(new_user):
    response = requests.post(f"{BASE_URL_API}/createAccount", data=new_user, timeout=10)

    assert response.status_code == 200

    data = response.json()

    assert data["responseCode"] == 201

    yield new_user

    requests.delete(
        f"{BASE_URL_API}/deleteAccount",
        data={"email": new_user["email"], "password": new_user["password"]},
        timeout=10,
    )


@pytest.fixture(autouse=True)
def block_ads(page):
    def handle_route(route):
        if any(domain in route.request.url for domain in AD_DOMAINS):
            route.abort()
        else:
            route.continue_()

    page.route("**/*", handle_route)
