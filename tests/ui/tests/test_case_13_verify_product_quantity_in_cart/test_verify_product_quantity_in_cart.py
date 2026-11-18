import allure

from src.pages.home_page import HomePage
from src.pages.products_page import ProductsPage
from src.pages.view_cart_page import ViewCartPage
from tests.ui.base_test import BaseUITest


@allure.story("Cart")
class TestProductQuantity(BaseUITest):
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test Case 13: Verify Product quantity in Cart")
    def test_verify_product_quantity_in_cart(self, page):
        home_page = HomePage(page)
        products_page = ProductsPage(page)
        view_cart_page = ViewCartPage(page)

        with allure.step("Navigate to url"):
            home_page.open()
        with allure.step("Verify that home page is visible successfully"):
            home_page.home_page_is_visible()
        with allure.step("Click 'View Product' for any product on home page"):
            home_page.click_view_product_link()

        with allure.step("Verify product detail is opened"):
            products_page.product_detail_page_is_open()
        with allure.step("Increase quantity to 4"):
            products_page.fill_quantity_input("4")
        with allure.step("Click 'Add to cart' button"):
            products_page.click_add_to_cart_button()
        with allure.step("Click 'View Cart' button"):
            products_page.click_view_cart_link()
        with allure.step(
            "Verify that product is displayed in cart page with exact quantity"
        ):
            view_cart_page.product_quantity_is(position=0, quantity=4)
