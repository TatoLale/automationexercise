from src.pages.base_page import BasePage


class PaymentPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.name_on_card_input = page.locator('[data-qa="name-on-card"]')
        self.card_number_input = page.locator('[data-qa="card-number"]')
        self.cvc_input = page.locator('[data-qa="cvc"]')
        self.expiry_month_input = page.locator('[data-qa="expiry-month"]')
        self.expiry_year_input = page.locator('[data-qa="expiry-year"]')
        self.pay_and_confirm_button = page.locator('[data-qa="pay-button"]')


    def fill_payment_details(
        self, name_on_card, card_number, cvc, expiration_month, expiration_year
    ):
        self.name_on_card_input.fill(name_on_card)
        self.card_number_input.fill(card_number)
        self.cvc_input.fill(cvc)
        self.expiry_month_input.fill(expiration_month)
        self.expiry_year_input.fill(expiration_year)

    def click_pay_and_confirm_button(self):
        self.pay_and_confirm_button.click()
