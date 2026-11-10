import requests
import allure

from api.base_test import BaseApiTest


@allure.story("Account")
class TestDeleteUserAccount(BaseApiTest):
    @allure.title("API 12: Verify deleting user account")
    def test_delete_method_to_delete_user_account(self, base_url, create_user):
        response = requests.delete(
            f"{base_url}/deleteAccount", data=create_user, timeout=10
        )

        assert response.status_code == 200

        data = response.json()

        assert data["responseCode"] == 200
        assert data["message"] == "Account deleted!"
