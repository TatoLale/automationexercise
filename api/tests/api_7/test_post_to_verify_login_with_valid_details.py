import requests
import allure

from api.base_test import BaseApiTest


@allure.story("Login")
class TestLoginWithValidDetails(BaseApiTest):
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("API 7: Verify login with valid details")
    def test_post_to_verify_login_with_valid_details(self, base_url, login_credentials):
        response = requests.post(
            f"{base_url}/verifyLogin",
            data=login_credentials,
            timeout=10,
        )

        assert response.status_code == 200

        data = response.json()

        assert data["responseCode"] == 200
        assert data["message"] == "User exists!"
