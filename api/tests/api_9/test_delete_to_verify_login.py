import requests


def test_delete_to_verify_login(base_url):
    response = requests.delete(f"{base_url}/verifyLogin", timeout=10)

    data = response.json()

    assert response.status_code == 200
    assert data["responseCode"] == 405
    assert data["message"] == "This request method is not supported."
