from src.components.footer import Footer
from src.components.header import Header


class BasePage:
    """Every page has the header menu and the footer."""

    def __init__(self, page):
        self.page = page
        self.header = Header(page)
        self.footer = Footer(page)
