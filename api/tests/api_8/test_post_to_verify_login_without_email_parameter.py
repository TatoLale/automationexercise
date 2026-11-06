import requests


def test_post_to_verify_login_without_email_parameter(base_url, login_credentials):
    response = requests.post(
        f"{base_url}/verifyLogin", data={"password": login_credentials["password"]}, timeout=10
    )

    data = response.json()

    assert response.status_code == 200
    assert data["responseCode"] == 400
    assert (
        data["message"]
        == "Bad request, email or password parameter is missing in POST request."
    )
