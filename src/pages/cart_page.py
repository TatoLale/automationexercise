from playwright.sync_api import expect

from src.pages.base_page import BasePage
from src.components.order_table import OrderTable
from src.config import BASE_URL_UI


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.order_table = OrderTable(page)
        self.proceed_to_checkout_button = page.get_by_text("Proceed To Checkout")
        self.register_login_link = page.locator("#checkoutModal").get_by_role(
            "link", name="Register / Login"
        )

    def cart_page_is_open(self):
        expect(self.page).to_have_url(f"{BASE_URL_UI}/view_cart")

    def click_proceed_to_checkout_button(self):
        self.proceed_to_checkout_button.click()

    def click_register_login_link(self):
        self.register_login_link.click()