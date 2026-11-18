import allure

from src.pages.home_page import HomePage
from src.pages.cart_page import CartPage
from tests.ui.base_test import BaseUITest


@allure.story("Subscription")
class TestSubscriptionInCartPage(BaseUITest):
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test Case 11: Verify Subscription in Cart page")
    def test_verify_subscription_in_cart_page(self, page):
        home_page = HomePage(page)
        cart_page = CartPage(page)

        with allure.step("Navigate to url"):
            home_page.open()
        with allure.step("Verify that home page is visible successfully"):
            home_page.home_page_is_visible()
        with allure.step("Click 'Cart' button"):
            home_page.header.click_cart_link()

        with allure.step("Scroll down to footer"):
            cart_page.footer.scroll_down_to_footer()
        with allure.step("Verify text 'SUBSCRIPTION'"):
            cart_page.footer.subscription_text_is_visible()
        with allure.step("Enter email address in input and click arrow button"):
            cart_page.footer.fill_subscription_email_input("testtest@example.com")
            cart_page.footer.click_subscription_button()
        with allure.step(
            "Verify success message 'You have been successfully subscribed!' is visible"
        ):
            cart_page.footer.subscription_successful_text_is_visible()
