from playwright.sync_api import expect

from config import BASE_URL_UI


class LoginPage:
    def __init__(self, page):
        self.page = page

        self.new_user_signup = page.get_by_text("New User Signup!")
        self.input_name = page.get_by_placeholder("Name")
        self.input_email = page.locator('[data-qa="signup-email"]')
        self.signup_button = page.get_by_role("button", name="Signup")

    def open(self):
        self.page.goto(f"{BASE_URL_UI}/login")

    def signup_message_is_visible(self):
        expect(self.new_user_signup).to_be_visible()

    def fill_name_and_email_fields(self, name, email):
        self.input_name.fill(name)
        self.input_email.fill(email)

    def click_signup_button(self):
        self.signup_button.click()
