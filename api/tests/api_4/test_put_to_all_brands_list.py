import requests
import allure

from api.base_test import BaseApiTest


@allure.story("Brands")
class TestPutAllBrandsList(BaseApiTest):
    @allure.title("PUT to brands list is not supported")
    def test_put_to_all_brands_list(self, base_url):
        response = requests.put(f"{base_url}/brandsList", timeout=10)

        data = response.json()

        assert response.status_code == 200
        assert data["responseCode"] == 405
        assert data["message"] == "This request method is not supported."
