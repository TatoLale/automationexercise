import requests


def test_post_to_search_product_without_search_product_parameter(base_url):
    response = requests.post(f"{base_url}/searchProduct", timeout=10)

    data = response.json()

    assert response.status_code == 200
    assert data["responseCode"] == 400
    assert (
        data["message"]
        == "Bad request, search_product parameter is missing in POST request."
    )
