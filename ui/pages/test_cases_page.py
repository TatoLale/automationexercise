from playwright.sync_api import expect

from config import BASE_URL_UI


class CasesPage:
    def __init__(self, page):
        self.page = page

    def test_cases_text_is_visible(self):
        expect(self.page).to_have_url(f"{BASE_URL_UI}/test_cases")
