import allure

from ui.pages.home_page import HomePage
from ui.pages.login_page import LoginPage
from ui.base_test import BaseUITest


@allure.story("Login")
class TestLoginUserWithValidData(BaseUITest):
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Test Case 2: Login User with correct email and password")
    def test_login_user_with_correct_email_and_password(self, page, registered_user):
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
        with allure.step("Enter correct email address and password"):
            login_page.fill_email_and_password_fields(
                email=registered_user["email"], password=registered_user["password"]
            )
        with allure.step("Click 'login' button"):
            login_page.click_login_button()

        with allure.step("Verify that 'Logged in as username' is visible"):
            home_page.logged_in_as_username_is_visible(name=registered_user["name"])
        with allure.step("Click 'Delete Account' button"):
            home_page.click_delete_account_button()
        with allure.step("Verify that 'ACCOUNT DELETED!' is visible"):
            home_page.account_delete_confirmation_is_visible()
