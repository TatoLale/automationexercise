from playwright.sync_api import expect

from src.components.cart_modal import CartModal
from src.components.product_list import ProductList
from src.components.sidebar import Sidebar
from src.config import BASE_URL_UI
from src.pages.base_page import BasePage


class ProductsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.products = ProductList(page)
        self.cart_modal = CartModal(page)
        self.sidebar = Sidebar(page)
        self.search_term = None

        self.search_input = page.locator("#search_product")
        self.search_button = page.locator("#submit_search")
        self.searched_products_text = page.get_by_role(
            "heading", name="Searched Products"
        )

    def all_products_page_is_open(self):
        expect(self.page).to_have_url(f"{BASE_URL_UI}/products")

    def enter_product_name(self, product):
        self.search_input.fill(product)
        self.search_term = product

    def click_search_button(self):
        self.page.wait_for_load_state("load")
        self.search_button.click()

    def searched_products_text_is_visible(self):
        expect(self.searched_products_text).to_be_visible()

    def searched_products_are_related(self):
        cards = self.products.product_cards
        expect(cards.first).to_be_visible()
        for card in cards.all():
            expect(card).to_be_visible()
            expect(card.locator(".productinfo p")).to_contain_text(
                self.search_term, ignore_case=True
            )
