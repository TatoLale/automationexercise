from playwright.sync_api import expect

from src.pages.base_page import BasePage


class AccountCreatedPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.account_created_text = page.get_by_text("Account Created!")
        self.continue_button = page.get_by_role("link", name="Continue")

    def account_created_text_is_visible(self):
        expect(self.account_created_text).to_be_visible()

    def click_continue_button(self):
        self.continue_button.click()
