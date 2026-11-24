import allure

from src.pages.home_page import HomePage
from src.pages.category_products_page import CategoryProductsPage
from tests.ui.base_test import BaseUITest


@allure.story("Products")
class TestViewCategoryProducts(BaseUITest):
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test Case 18: View Category Products")
    def test_view_category_products(self, page):
        home_page = HomePage(page)
        category_products_page = CategoryProductsPage(page)

        with allure.step("Navigate to url"):
            home_page.open()
        with allure.step("Verify that categories are visible on left side bar"):
            home_page.sidebar.category_sidebar_is_visible()
        with allure.step("Click on 'Women' category"):
            home_page.sidebar.click_category(name="Women")
        with allure.step(
            "Click on any category link under 'Women' category, for example: Dress"
        ):
            home_page.sidebar.click_subcategory(category="Women", name="Dress")

        with allure.step(
            "Verify that category page is displayed and confirm text 'WOMEN - DRESS PRODUCTS'"
        ):
            category_products_page.category_page_is_open()
            category_products_page.category_text_is(text="Women - Dress Products")
        with allure.step(
            "On left side bar, click on any sub-category link of 'Men' category"
        ):
            category_products_page.sidebar.click_category(name="Men")
            category_products_page.sidebar.click_subcategory(
                category="Men", name="Tshirts"
            )
        with allure.step("Verify that user is navigated to that category page"):
            category_products_page.category_page_is_open()
            category_products_page.category_text_is(text="Men - Tshirts Products")
