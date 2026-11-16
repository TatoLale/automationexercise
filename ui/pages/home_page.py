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
        self.logout_button = page.get_by_role("link", name="Logout")
        self.contact_us_link = page.get_by_role("link", name="Contact us")
        self.test_cases_link = page.locator("#header").get_by_role(
            "link", name="Test Cases"
        )
        self.products_link = page.locator("#header").get_by_role(
            "link", name="Products"
        )
        self.footer = page.locator("#footer")
        self.subscription_text = page.get_by_text("Subscription")
        self.subscription_email_input = page.locator("#susbscribe_email")
        self.subscription_button = page.locator("#subscribe")
        self.subscription_successful_text = page.get_by_text("You have been successfully subscribed!")

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

    def click_logout_button(self):
        self.logout_button.click()

    def click_contact_us_link(self):
        self.contact_us_link.click()

    def click_test_cases_link(self):
        self.test_cases_link.click()

    def click_products_link(self):
        self.products_link.click()

    def scroll_down_to_footer(self):
        self.footer.scroll_into_view_if_needed()

    def subscription_text_is_visible(self):
        expect(self.subscription_text).to_be_visible()

    def fill_subscription_email(self, email):
        self.subscription_email_input.fill(email)

    def click_subscribe_button(self):
        self.subscription_button.click()

    def subscription_successful_text_is_visible(self):
        expect(self.subscription_successful_text).to_be_visible()