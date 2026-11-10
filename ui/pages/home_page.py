from playwright.sync_api import expect

from config import BASE_URL_UI


class HomePage:
    def __init__(self, page):
        self.page = page

        self.home_link = page.get_by_role("link", name="Home")
        self.signup_login_link = page.get_by_role("link", name="Signup / Login")
        self.logged_in_as = page.get_by_text("Logged in as")
        self.delete_account_button = page.get_by_role("link", name="Delete Account")
        self.delete_account_text = page.get_by_text("Account Deleted!")

    def open(self):
        self.page.goto(BASE_URL_UI)

    def home_page_is_visible(self):
        expect(self.home_link).to_have_attribute("style", "color: orange;")

    def click_signup_login_link(self):
        self.signup_login_link.click()

    def logged_in_as_username_is_visible(self, name):
        expect(self.logged_in_as).to_contain_text(name)

    def click_delete_account_button(self):
        self.delete_account_button.click()

    def account_delete_confirmation_is_visible(self):
        expect(self.delete_account_text).to_be_visible()
