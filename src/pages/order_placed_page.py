from playwright.sync_api import expect

from src.pages.base_page import BasePage


class OrderPlacedPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.order_placed_heading = page.get_by_role("heading", name="Order Placed!")
        self.order_confirmed_text = page.get_by_text(
            "Congratulations! Your order has been confirmed!"
        )

    def order_placed_text_is_visible(self):
        expect(self.order_placed_heading).to_be_visible()
        expect(self.order_confirmed_text).to_be_visible()
