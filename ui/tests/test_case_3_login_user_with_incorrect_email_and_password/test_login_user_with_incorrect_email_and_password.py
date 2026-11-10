import allure

from ui.pages.home_page import HomePage
from ui.pages.login_page import LoginPage
from ui.base_test import BaseUITest


@allure.story("Login")
class TestLoginUserWithInvalidData(BaseUITest):
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Test Case 3: Login User with incorrect email and password")
    def test_login_user_with_incorrect_email_and_password(self, page):
        home_page = HomePage(page)
        login_page = LoginPage(page)

        with allure.step("Navigate to url"):
            home_page.open()
        with allure.step("Verify that home page is visible successfully"):
            home_page.home_page_is_visible()
        with allure.step("Click on 'Signup / Login' button"):
            home_page.click_signup_login_link()

        with allure.step("Verify 'Login to your account' is visible"):
            login_page.login_message_is_visible()
        with allure.step("Enter incorrect email address and password"):
            login_page.fill_email_and_password_fields(
                email="incorrect@example.com", password="Incorrectpass"
            )
        with allure.step("Click 'login' button"):
            login_page.click_login_button()
        with allure.step(
            "Verify error 'Your email or password is incorrect!' is visible"
        ):
            login_page.incorrect_login_text_is_visible()
