import requests
import allure

from api.base_test import BaseApiTest


@allure.story("Login")
class TestDeleteLogin(BaseApiTest):
    @allure.title("API 9: Verify deleting login” sounds like deleting a login. Something like “DELETE to verify login is not supported")
    def test_delete_to_verify_login(self, base_url):
        response = requests.delete(f"{base_url}/verifyLogin", timeout=10)

        data = response.json()

        assert response.status_code == 200
        assert data["responseCode"] == 405
        assert data["message"] == "This request method is not supported."
