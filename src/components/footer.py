from playwright.sync_api import expect


class Footer:
    def __init__(self, page):
        self.page = page

        self.footer = page.locator("#footer")
        self.subscription_text = self.footer.get_by_role("heading", name="Subscription")
        self.subscription_email_input = page.locator("#susbscribe_email")
        self.subscription_button = page.locator("#subscribe")
        self.subscription_successful_text = page.locator("#success-subscribe").get_by_text(
            "You have been successfully subscribed!"
        )

    def scroll_down_to_footer(self):
        self.footer.scroll_into_view_if_needed()

    def subscription_text_is_visible(self):
        expect(self.subscription_text).to_be_visible()

    def fill_subscription_email_input(self, email):
        self.subscription_email_input.fill(email)

    def click_subscription_button(self):
        self.subscription_button.click()

    def subscription_successful_text_is_visible(self):
        expect(self.subscription_successful_text).to_be_visible()
