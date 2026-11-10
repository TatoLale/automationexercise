import requests
import allure

from api.base_test import BaseApiTest


@allure.story("Products")
class TestSearchProductWithoutParameter(BaseApiTest):
    @allure.title("API 6: Search product without search_product parameter")
    def test_post_to_search_product_without_search_product_parameter(self, base_url):
        response = requests.post(f"{base_url}/searchProduct", timeout=10)

        assert response.status_code == 200

        data = response.json()

        assert data["responseCode"] == 400
        assert (
            data["message"]
            == "Bad request, search_product parameter is missing in POST request."
        )
