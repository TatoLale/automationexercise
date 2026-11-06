from ui.pages.home_page import HomePage


def test_register_user(page):
    home_page = HomePage(page)

    home_page.open()
    home_page.home_page_is_visible()
    home_page.click_signup_login_button_and_is_visible()
    home_page.fill_name_and_email_fields_and_click_signup(name="GSDS", email="GHSD@gmail.com")
    page.wait_for_timeout(3000)
