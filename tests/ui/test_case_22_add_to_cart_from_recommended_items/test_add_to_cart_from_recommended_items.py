import allure

from src.pages.home_page import HomePage
from src.pages.cart_page import CartPage
from tests.ui.base_test import BaseUITest


@allure.story("Cart")
class TestAddToCartFromRecommendedItems(BaseUITest):
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test Case 22: Add to cart from Recommended items")
    def test_add_to_cart_from_recommended_items(self, page):
        home_page = HomePage(page)
        cart_page = CartPage(page)

        with allure.step("Navigate to url"):
            home_page.open()
        with allure.step("Scroll to bottom of page"):
            home_page.footer.scroll_down_to_footer()
        with allure.step("Verify 'RECOMMENDED ITEMS' are visible"):
            home_page.recommended_items_are_visible()
        with allure.step("Click on 'Add To Cart' on Recommended product"):
            product_name = home_page.get_recommended_product_name(index=0)
            home_page.add_recommended_product_to_cart(index=0)
        with allure.step("Click on 'View Cart' button"):
            home_page.cart_modal.click_view_cart_link()

        with allure.step("Verify that product is displayed in cart page"):
            cart_page.order_table.products_are_in_cart([product_name])
