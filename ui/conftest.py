import pytest
import requests


from config import BASE_URL_API
from test_data import generate_user_data
from ui.pages.home_page import HomePage
from ui.pages.login_page import LoginPage
from ui.pages.signup_page import SignUpPage


@pytest.fixture
def new_user():
    return generate_user_data()


@pytest.fixture
def registered_user(page, new_user):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    signup_page = SignUpPage(page)

    home_page.open()
    home_page.home_page_is_visible()
    home_page.click_signup_login_link()
    login_page.signup_message_is_visible()
    login_page.fill_name_and_email_fields(
        name=new_user["name"], email=new_user["email"]
    )
    login_page.click_signup_button()
    signup_page.enter_account_information_is_visible()
    signup_page.fill_account_information(
        password=new_user["password"],
        days=new_user["birth_date"],
        months=new_user["birth_month"],
        years=new_user["birth_year"],
    )
    signup_page.check_sign_up_for_newsletter()
    signup_page.check_special_offers()
    signup_page.fill_address_information(
        first_name=new_user["firstname"],
        last_name=new_user["lastname"],
        company=new_user["company"],
        address_1=new_user["address1"],
        address_2=new_user["address2"],
        country=new_user["country"],
        state=new_user["state"],
        city=new_user["city"],
        zipcode=new_user["zipcode"],
        mobile_number=new_user["mobile_number"],
    )
    signup_page.click_create_account_button()
    signup_page.account_created_text_is_visible()
    signup_page.click_continue_button()
    home_page.click_logout_button()

    yield new_user

    requests.delete(
        f"{BASE_URL_API}/deleteAccount",
        data={"email": new_user["email"], "password": new_user["password"]},
        timeout=10,
    )
