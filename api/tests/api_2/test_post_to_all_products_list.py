import requests
import allure

from api.base_test import BaseApiTest


@allure.story("Products")
class TestPostAllProductsList(BaseApiTest):
    @allure.title("API 2: POST to products list is not supported")
    def test_post_to_all_products_list(self, base_url):
        response = requests.post(f"{base_url}/productsList", timeout=10)

        data = response.json()

        assert response.status_code == 200
        assert data["responseCode"] == 405
        assert data["message"] == "This request method is not supported."
