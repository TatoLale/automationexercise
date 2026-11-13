import allure

from ui.pages.home_page import HomePage
from ui.pages.products_page import ProductsPage
from ui.base_test import BaseUITest


@allure.story("Products")
class TestSearchProduct(BaseUITest):
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test Case 9: Search Product")
    def test_search_product(self, page):
        home_page = HomePage(page)
        products_page = ProductsPage(page)

        with allure.step("Navigate to url"):
            home_page.open()
        with allure.step("Verify that home page is visible successfully"):
            home_page.home_page_is_visible()
        with allure.step("Click on 'Products' button"):
            home_page.click_products_link()

        with allure.step("Verify user is navigated to ALL PRODUCTS page successfully"):
            products_page.all_products_page_is_open()
        with allure.step("Enter product name in search input and click search button"):
            products_page.enter_product_name("Jeans")
            products_page.click_search_button()
        with allure.step("Verify 'SEARCHED PRODUCTS' is visible"):
            products_page.searched_products_text_is_visible()
        with allure.step("Verify all the products related to search are visible"):
            products_page.searched_products_are_related()
