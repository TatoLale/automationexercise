from playwright.sync_api import expect

from src.pages.base_page import BasePage


class SignUpPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        # ENTER ACCOUNT INFORMATION SECTION

        self.enter_account_information_text = page.get_by_text(
            "Enter Account Information"
        )
        self.input_password = page.locator("#password")
        self.date_of_birth_days = page.locator("#days")
        self.date_of_birth_months = page.locator("#months")
        self.date_of_birth_years = page.locator("#years")
        self.newsletter_check = page.locator("#newsletter")
        self.special_offer_check = page.locator("#optin")

        # ADDRESS INFORMATION SECTION

        self.input_first_name = page.locator("#first_name")
        self.input_last_name = page.locator("#last_name")
        self.input_company = page.locator("#company")
        self.input_address_1 = page.locator("#address1")
        self.input_address_2 = page.locator("#address2")
        self.input_country = page.locator("#country")
        self.input_state = page.locator("#state")
        self.input_city = page.locator("#city")
        self.input_zipcode = page.locator("#zipcode")
        self.input_mobile_number = page.locator("#mobile_number")
        self.create_account_button = page.get_by_role("button", name="Create Account")

    # ENTER ACCOUNT INFORMATION SECTION

    def enter_account_information_is_visible(self):
        expect(self.enter_account_information_text).to_be_visible()

    def fill_account_information(self, title, password, days, months, years):
        self.page.locator(f"input[name='title'][value='{title}']").check()
        self.input_password.fill(password)
        self.date_of_birth_days.select_option(days)
        self.date_of_birth_months.select_option(months)
        self.date_of_birth_years.select_option(years)

    def check_sign_up_for_newsletter(self):
        self.newsletter_check.check()

    def check_special_offers(self):
        self.special_offer_check.check()

    # ADDRESS INFORMATION SECTION

    def fill_address_information(
        self,
        first_name,
        last_name,
        company,
        address_1,
        address_2,
        country,
        state,
        city,
        zipcode,
        mobile_number,
    ):
        self.input_first_name.fill(first_name)
        self.input_last_name.fill(last_name)
        self.input_company.fill(company)
        self.input_address_1.fill(address_1)
        self.input_address_2.fill(address_2)
        self.input_country.select_option(country)
        self.input_state.fill(state)
        self.input_city.fill(city)
        self.input_zipcode.fill(zipcode)
        self.input_mobile_number.fill(mobile_number)

    def click_create_account_button(self):
        self.create_account_button.click()

    def create_account(self, user):
        self.fill_account_information(
            title=user["title"],
            password=user["password"],
            days=user["birth_date"],
            months=user["birth_month"],
            years=user["birth_year"],
        )
        self.fill_address_information(
            first_name=user["firstname"],
            last_name=user["lastname"],
            company=user["company"],
            address_1=user["address1"],
            address_2=user["address2"],
            country=user["country"],
            state=user["state"],
            city=user["city"],
            zipcode=user["zipcode"],
            mobile_number=user["mobile_number"],
        )
        self.click_create_account_button()