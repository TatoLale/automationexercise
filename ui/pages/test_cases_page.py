from playwright.sync_api import expect

from config import BASE_URL_UI


class CasesPage:
    def __init__(self, page):
        self.page = page

        self.test_cases_text = page.get_by_role("heading", name="Test Cases")

    def open(self):
        self.page.goto(BASE_URL_UI)

    def test_cases_text_is_visible(self):
        expect(self.page).to_have_url(f"{BASE_URL_UI}/test_cases")
