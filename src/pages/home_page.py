from playwright.sync_api import expect

from src.components.cart_modal import CartModal
from src.components.product_list import ProductList
from src.components.sidebar import Sidebar
from src.config import BASE_URL_UI
from src.pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.products = ProductList(page)
        self.cart_modal = CartModal(page)
        self.sidebar = Sidebar(page)
        self.recommended_items = page.locator(".recommended_items")
        self.recommended_cards = page.locator(
            ".recommended_items .item.active .product-image-wrapper"
        )

    def open(self):
        self.page.goto(BASE_URL_UI)

    def home_page_is_visible(self):
        expect(self.header.home_link).to_have_attribute("style", "color: orange;")

    def recommended_items_are_visible(self):
        expect(self.recommended_items).to_be_visible()

    def get_recommended_product_name(self, index):
        name = self.recommended_cards.nth(index).locator(".productinfo p")
        expect(name).to_be_visible()
        return name.inner_text()

    def add_recommended_product_to_cart(self, index):
        self.page.wait_for_load_state("load")
        self.recommended_cards.nth(index).locator(".add-to-cart").click()
