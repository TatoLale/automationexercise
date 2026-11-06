import requests


def test_post_to_create_register_user_account(base_url, delete_user):

    response = requests.post(f"{base_url}/createAccount", data=delete_user, timeout=10)

    data = response.json()

    assert response.status_code == 200
    assert data["responseCode"] == 201
    assert data["message"] == "User created!"
