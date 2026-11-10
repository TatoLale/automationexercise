import requests
import allure

from api.base_test import BaseApiTest


@allure.story("Login")
class TestLoginWithInvalidDetails(BaseApiTest):
    @allure.title("API 10: Verify login with invalid details")
    def test_post_to_verify_login_with_invalid_details(
        self, base_url, login_credentials
    ):
        response = requests.post(
            f"{base_url}/verifyLogin",
            data={
                "email": login_credentials["email"],
                "password": "sdwadsd",
            },
            timeout=10,
        )

        assert response.status_code == 200

        data = response.json()

        assert data["responseCode"] == 404
        assert data["message"] == "User not found!"
