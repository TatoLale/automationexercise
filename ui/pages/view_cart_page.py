from playwright.sync_api import expect


class ViewCartPage:
    def __init__(self, page):
        self.page = page
