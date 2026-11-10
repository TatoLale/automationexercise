import requests
import allure

from api.base_test import BaseApiTest


@allure.story("Brands")
class TestAllBrandsList(BaseApiTest):
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("API 3: Get all brands list")
    def test_get_all_brands_list(self, base_url):
        response = requests.get(f"{base_url}/brandsList", timeout=10)

        assert response.status_code == 200

        data = response.json()

        assert data["responseCode"] == 200
        assert len(data["brands"]) > 0

        for item in data["brands"]:
            assert "id" in item
            assert "brand" in item
            assert isinstance(item["id"], int)
            assert isinstance(item["brand"], str)
            assert item["brand"] != ""
