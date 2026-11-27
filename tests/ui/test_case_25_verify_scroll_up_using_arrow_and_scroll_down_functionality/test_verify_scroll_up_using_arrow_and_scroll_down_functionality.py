import allure

from src.pages.home_page import HomePage
from tests.ui.base_test import BaseUITest


@allure.story("Navigation")
class TestVerifyScrollUpUsingArrowButtonAndScrollDownFunctionality(BaseUITest):
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title(
        "Test Case 25: Verify Scroll Up using 'Arrow' button and Scroll Down functionality"
    )
    def test_verify_scroll_up_using_arrow_button_and_scroll_down_functionality(
        self, page
    ):
        home_page = HomePage(page)

        with allure.step("Navigate to url"):
            home_page.open()
        with allure.step("Verify that home page is visible successfully"):
            home_page.home_page_is_visible()
        with allure.step("Scroll down page to bottom"):
            home_page.footer.scroll_down_to_footer()
        with allure.step("Verify 'SUBSCRIPTION' is visible"):
            home_page.footer.subscription_text_is_visible()
        with allure.step("Click on arrow at bottom right side to move upward"):
            home_page.click_scroll_up_arrow()
        with allure.step(
            "Verify that page is scrolled up and 'Full-Fledged practice website for Automation Engineers' text is visible on screen"
        ):
            home_page.full_fledged_text_is_in_viewport()
