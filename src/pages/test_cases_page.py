from playwright.sync_api import expect

from src.config import BASE_URL_UI
from src.pages.base_page import BasePage


class CasesPage(BasePage):
    def test_cases_page_is_open(self):
        expect(self.page).to_have_url(f"{BASE_URL_UI}/test_cases")
