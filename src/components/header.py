from playwright.sync_api import expect


class Header:
    def __init__(self, page):
        self.page = page

        self.header = page.locator("#header")
        self.home_link = self.header.get_by_role("link", name="Home")
        self.products_link = self.header.get_by_role("link", name="Products")
        self.cart_link = self.header.get_by_role("link", name="Cart")
        self.signup_login_link = self.header.get_by_role("link", name="Signup / Login")
        self.logout_link = self.header.get_by_role("link", name="Logout")
        self.delete_account_link = self.header.get_by_role("link", name="Delete Account")
        self.test_cases_link = self.header.get_by_role("link", name="Test Cases")
        self.contact_us_link = self.header.get_by_role("link", name="Contact us")
        self.logged_in_as = self.header.get_by_text("Logged in as")

    def scroll_up_to_header(self):
        self.header.scroll_into_view_if_needed()

    def click_home_link(self):
        self.home_link.click()

    def click_products_link(self):
        self.products_link.click()

    def click_cart_link(self):
        self.cart_link.click()

    def click_signup_login_link(self):
        self.signup_login_link.click()

    def click_logout_link(self):
        self.logout_link.click()

    def click_delete_account_link(self):
        self.delete_account_link.click()

    def click_test_cases_link(self):
        self.test_cases_link.click()

    def click_contact_us_link(self):
        self.contact_us_link.click()

    def logged_in_as_username_is_visible(self, name):
        expect(self.logged_in_as).to_contain_text(name)
