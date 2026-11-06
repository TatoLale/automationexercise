import requests


def test_get_user_account_detail_by_email(base_url, update_user):
    response = requests.get(
        f"{base_url}/getUserDetailByEmail",
        params={"email": update_user["email"]},
        timeout=10,
    )

    data = response.json()

    assert response.status_code == 200
    assert data["responseCode"] == 200
    assert data["user"]["email"] == update_user["email"]
    assert data["user"]["name"] == update_user["name"]
