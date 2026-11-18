import allure

from src.pages.home_page import HomePage
from tests.ui.base_test import BaseUITest


@allure.story("Subscription")
class TestSubscriptionInHomePage(BaseUITest):
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test Case 10: Verify Subscription in home page")
    def test_verify_subscription_in_home_page(self, page):
        home_page = HomePage(page)

        with allure.step("Navigate to url"):
            home_page.open()
        with allure.step("Verify that home page is visible successfully"):
            home_page.home_page_is_visible()
        with allure.step("Scroll down to footer"):
            home_page.footer.scroll_down_to_footer()
        with allure.step("Verify text 'SUBSCRIPTION'"):
            home_page.footer.subscription_text_is_visible()
        with allure.step("Enter email address in input and click arrow button"):
            home_page.footer.fill_subscription_email_input(email="testtest@example.com")
            home_page.footer.click_subscription_button()
        with allure.step(
            "Verify success message 'You have been successfully subscribed!' is visible"
        ):
            home_page.footer.subscription_successful_text_is_visible()
