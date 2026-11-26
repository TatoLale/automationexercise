import allure

from src.pages.home_page import HomePage
from src.pages.products_page import ProductsPage
from src.pages.product_detail_page import ProductDetailPage
from tests.ui.base_test import BaseUITest


@allure.story("Products")
class TestAddReviewOnProduct(BaseUITest):
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test Case 21: Add review on product")
    def test_add_review_on_product(self, page):
        home_page = HomePage(page)
        products_page = ProductsPage(page)
        product_detail_page = ProductDetailPage(page)

        with allure.step("Navigate to url"):
            home_page.open()
        with allure.step("Click on 'Products' button"):
            home_page.header.click_products_link()

        with allure.step("Verify user is navigated to ALL PRODUCTS page successfully"):
            products_page.all_products_page_is_open()
        with allure.step("Click on 'View Product' button"):
            products_page.products.click_view_product(index=0)

        with allure.step("Verify 'Write Your Review' is visible"):
            product_detail_page.write_your_review_text_is_visible()
        with allure.step("Enter name, email and review"):
            product_detail_page.fill_review(
                name="Test", email="Test@example.com", review="TestReview"
            )
        with allure.step("Click 'Submit' button"):
            product_detail_page.click_review_button()
        with allure.step("Verify success message 'Thank you for your review.'"):
            product_detail_page.review_successful_text_is_visible()
