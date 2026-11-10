import requests
import allure

from api.base_test import BaseApiTest


@allure.story("Login")
class TestLoginWithoutEmail(BaseApiTest):
    @allure.severity(allure.severity_level.MINOR)
    @allure.title("API 8: Verify login without email parameter")
    def test_post_to_verify_login_without_email_parameter(
        self, base_url, login_credentials
    ):
        response = requests.post(
            f"{base_url}/verifyLogin",
            data={"password": login_credentials["password"]},
            timeout=10,
        )

        assert response.status_code == 200

        data = response.json()

        assert data["responseCode"] == 400
        assert (
            data["message"]
            == "Bad request, email or password parameter is missing in POST request."
        )
