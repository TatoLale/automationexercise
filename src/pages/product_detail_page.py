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
        self.write_your_review_text = page.get_by_text("Write Your Review")
        self.name_input = page.locator("#name")
        self.email_input = page.locator("#email")
        self.review_input = page.locator("#review")
        self.review_button = page.locator("#button-review")
        self.review_successful_text = page.get_by_text("Thank you for your review.")

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
        expect(self.quantity_input).to_be_visible()
        self.quantity_input.fill(number)

    def click_add_to_cart_button(self):
        self.page.wait_for_load_state("load")
        self.add_to_cart_button.click()

    def write_your_review_text_is_visible(self):
        expect(self.write_your_review_text).to_be_visible()

    def fill_review(self, name, email, review):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.review_input.fill(review)

    def click_review_button(self):
        self.review_button.click()

    def review_successful_text_is_visible(self):
        expect(self.review_successful_text).to_be_visible()
