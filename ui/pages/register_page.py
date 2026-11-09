from playwright.sync_api import expect

from config import BASE_URL_UI


class RegisterPage:
    def __init__(self, page):
        self.page = page
        self.home_link = page.get_by_role("link", name="Home")
        self.signup_login_link = page.get_by_role("link", name="Signup / login")
        self.new_user_signup = page.get_by_text("New User Signup!")
        self.name_field = page.get_by_placeholder("Name")
        self.email_field = page.locator('[data-qa="signup-email"]')
        self.signup_button = page.get_by_role("button", name="Signup")
        self.enter_account_information_text = page.get_by_text("Enter Account Information")
        self.gender_choose_mr = page.locator("#id_gender1")

    def open(self):
        self.page.goto(BASE_URL_UI)

    def home_page_is_visible(self):
        expect(self.home_link).to_have_attribute("style", "color: orange;")

    def click_signup_login_link_button(self):
        self.signup_login_link.click()

    def singup_message_is_visible(self):
        expect(self.new_user_signup).to_be_visible()

    def fill_name_and_email_fields(self, name, email):
        self.name_field.fill(name)
        self.email_field.fill(email)

    def click_signup_button(self):
        self.signup_button.click()

    def enter_account_information_is_visible(self):
        expect(self.enter_account_information_text).to_be_visible()

    def fill_account_information(self):
        self.gender_choose_mr.click()
        
