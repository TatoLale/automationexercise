import allure

from ui.pages.home_page import HomePage
from ui.pages.login_page import LoginPage
from ui.base_test import BaseUITest


@allure.story("Register")
class TestRegisterUserWithExistingEmail(BaseUITest):
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test Case 5: Register User with existing email")
    def test_register_user_with_existing_email(self, page, registered_user):
        home_page = HomePage(page)
        login_page = LoginPage(page)

        with allure.step("Navigate to url"):
            home_page.open()
        with allure.step("Verify that home page is visible successfully"):
            home_page.home_page_is_visible()
        with allure.step("Click on 'Signup / Login' button"):
            home_page.click_signup_login_link()

        with allure.step("Verify 'New User Signup!' is visible"):
            login_page.signup_message_is_visible()
        with allure.step("Enter name and already registered email address"):
            login_page.fill_name_and_email_fields(
                name=registered_user["name"], email=registered_user["email"]
            )
        with allure.step("Click 'Signup' button"):
            login_page.click_signup_button()
        with allure.step("Verify error 'Email Address already exist!' is visible"):
            login_page.email_already_exist_text_is_visible()
