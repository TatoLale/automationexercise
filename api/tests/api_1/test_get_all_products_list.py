import requests
import allure

from api.base_test import BaseApiTest


@allure.story("Products")
class TestAllProductsList(BaseApiTest):
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("API 1: Get all products list")
    def test_get_all_products_list(self, base_url):
        response = requests.get(f"{base_url}/productsList", timeout=10)

        assert response.status_code == 200

        data = response.json()

        assert data["responseCode"] == 200
        assert len(data["products"]) > 0
