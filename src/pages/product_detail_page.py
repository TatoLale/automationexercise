import re

from playwright.sync_api import expect

from src.components.cart_modal import CartModal
from src.pages.base_page import BasePage


class ProductDetailPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.cart_modal = CartModal(page)

        self.product_information = page.locator(".product-information")
        self.product_name = self.product_information.get_by_role("heading")
        self.product_category = self.product_information.get_by_text("Category:")
        self.product_price = self.product_information.get_by_text("Rs.")
        self.product_availability = self.product_information.get_by_text(
            "Availability:"
        )
        self.product_condition = self.product_information.get_by_text("Condition:")
        self.product_brand = self.product_information.get_by_text("Brand:")
        self.quantity_input = page.locator("#quantity")
        self.add_to_cart_button = page.get_by_role("button", name="Add to cart")

    def product_detail_page_is_open(self):
        expect(self.page).to_have_url(re.compile(r".*/product_details/\d+"))

    def product_details_are_visible(self):
        expect(self.product_information).to_be_visible()
        expect(self.product_name).to_be_visible()
        expect(self.product_category).to_be_visible()
        expect(self.product_price).to_be_visible()
        expect(self.product_availability).to_be_visible()
        expect(self.product_condition).to_be_visible()
        expect(self.product_brand).to_be_visible()

    def fill_quantity_input(self, number):
        self.quantity_input.fill(number)

    def click_add_to_cart_button(self):
        self.page.wait_for_load_state("load")
        self.add_to_cart_button.click()
