from playwright.sync_api import expect


class ProductList:
    """The product cards grid ("Features Items" / "All Products")."""

    def __init__(self, page):
        self.page = page

        self.product_cards = page.locator(".features_items .product-image-wrapper")

    def products_list_is_visible(self):
        expect(self.product_cards.first).to_be_visible()

    def get_product_name(self, index):
        name = self.product_cards.nth(index).locator(".productinfo p")
        expect(name).to_be_visible()
        return name.inner_text()

    def get_product_price(self, index):
        price = self.product_cards.nth(index).locator(".productinfo h2")
        expect(price).to_be_visible()
        return price.inner_text()

    def hover_on_product(self, index):
        card = self.product_cards.nth(index)
        card.scroll_into_view_if_needed()
        card.hover()

    def click_add_to_cart_overlay(self, index):
        self.product_cards.nth(index).locator(".product-overlay").get_by_text(
            "Add to cart"
        ).click()

    def click_view_product(self, index):
        self.product_cards.nth(index).get_by_role("link", name="View Product").click()
