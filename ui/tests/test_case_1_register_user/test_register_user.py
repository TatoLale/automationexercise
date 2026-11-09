import allure

from ui.pages.register_page import RegisterPage
from ui.base_test import BaseUITest


@allure.story("Register")
class TestRegisterUser(BaseUITest):
    @allure.title("Verify registering user")
    def test_register_user(self, page):
        register_page = RegisterPage(page)

        with allure.step("Navigate to url"):
            register_page.open()
        with allure.step("Verify that home page is visible successfully"):
            register_page.home_page_is_visible()
        with allure.step("Click on 'Signup / Login' button"):
            register_page.click_signup_login_link_button()
        with allure.step("Verify 'New User Signup!' is visible"):
            register_page.singup_message_is_visible()
        with allure.step("Enter name and email address"):
            register_page.fill_name_and_email_fields(
                name="GSDS", email="GHSD@gmail.com"
            )
        with allure.step("Click 'Signup' button"):
            register_page.click_signup_button()
        with allure.step("Verify that 'ENTER ACCOUNT INFORMATION' is visible"):
            register_page.enter_account_information_is_visible()
        with allure.step("Fill details: Title, Name, Email, Password, Date of birth"):
            pass
