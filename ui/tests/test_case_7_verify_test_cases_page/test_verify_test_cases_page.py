import allure

from ui.pages.home_page import HomePage
from ui.pages.test_cases_page import CasesPage
from ui.base_test import BaseUITest


@allure.story("Test Case")
class TestVerifyTestCasesPage(BaseUITest):
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test Case 7: Verify Test Cases Page")
    def test_verify_test_cases_page(self, page):
        home_page = HomePage(page)
        test_cases_page = CasesPage(page)

        with allure.step("Navigate to url"):
            home_page.open()
        with allure.step("Verify that home page is visible successfully"):
            home_page.home_page_is_visible()
        with allure.step("Click on 'Test Cases' button"):
            home_page.click_test_cases_link()

        with allure.step("Verify user is navigated to test cases page successfully"):
            test_cases_page.test_cases_text_is_visible()
