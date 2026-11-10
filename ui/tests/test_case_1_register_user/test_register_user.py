import allure

from ui.pages.home_page import HomePage
from ui.pages.login_page import LoginPage
from ui.pages.signup_page import SignUpPage
from ui.base_test import BaseUITest


@allure.story("Register")
class TestRegisterUser(BaseUITest):
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Test Case 1: Register user")
    def test_register_user(self, page, new_user):
        home_page = HomePage(page)
        login_page = LoginPage(page)
        signup_page = SignUpPage(page)

        with allure.step("Navigate to url"):
            home_page.open()
        with allure.step("Verify that home page is visible successfully"):
            home_page.home_page_is_visible()
        with allure.step("Click on 'Signup / Login' button"):
            home_page.click_signup_login_link()

        with allure.step("Verify 'New User Signup!' is visible"):
            login_page.signup_message_is_visible()
        with allure.step("Enter name and email address"):
            login_page.fill_name_and_email_fields(
                name=new_user["name"], email=new_user["email"]
            )
        with allure.step("Click 'Signup' button"):
            login_page.click_signup_button()

        with allure.step("Verify that 'ENTER ACCOUNT INFORMATION' is visible"):
            signup_page.enter_account_information_is_visible()
        with allure.step("Fill details: Title, Name, Email, Password, Date of birth"):
            signup_page.fill_account_information(
                password=new_user["password"],
                days=new_user["birth_date"],
                months=new_user["birth_month"],
                years=new_user["birth_year"],
            )
        with allure.step("Select checkbox 'Sign up for our newsletter!'"):
            signup_page.check_sign_up_for_newsletter()
        with allure.step("Select checkbox 'Receive special offers from our partners!'"):
            signup_page.check_special_offers()
        with allure.step(
            "Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number"
        ):
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
        with allure.step("Click 'Create Account button'"):
            signup_page.click_create_account_button()
        with allure.step("Verify that 'ACCOUNT CREATED!' is visible"):
            signup_page.account_created_text_is_visible()
        with allure.step("Click 'Continue' button"):
            signup_page.click_continue_button()

        with allure.step("Verify that 'Logged in as username' is visible"):
            home_page.logged_in_as_username_is_visible(name=new_user["name"])
        with allure.step("Click 'Delete Account' button"):
            home_page.click_delete_account_button()
        with allure.step(
            "Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button"
        ):
            home_page.account_delete_confirmation_is_visible()
