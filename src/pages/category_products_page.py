import re

from playwright.sync_api import expect

from src.components.product_list import ProductList
from src.components.sidebar import Sidebar
from src.pages.base_page import BasePage


class CategoryProductsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.products = ProductList(page)
        self.sidebar = Sidebar(page)

        self.category_text = page.locator(".features_items .title.text-center")

    def category_page_is_open(self):
        expect(self.page).to_have_url(re.compile(r".*/category_products/\d+"))

    def category_text_is(self, text):
        expect(self.category_text).to_have_text(text)
