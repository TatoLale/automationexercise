from playwright.sync_api import expect

from config import BASE_URL_UI


class ContactUsPage:
    def __init__(self, page):
        self.page = page

        self.get_in_touch_text = page.get_by_text("Get In Touch")
        self.name_input = page.locator('[data-qa="name"]')
        self.email_input = page.locator('[data-qa="email"]')
        self.subject_input = page.locator('[data-qa="subject"]')
        self.text_area_input = page.locator('[data-qa="message"]')
        self.choose_file_input = page.locator('input[name="upload_file"]')
        self.submit_button = page.get_by_role("button", name="submit")
        self.success_message_text = page.locator(".status.alert-success")
        self.home_link = page.locator("#form-section").get_by_role("link", name="Home")

    def get_in_touch_text_is_visible(self):
        expect(self.get_in_touch_text).to_be_visible()

    def fill_name_input(self, name):
        self.name_input.fill(name)

    def fill_email_input(self, email):
        self.email_input.fill(email)

    def fill_subject_input(self, subject):
        self.subject_input.fill(subject)

    def fill_text_area_input(self, text_area):
        self.text_area_input.fill(text_area)

    def upload_file(self, file):
        self.choose_file_input.set_input_files(file)

    def accept_dialog(self):
        self.page.once("dialog", lambda dialog: dialog.accept())

    def click_submit_button(self):
        self.page.wait_for_load_state("load")
        self.submit_button.click()

    def success_message_text_is_visible(self):
        expect(self.success_message_text).to_be_visible()

    def click_home_page_button(self):
        self.home_link.click()
