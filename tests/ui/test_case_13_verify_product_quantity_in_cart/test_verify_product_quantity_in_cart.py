import allure

from src.pages.home_page import HomePage
from src.pages.cart_page import CartPage
from src.pages.product_detail_page import ProductDetailPage
from tests.ui.base_test import BaseUITest


@allure.story("Cart")
class TestProductQuantity(BaseUITest):
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test Case 13: Verify Product quantity in Cart")
    def test_verify_product_quantity_in_cart(self, page):
        home_page = HomePage(page)
        product_detail_page = ProductDetailPage(page)
        cart_page = CartPage(page)

        with allure.step("Navigate to url"):
            home_page.open()
        with allure.step("Verify that home page is visible successfully"):
            home_page.home_page_is_visible()
        with allure.step("Click 'View Product' for any product on home page"):
            home_page.products.click_view_product(index=0)

        with allure.step("Verify product detail is opened"):
            product_detail_page.product_detail_page_is_open()
        with allure.step("Increase quantity to 4"):
            product_detail_page.fill_quantity_input("4")
        with allure.step("Click 'Add to cart' button"):
            product_detail_page.click_add_to_cart_button()
        with allure.step("Click 'View Cart' button"):
            product_detail_page.cart_modal.click_view_cart_link()
        with allure.step(
            "Verify that product is displayed in cart page with exact quantity"
        ):
            cart_page.product_quantity_is(position=0, quantity=4)
