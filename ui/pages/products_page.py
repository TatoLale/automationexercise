import re

from playwright.sync_api import expect

from config import BASE_URL_UI


class ProductsPage:
    def __init__(self, page):
        self.page = page

        self.product_cards = page.locator(".features_items .product-image-wrapper")
        self.first_product_view_link = page.get_by_role(
            "link", name="View Product"
        ).first
        # PRODUCT DETAIL PAGE
        self.product_information = page.locator(".product-information")
        self.product_name = self.product_information.get_by_role("heading")
        self.product_category = self.product_information.get_by_text("Category:")
        self.product_price = self.product_information.get_by_text("Rs.")
        self.product_availability = self.product_information.get_by_text(
            "Availability:"
        )
        self.product_condition = self.product_information.get_by_text("Condition:")
        self.product_brand = self.product_information.get_by_text("Brand:")

    def all_products_page_is_open(self):
        expect(self.page).to_have_url(f"{BASE_URL_UI}/products")

    def products_list_is_visible(self):
        expect(self.product_cards.first).to_be_visible()

    def click_first_product_view_link(self):
        self.first_product_view_link.click()

    # PRODUCT DETAIL PAGE
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
