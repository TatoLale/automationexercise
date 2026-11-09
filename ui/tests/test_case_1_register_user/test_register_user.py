import allure

from ui.pages.home_page import HomePage
from ui.base_test import BaseUITest


@allure.story("Register")
class TestRegisterUser(BaseUITest):
    @allure.title("Verify registering user")
    def test_register_user(self, page):
        home_page = HomePage(page)

        home_page.open()
        home_page.home_page_is_visible()
        home_page.click_signup_login_button_and_is_visible()
        home_page.fill_name_and_email_fields_and_click_signup(
            name="GSDS", email="GHSD@gmail.com"
        )
