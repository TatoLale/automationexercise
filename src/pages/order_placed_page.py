from playwright.sync_api import expect

from src.pages.base_page import BasePage


class OrderPlacedPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.order_placed_heading = page.get_by_role("heading", name="Order Placed!")
        self.order_confirmed_text = page.get_by_text(
            "Congratulations! Your order has been confirmed!"
        )
        self.download_invoice_link = page.get_by_role("link", name="Download Invoice")
        self.continue_button = page.get_by_role("link", name="Continue")

    def order_placed_text_is_visible(self):
        expect(self.order_placed_heading).to_be_visible()
        expect(self.order_confirmed_text).to_be_visible()

    def download_invoice(self):
        with self.page.expect_download() as download_info:
            self.download_invoice_link.click()
        return download_info.value

    def click_continue_button(self):
        self.continue_button.click()