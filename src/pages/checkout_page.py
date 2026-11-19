from playwright.sync_api import expect

from src.pages.base_page import BasePage
from src.components.order_table import OrderTable


class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.order_table = OrderTable(page)
        self.delivery_address = page.locator("#address_delivery")
        self.comment_textarea = page.locator("#ordermsg textarea")
        self.place_order_link = page.get_by_role("link", name="Place Order")

    def delivery_address_is_correct(self, user):
        for value in [
            user["firstname"],
            user["lastname"],
            user["company"],
            user["address1"],
            user["address2"],
            user["city"],
            user["state"],
            user["zipcode"],
            user["country"],
            user["mobile_number"],
        ]:
            expect(self.delivery_address).to_contain_text(value)

    def fill_comment_textarea(self, comment):
        self.comment_textarea.fill(comment)

    def click_place_order_link(self):
        self.place_order_link.click()