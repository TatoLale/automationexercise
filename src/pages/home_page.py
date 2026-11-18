from playwright.sync_api import expect

from src.components.cart_modal import CartModal
from src.components.product_list import ProductList
from src.config import BASE_URL_UI
from src.pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.products = ProductList(page)
        self.cart_modal = CartModal(page)

    def open(self):
        self.page.goto(BASE_URL_UI)

    def home_page_is_visible(self):
        expect(self.header.home_link).to_have_attribute("style", "color: orange;")
