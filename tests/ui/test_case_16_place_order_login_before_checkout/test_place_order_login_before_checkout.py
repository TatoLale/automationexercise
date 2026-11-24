import allure

from src.pages.home_page import HomePage
from src.pages.cart_page import CartPage
from src.pages.login_page import LoginPage
from src.pages.checkout_page import CheckoutPage
from src.pages.payment_page import PaymentPage
from src.pages.order_placed_page import OrderPlacedPage
from src.pages.account_deleted_page import AccountDeletedPage
from tests.ui.base_test import BaseUITest


@allure.story("Place Order")
class TestPlaceOrderLoginBeforeCheckout(BaseUITest):
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test Case 16: Place Order: Login before Checkout")
    def test_place_order_login_before_checkout(self, page, registered_user):
        home_page = HomePage(page)
        cart_page = CartPage(page)
        login_page = LoginPage(page)
        checkout_page = CheckoutPage(page)
        payment_page = PaymentPage(page)
        order_placed_page = OrderPlacedPage(page)
        account_deleted_page = AccountDeletedPage(page)

        with allure.step("Navigate to url"):
            home_page.open()
        with allure.step("Verify that home page is visible successfully"):
            home_page.home_page_is_visible()
        with allure.step("Click 'Signup / Login' button"):
            home_page.header.click_signup_login_link()

        with allure.step("Fill email, password and click 'Login' button"):
            login_page.fill_email_and_password_fields(
                email=registered_user["email"], password=registered_user["password"]
            )
            login_page.click_login_button()

        with allure.step("Verify 'Logged in as username' at top"):
            home_page.header.logged_in_as_username_is_visible(
                name=registered_user["name"]
            )
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

        with allure.step("Verify Address Details and Review Your Order"):
            checkout_page.delivery_address_is_correct(user=registered_user)
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
        with allure.step("Click 'Delete Account' button"):
            order_placed_page.header.click_delete_account_link()

        with allure.step("Verify 'ACCOUNT DELETED!' and click 'Continue' button"):
            account_deleted_page.account_deleted_text_is_visible()
            account_deleted_page.click_continue_button()
