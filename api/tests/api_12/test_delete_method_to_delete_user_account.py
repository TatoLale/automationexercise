import requests


def test_delete_method_to_delete_user_account(base_url, create_user):
    response = requests.delete(
        f"{base_url}/deleteAccount", data=create_user, timeout=10
    )

    data = response.json()

    assert response.status_code == 200
    assert data["responseCode"] == 200
    assert data["message"] == "Account deleted!"
