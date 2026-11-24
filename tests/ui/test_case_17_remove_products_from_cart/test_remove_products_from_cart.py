import allure

from src.pages.home_page import HomePage
from src.pages.cart_page import CartPage
from tests.ui.base_test import BaseUITest


@allure.story("Cart")
class TestRemoveProductsFromCart(BaseUITest):
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test Case 17: Remove Products From Cart")
    def test_remove_products_from_cart(self, page):
        home_page = HomePage(page)
        cart_page = CartPage(page)

        with allure.step("Navigate to url"):
            home_page.open()
        with allure.step("Verify that home page is visible successfully"):
            home_page.home_page_is_visible()
        with allure.step("Add products to cart"):
            product_names = []
            for index in [0, 1, 2, 3]:
                product_names.append(home_page.products.get_product_name(index))
                home_page.products.hover_on_product(index=index)
                home_page.products.click_add_to_cart_overlay(index=index)
                home_page.cart_modal.click_continue_shopping_button()
        with allure.step("Click 'Cart' button"):
            home_page.header.click_cart_link()

        with allure.step("Verify that cart page is displayed"):
            cart_page.cart_page_is_open()
        with allure.step("Click 'X' button corresponding to particular product"):
            cart_page.order_table.click_product_x_button(position=0)
        with allure.step("Verify that product is removed from the cart"):
            cart_page.order_table.products_are_in_cart(product_names[1:])
