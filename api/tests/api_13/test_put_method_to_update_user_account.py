import requests
import allure

from api.base_test import BaseApiTest


@allure.story("Account")
class TestUpdateUserAccount(BaseApiTest):
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("API 13: Verify updating user account")
    def test_put_method_to_update_user_account(self, base_url, update_user):
        update_user["name"] = "TestUpdateName"

        response = requests.put(
            f"{base_url}/updateAccount", data=update_user, timeout=10
        )

        assert response.status_code == 200

        data = response.json()

        assert data["responseCode"] == 200
        assert data["message"] == "User updated!"

        get_response = requests.get(
            f"{base_url}/getUserDetailByEmail",
            params={"email": update_user["email"]},
            timeout=10,
        )

        assert get_response.status_code == 200

        get_data = get_response.json()

        assert get_data["user"]["name"] == "TestUpdateName"
