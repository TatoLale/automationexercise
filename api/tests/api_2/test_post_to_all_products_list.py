import requests


def test_post_to_all_products_list(base_url):
    response = requests.post(f"{base_url}/productsList", timeout=10)

    data = response.json()

    assert response.status_code == 200
    assert data["responseCode"] == 405
    assert data["message"] == "This request method is not supported."
