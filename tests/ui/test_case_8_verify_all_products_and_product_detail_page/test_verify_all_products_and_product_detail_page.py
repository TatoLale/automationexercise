import allure

from src.pages.home_page import HomePage
from src.pages.products_page import ProductsPage
from src.pages.product_detail_page import ProductDetailPage
from tests.ui.base_test import BaseUITest


@allure.story("Products")
class TestVerifyProducts(BaseUITest):
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test Case 8: Verify All Products and product detail page")
    def test_verify_all_products_and_product_detail_page(self, page):
        home_page = HomePage(page)
        products_page = ProductsPage(page)
        product_detail_page = ProductDetailPage(page)

        with allure.step("Navigate to url"):
            home_page.open()
        with allure.step("Verify that home page is visible successfully"):
            home_page.home_page_is_visible()
        with allure.step("Click on 'Products' button"):
            home_page.header.click_products_link()

        with allure.step("Verify user is navigated to ALL PRODUCTS page successfully"):
            products_page.all_products_page_is_open()
        with allure.step("The products list is visible"):
            products_page.products.products_list_is_visible()
        with allure.step("Click on 'View Product' of first product"):
            products_page.products.click_view_product(index=0)
        with allure.step("User is landed to product detail page"):
            product_detail_page.product_detail_page_is_open()
        with allure.step(
            "Verify that detail detail is visible: product name, category, price, availability, condition, brand"
        ):
            product_detail_page.product_details_are_visible()
