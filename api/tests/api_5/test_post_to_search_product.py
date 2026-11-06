import requests


def test_post_to_search_product(base_url):
    response = requests.post(
        f"{base_url}/searchProduct", data={"search_product": "tshirt"}, timeout=10
    )

    data = response.json()

    assert response.status_code == 200
    assert data["responseCode"] == 200
    assert len(data["products"]) > 0

    for item in data["products"]:
        assert item["category"]["category"] == "Tshirts"
