import allure

from src.pages.home_page import HomePage
from src.pages.cart_page import CartPage
from src.pages.login_page import LoginPage
from src.pages.signup_page import SignUpPage
from src.pages.account_created_page import AccountCreatedPage
from src.pages.checkout_page import CheckoutPage
from src.pages.payment_page import PaymentPage
from src.pages.order_placed_page import OrderPlacedPage
from src.pages.account_deleted_page import AccountDeletedPage
from tests.ui.base_test import BaseUITest


@allure.story("Place Order")
class TestDownloadInvoiceAfterPurchaseOrder(BaseUITest):
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test Case 24: Download Invoice after purchase order")
    def test_download_invoice_after_purchase_order(self, page, new_user, tmp_path):
        home_page = HomePage(page)
        cart_page = CartPage(page)
        login_page = LoginPage(page)
        signup_page = SignUpPage(page)
        account_created_page = AccountCreatedPage(page)
        checkout_page = CheckoutPage(page)
        payment_page = PaymentPage(page)
        order_placed_page = OrderPlacedPage(page)
        account_deleted_page = AccountDeletedPage(page)

        with allure.step("Navigate to url"):
            home_page.open()
        with allure.step("Verify that home page is visible successfully"):
            home_page.home_page_is_visible()
        with allure.step("Add products to cart"):
            product_names = []
            for index in [0, 1, 2, 3]:
                product_names.append(home_page.products.get_product_name(index))
                home_page.products.hover_on_product(index=index)
                home_page.products.click_add_to_cart_overlay(index=index)
                home_page.cart_modal.click_continue_shopping_button()
        with allure.step("Click 'Cart' button"):
            home_page.header.click_cart_link()

        with allure.step("Verify that cart page is displayed"):
            cart_page.cart_page_is_open()
        with allure.step("Click Proceed To Checkout"):
            cart_page.click_proceed_to_checkout_button()
        with allure.step("Click 'Register / Login' button"):
            cart_page.click_register_login_link()

        with allure.step("Fill all details in Signup and create account"):
            login_page.fill_name_and_email_fields(
                name=new_user["name"], email=new_user["email"]
            )
            login_page.click_signup_button()

            signup_page.create_account(user=new_user)

        with allure.step("Verify 'ACCOUNT CREATED!' and click 'Continue' button"):
            account_created_page.account_created_text_is_visible()
            account_created_page.click_continue_button()

        with allure.step("Verify ' Logged in as username' at top"):
            home_page.header.logged_in_as_username_is_visible(name=new_user["name"])
        with allure.step("Click 'Cart' button"):
            home_page.header.click_cart_link()

        with allure.step("Click 'Proceed To Checkout' button"):
            cart_page.click_proceed_to_checkout_button()

        with allure.step("Verify Address Details and Review Your Order"):
            checkout_page.delivery_address_is_correct(user=new_user)
            checkout_page.order_table.products_are_in_cart(product_names)
        with allure.step(
            "Enter description in comment text area and click 'Place Order'"
        ):
            checkout_page.fill_comment_textarea("TestTestTest")
            checkout_page.click_place_order_link()

        with allure.step(
            "Enter payment details: Name on Card, Card Number, CVC, Expiration date"
        ):
            payment_page.fill_payment_details(
                name_on_card="TestName",
                card_number="4111111111111111",
                cvc="123",
                expiration_month="12",
                expiration_year="2030",
            )
        with allure.step("Click 'Pay and Confirm Order' button"):
            payment_page.click_pay_and_confirm_button()
        # The success message only flashes on /payment before the redirect,
        # so the order is verified on the 'Order Placed!' confirmation page instead.
        with allure.step(
            "Verify success message 'Your order has been placed successfully!'"
        ):
            order_placed_page.order_placed_text_is_visible()
        with allure.step(
            "Click 'Download Invoice' button and verify invoice is downloaded successfully."
        ):
            invoice = order_placed_page.download_invoice()
            invoice_file = tmp_path / invoice.suggested_filename
            invoice.save_as(invoice_file)
            assert invoice_file.exists()
        with allure.step("Click 'Continue' button"):
            order_placed_page.click_continue_button()

        with allure.step("Click 'Delete Account' button"):
            home_page.header.click_delete_account_link()

        with allure.step("Verify 'ACCOUNT DELETED!' and click 'Continue' button"):
            account_deleted_page.account_deleted_text_is_visible()
            account_deleted_page.click_continue_button()
