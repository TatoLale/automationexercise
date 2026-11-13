import allure

from ui.pages.home_page import HomePage
from ui.pages.products_page import ProductsPage
from ui.base_test import BaseUITest


@allure.story("Products")
class TestVerifyProducts(BaseUITest):
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test Case 8: Verify All Products and product detail page")
    def test_verify_all_products_and_product_detail_page(self, page):
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
        with allure.step("The products list is visible"):
            products_page.products_list_is_visible()
        with allure.step("Click on 'View Product' of first product"):
            products_page.click_first_product_view_link()
        with allure.step("User is landed to product detail page"):
            products_page.product_detail_page_is_open()
        with allure.step(
            "Verify that detail detail is visible: product name, category, price, availability, condition, brand"
        ):
            products_page.product_details_are_visible()

