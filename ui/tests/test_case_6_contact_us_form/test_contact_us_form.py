import allure

from ui.pages.home_page import HomePage
from ui.pages.contact_us_page import ContactUsPage
from ui.base_test import BaseUITest
from config import TEST_FILES_DIR


@allure.story("Contact Us")
class TestContactUsForm(BaseUITest):
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test Case 6: Contact Us Form")
    def test_contact_us_form(self, page):
        home_page = HomePage(page)
        contact_us_page = ContactUsPage(page)

        with allure.step("Navigate to url"):
            home_page.open()
        with allure.step("Verify that home page is visible successfully"):
            home_page.home_page_is_visible()
        with allure.step("Click on 'Contact Us' button"):
            home_page.click_contact_us_link()

        with allure.step("Verify 'GET IN TOUCH' is visible"):
            contact_us_page.get_in_touch_text_is_visible()
        with allure.step("Enter name, email, subject and message"):
            contact_us_page.fill_name_input("TestName")
            contact_us_page.fill_email_input("test@example.com")
            contact_us_page.fill_subject_input("TestSubject")
            contact_us_page.fill_text_area_input("TestText")
        with allure.step("Upload file"):
            contact_us_page.upload_file(TEST_FILES_DIR / "test.pdf")
        # The dialog opens during the Submit click,
        # so the handler must be registered before it.
        with allure.step("Click OK button"):
            contact_us_page.accept_dialog()
        with allure.step("Click 'Submit' button"):
            contact_us_page.click_submit_button()
        with allure.step(
            "Verify success message 'Success! Your details have been submitted successfully.' is visible"
        ):
            contact_us_page.success_message_text_is_visible()
        with allure.step(
            "Click 'Home' button and verify that landed to home page successfully"
        ):
            contact_us_page.click_home_page_button()
            home_page.home_page_is_visible()
