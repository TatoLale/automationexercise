import requests


def test_put_method_to_update_user_account(base_url, update_user):
    update_user["name"] = "TestUpdateName"

    response = requests.put(f"{base_url}/updateAccount", data=update_user, timeout=10)

    data = response.json()

    assert response.status_code == 200
    assert data["responseCode"] == 200
    assert data["message"] == "User updated!"

    get_response = requests.get(f"{base_url}/getUserDetailByEmail",
        params={"email": update_user["email"]},
        timeout=10,
    )

    get_data = get_response.json()

    assert get_data["user"]["name"] == "TestUpdateName"