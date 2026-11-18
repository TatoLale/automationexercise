import allure

from src.pages.home_page import HomePage
from src.pages.products_page import ProductsPage
from src.pages.view_cart_page import ViewCartPage
from tests.ui.base_test import BaseUITest


@allure.story("Cart")
class TestAddProducts(BaseUITest):
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test Case 12: Add Products in Cart")
    def test_add_products_in_cart(self, page):
        home_page = HomePage(page)
        products_page = ProductsPage(page)
        view_cart_page = ViewCartPage(page)

        with allure.step("Navigate to url"):
            home_page.open()
        with allure.step("Verify that home page is visible successfully"):
            home_page.home_page_is_visible()
        with allure.step("Click 'Products' button"):
            home_page.click_products_link()

        with allure.step("Hover over first product and click 'Add to cart'"):
            first_product_name = products_page.get_product_name(0)
            first_product_price = products_page.get_product_price(0)
            products_page.hover_on_product(index=0)
            products_page.click_add_to_cart_overlay(index=0)
        with allure.step("Click 'Continue Shopping' button"):
            products_page.click_continue_shopping_button()
        with allure.step("Hover over second product and click 'Add to cart'"):
            second_product_name = products_page.get_product_name(1)
            second_product_price = products_page.get_product_price(1)
            products_page.hover_on_product(index=1)
            products_page.click_add_to_cart_overlay(index=1)
        with allure.step("Click 'View Cart' button"):
            products_page.click_view_cart_link()
        with allure.step("Verify both products are added to Cart"):
            view_cart_page.products_are_in_cart(
                [first_product_name, second_product_name]
            )
        with allure.step("Verify their prices, quantity and total price"):
            view_cart_page.products_prices_quantities_and_totals_are_correct(
                prices=[first_product_price, second_product_price], quantities=[1, 1]
            )

        page.wait_for_timeout(3000)
