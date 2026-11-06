import requests


def test_get_all_products_list(base_url):
    response = requests.get(f"{base_url}/productsList", timeout=10)

    assert response.status_code == 200

    data = response.json()

    assert response.status_code == 200
    assert data["responseCode"] == 200
    assert len(data["products"]) > 0
