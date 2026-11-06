import requests


def test_post_to_verify_login_with_invalid_details(base_url, login_credentials):
    response = requests.post(
        f"{base_url}/verifyLogin",
        data={
            "email": login_credentials["email"],
            "password": "sdwadsd",
        },
        timeout=10,
    )

    data = response.json()

    assert response.status_code == 200
    assert data["responseCode"] == 404
    assert data["message"] == "User not found!"
