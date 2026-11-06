import requests


def test_get_all_brands_list(base_url):
    response = requests.get(f"{base_url}/brandsList", timeout=10)

    data = response.json()

    assert response.status_code == 200
    assert data["responseCode"] == 200
    assert len(data["brands"]) > 0

    for item in data["brands"]:
        assert "id" in item
        assert "brand" in item
        assert isinstance(item["id"], int)
        assert isinstance(item["brand"], str)
        assert item["brand"] != ""
