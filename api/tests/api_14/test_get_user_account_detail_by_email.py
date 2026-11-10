import requests
import allure

from api.base_test import BaseApiTest


@allure.story("Account")
class TestAccountDetailByEmail(BaseApiTest):
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("API 14: Verify to get account detail by email")
    def test_get_user_account_detail_by_email(self, base_url, update_user):
        response = requests.get(
            f"{base_url}/getUserDetailByEmail",
            params={"email": update_user["email"]},
            timeout=10,
        )

        assert response.status_code == 200

        data = response.json()

        assert data["responseCode"] == 200
        assert data["user"]["email"] == update_user["email"]
        assert data["user"]["name"] == update_user["name"]
