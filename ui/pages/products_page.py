import re

from playwright.sync_api import expect

from config import BASE_URL_UI


class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.search_term = None

        self.product_cards = page.locator(".features_items .product-image-wrapper")
        self.first_product_view_link = page.get_by_role(
            "link", name="View Product"
        ).first
        self.product_information = page.locator(".product-information")
        self.product_name = self.product_information.get_by_role("heading")
        self.product_category = self.product_information.get_by_text("Category:")
        self.product_price = self.product_information.get_by_text("Rs.")
        self.product_availability = self.product_information.get_by_text(
            "Availability:"
        )
        self.product_condition = self.product_information.get_by_text("Condition:")
        self.product_brand = self.product_information.get_by_text("Brand:")
        self.search_input = page.locator("#search_product")
        self.search_button = page.locator("#submit_search")
        self.searched_products_text = page.get_by_role(
            "heading", name="Searched Products"
        )

    def all_products_page_is_open(self):
        expect(self.page).to_have_url(f"{BASE_URL_UI}/products")

    def products_list_is_visible(self):
        expect(self.product_cards.first).to_be_visible()

    def click_first_product_view_link(self):
        self.first_product_view_link.click()

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

    def enter_product_name(self, product):
        self.search_input.fill(product)
        self.search_term = product

    def click_search_button(self):
        self.page.wait_for_load_state("load")
        self.search_button.click()

    def searched_products_text_is_visible(self):
        expect(self.searched_products_text).to_be_visible()

    def searched_products_are_related(self):
        expect(self.product_cards.first).to_be_visible()
        for card in self.product_cards.all():
            expect(card).to_be_visible()
            expect(card.locator(".productinfo p")).to_contain_text(
                self.search_term, ignore_case=True
            )
