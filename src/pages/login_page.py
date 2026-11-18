from playwright.sync_api import expect

from src.config import BASE_URL_UI
from src.pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        # NEW USER SIGNUP FORM
        self.new_user_signup = page.get_by_text("New User Signup!")
        self.input_name = page.get_by_placeholder("Name")
        self.input_email = page.locator('[data-qa="signup-email"]')
        self.signup_button = page.get_by_role("button", name="Signup")
        self.email_already_exists_text = page.get_by_text("Email Address already exist!")

        # LOGIN FORM
        self.login_to_your_account = page.get_by_text("Login to your account")
        self.input_registered_email = page.locator('[data-qa="login-email"]')
        self.input_registered_password = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.incorrect_login_text = page.get_by_text(
            "Your email or password is incorrect!"
        )

    def open(self):
        self.page.goto(f"{BASE_URL_UI}/login")

    def login_page_is_open(self):
        expect(self.page).to_have_url(f"{BASE_URL_UI}/login")

    # NEW USER SIGNUP FORM

    def signup_message_is_visible(self):
        expect(self.new_user_signup).to_be_visible()

    def fill_name_and_email_fields(self, name, email):
        self.input_name.fill(name)
        self.input_email.fill(email)

    def click_signup_button(self):
        self.signup_button.click()

    def email_already_exist_text_is_visible(self):
        expect(self.email_already_exists_text).to_be_visible()

    # LOGIN FORM

    def login_message_is_visible(self):
        expect(self.login_to_your_account).to_be_visible()

    def fill_email_and_password_fields(self, email, password):
        self.input_registered_email.fill(email)
        self.input_registered_password.fill(password)

    def click_login_button(self):
        self.login_button.click()

    def incorrect_login_text_is_visible(self):
        expect(self.incorrect_login_text).to_be_visible()
