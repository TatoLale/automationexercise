from playwright.sync_api import expect


class OrderTable:
    """Products table on the cart page and in 'Review Your Order' on checkout."""

    def __init__(self, page):
        self.page = page

        self.product_rows = page.locator("#cart_info tbody tr[id^='product-']")

    def products_are_in_cart(self, names):
        expect(self.product_rows).to_have_count(len(names))
        for position, name in enumerate(names):
            expect(
                self.product_rows.nth(position).locator(".cart_description h4")
            ).to_have_text(name)

    def products_prices_quantities_and_totals_are_correct(self, prices, quantities):
        for position, (price, quantity) in enumerate(zip(prices, quantities)):
            row = self.product_rows.nth(position)
            expected_total = int(price.replace("Rs. ", "")) * quantity

            expect(row.locator(".cart_price p")).to_have_text(price)
            expect(row.locator(".cart_quantity button")).to_have_text(str(quantity))
            expect(row.locator(".cart_total p")).to_have_text(f"Rs. {expected_total}")

    def product_quantity_is(self, position, quantity):
        expect(
            self.product_rows.nth(position).locator(".cart_quantity button")
        ).to_have_text(str(quantity))