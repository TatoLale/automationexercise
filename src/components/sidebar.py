from playwright.sync_api import expect


class Sidebar:
    def __init__(self, page):
        self.page = page

        self.category_sidebar = page.locator("#accordian")

    def category_sidebar_is_visible(self):
        expect(self.category_sidebar).to_be_visible()

    def click_category(self, name):
        self.page.wait_for_load_state("load")
        self.category_sidebar.locator(f"a[href='#{name}']").click()

    def click_subcategory(self, category, name):
        self.category_sidebar.locator(f"#{category}").get_by_role(
            "link", name=name, exact=True
        ).click()
