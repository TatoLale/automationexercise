import allure

from src.pages.home_page import HomePage
from src.pages.products_page import ProductsPage
from src.pages.cart_page import CartPage
from src.pages.login_page import LoginPage
from tests.ui.base_test import BaseUITest


@allure.story("Cart")
class TestSearchProductsAndVerifyCartAfterLogin(BaseUITest):
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test Case 20: Search Products and Verify Cart After Login")
    def test_search_products_and_verify_cart_after_login(self, page, registered_user):
        home_page = HomePage(page)
        products_page = ProductsPage(page)
        cart_page = CartPage(page)
        login_page = LoginPage(page)

        with allure.step("Navigate to url"):
            home_page.open()
        with allure.step("Click on 'Products' button"):
            home_page.header.click_products_link()

        with allure.step("Verify user is navigated to ALL PRODUCTS page successfully"):
            products_page.all_products_page_is_open()
        with allure.step("Enter product name in search input and click search button"):
            products_page.enter_product_name(product="Jeans")
            products_page.click_search_button()
        with allure.step("Verify 'SEARCHED PRODUCTS' is visible"):
            products_page.searched_products_text_is_visible()
        with allure.step("Verify all the products related to search are visible"):
            products_page.searched_products_are_related()
        with allure.step("Add those products to cart"):
            product_names = []
            count = products_page.products.product_cards.count()
            for index in range(count):
                product_names.append(products_page.products.get_product_name(index))
                products_page.products.hover_on_product(index=index)
                products_page.products.click_add_to_cart_overlay(index=index)
                products_page.cart_modal.click_continue_shopping_button()
        with allure.step(
            "Click 'Cart' button and verify that products are visible in cart"
        ):
            products_page.header.click_cart_link()

            cart_page.order_table.products_are_in_cart(product_names)

        with allure.step("Click 'Signup / Login' button and submit login details"):
            cart_page.header.click_signup_login_link()

            login_page.fill_email_and_password_fields(
                email=registered_user["email"], password=registered_user["password"]
            )
            login_page.click_login_button()

        with allure.step("Again, go to Cart page"):
            home_page.header.click_cart_link()

        with allure.step(
            "Verify that those products are visible in cart after login as well"
        ):
            cart_page.order_table.products_are_in_cart(product_names)
