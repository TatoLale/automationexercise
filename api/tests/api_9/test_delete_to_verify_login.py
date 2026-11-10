import requests
import allure

from api.base_test import BaseApiTest


@allure.story("Login")
class TestDeleteLogin(BaseApiTest):
    @allure.title("API 9: DELETE to verify login is not supported")
    def test_delete_to_verify_login(self, base_url):
        response = requests.delete(f"{base_url}/verifyLogin", timeout=10)

        assert response.status_code == 200

        data = response.json()

        assert data["responseCode"] == 405
        assert data["message"] == "This request method is not supported."
