import allure

from src.pages.home_page import HomePage
from src.pages.products_page import ProductsPage
from src.pages.brand_products_page import BrandProductsPage
from tests.ui.base_test import BaseUITest


@allure.story("Products")
class TestViewCartBrandProducts(BaseUITest):
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test Case 19: View & Cart Brand Products")
    def test_view_cart_brand_products(self, page):
        home_page = HomePage(page)
        products_page = ProductsPage(page)
        brand_products_page = BrandProductsPage(page)

        with allure.step("Navigate to url"):
            home_page.open()
        with allure.step("Click on 'Products' button"):
            home_page.header.click_products_link()

        with allure.step("Verify that Brands are visible on left side bar"):
            products_page.sidebar.brand_sidebar_is_visible()
        with allure.step("Click on any brand name"):
            products_page.sidebar.click_brand(name="Polo")

        with allure.step(
            "Verify that user is navigated to brand page and brand products are displayed"
        ):
            brand_products_page.brand_page_is_open()
            brand_products_page.brand_text_is(text="Brand - Polo Products")
            brand_products_page.products.products_list_is_visible()
        with allure.step("On left side bar, click on any other brand link"):
            brand_products_page.sidebar.click_brand(name="Madame")
        with allure.step(
            "Verify that user is navigated to that brand page and can see products"
        ):
            brand_products_page.brand_page_is_open()
            brand_products_page.brand_text_is(text="Brand - Madame Products")
            brand_products_page.products.products_list_is_visible()
