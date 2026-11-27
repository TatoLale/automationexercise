import allure

from src.pages.home_page import HomePage
from src.pages.cart_page import CartPage
from src.pages.login_page import LoginPage
from src.pages.signup_page import SignUpPage
from src.pages.account_created_page import AccountCreatedPage
from src.pages.checkout_page import CheckoutPage
from src.pages.account_deleted_page import AccountDeletedPage
from tests.ui.base_test import BaseUITest


@allure.story("Place Order")
class TestVerifyAddressDetailsInCheckoutPage(BaseUITest):
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test Case 23: Verify address details in checkout page")
    def test_verify_address_details_in_checkout_page(self, page, new_user):
        home_page = HomePage(page)
        cart_page = CartPage(page)
        login_page = LoginPage(page)
        signup_page = SignUpPage(page)
        account_created_page = AccountCreatedPage(page)
        checkout_page = CheckoutPage(page)
        account_deleted_page = AccountDeletedPage(page)

        with allure.step("Navigate to url"):
            home_page.open()
        with allure.step("Verify that home page is visible successfully"):
            home_page.home_page_is_visible()
        with allure.step("Click 'Signup / Login' button"):
            home_page.header.click_signup_login_link()
        with allure.step("Fill all details in Signup and create account"):
            login_page.fill_name_and_email_fields(
                name=new_user["name"], email=new_user["email"]
            )
            login_page.click_signup_button()

            signup_page.fill_account_information(
                password=new_user["password"],
                days=new_user["birth_date"],
                months=new_user["birth_month"],
                years=new_user["birth_year"],
            )
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

        with allure.step("Verify 'ACCOUNT CREATED!' and click 'Continue' button"):
            account_created_page.account_created_text_is_visible()
            account_created_page.click_continue_button()

        with allure.step("Verify 'Logged in as username' at top"):
            home_page.header.logged_in_as_username_is_visible(name=new_user["name"])
        with allure.step("Add products to cart"):
            for index in [0, 1, 2, 3]:
                home_page.products.hover_on_product(index=index)
                home_page.products.click_add_to_cart_overlay(index=index)
                home_page.cart_modal.click_continue_shopping_button()
        with allure.step("Click 'Cart' button"):
            home_page.header.click_cart_link()

        with allure.step("Verify that cart page is displayed"):
            cart_page.cart_page_is_open()
        with allure.step("Click Proceed To Checkout"):
            cart_page.click_proceed_to_checkout_button()

        with allure.step(
            "Verify that the delivery address is same address filled at the time registration of account"
        ):
            checkout_page.delivery_address_is_correct(user=new_user)
        with allure.step(
            "Verify that the billing address is same address filled at the time registration of account"
        ):
            checkout_page.billing_address_is_correct(user=new_user)
        with allure.step("Click 'Delete Account' button"):
            checkout_page.header.click_delete_account_link()

        with allure.step("Verify 'ACCOUNT DELETED!' and click 'Continue' button"):
            account_deleted_page.account_deleted_text_is_visible()
            account_deleted_page.click_continue_button()
