class CartModal:
    """The "Added!" popup shown after adding a product to the cart."""

    def __init__(self, page):
        self.page = page

        self.continue_shopping_button = page.get_by_role(
            "button", name="Continue Shopping"
        )
        self.view_cart_link = page.get_by_role("link", name="View Cart")

    def click_continue_shopping_button(self):
        self.continue_shopping_button.click()

    def click_view_cart_link(self):
        self.view_cart_link.click()
