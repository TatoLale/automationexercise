import requests


def test_post_to_verify_login_with_valid_details(base_url, login_credentials):
    response = requests.post(
        f"{base_url}/verifyLogin",
        data=login_credentials,
        timeout=10,
    )

    data = response.json()

    assert response.status_code == 200
    assert data["responseCode"] == 200
    assert data["message"] == "User exists!"
