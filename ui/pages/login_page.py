from playwright.sync_api import expect

from config import BASE_URL_UI


class LoginPage:
    def __init__(self, page):
        self.page = page

        self.new_user_signup = page.get_by_text("New User Signup!")
        self.input_name = page.get_by_placeholder("Name")
        self.input_email = page.locator('[data-qa="signup-email"]')
        self.signup_button = page.get_by_role("button", name="Signup")
        self.login_to_your_account = page.get_by_text("Login to your account")
        self.input_registered_email = page.locator('[data-qa="login-email"]')
        self.input_registered_password = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.incorrect_login_text = page.get_by_text(
            "Your email or password is incorrect!"
        )

    def open(self):
        self.page.goto(f"{BASE_URL_UI}/login")

    def signup_message_is_visible(self):
        expect(self.new_user_signup).to_be_visible()

    def fill_name_and_email_fields(self, name, email):
        self.input_name.fill(name)
        self.input_email.fill(email)

    def click_signup_button(self):
        self.signup_button.click()

    def login_message_is_visible(self):
        expect(self.login_to_your_account).to_be_visible()

    def fill_email_and_password_fields(self, email, password):
        self.input_registered_email.fill(email)
        self.input_registered_password.fill(password)

    def click_login_button(self):
        self.login_button.click()

    def incorrect_login_text_is_visible(self):
        expect(self.incorrect_login_text).to_be_visible()