# AutomationExercise – API & UI Test Automation

Test automation project for [automationexercise.com](https://automationexercise.com), a demo e-commerce site built for testing practice.

It covers all 14 scenarios from the site's public API and all 26 UI test cases from its test case list. It's written in Python with pytest, Requests and Playwright, and the UI tests use the Page Object Model with reusable components.

[![Tests](https://github.com/TatoLale/automationexercise/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/TatoLale/automationexercise/actions/workflows/tests.yml)

**Allure report (latest run on `main`):** https://tatolale.github.io/automationexercise/

## Tech stack

- Python 3.11
- pytest
- Requests (API tests)
- Playwright + pytest-playwright (UI tests)
- Allure (reports, published to GitHub Pages)
- pytest-rerunfailures (retries when the site is overloaded)
- pytest-xdist (parallel runs)
- python-dotenv (credentials)
- GitHub Actions (CI)

## Project structure

```
automationexercise/
├── .github/workflows/
│   └── tests.yml                  # CI: tests, Allure report, Playwright traces on failure
├── src/
│   ├── components/                # parts of the site shared by several pages
│   │   ├── header.py              # top menu
│   │   ├── footer.py              # footer + subscription
│   │   ├── sidebar.py             # category and brand lists
│   │   ├── product_list.py        # product cards grid
│   │   ├── cart_modal.py          # "Added!" popup
│   │   └── order_table.py         # products table (cart and checkout)
│   ├── pages/                     # page objects, all inherit BasePage
│   │   ├── base_page.py           # gives every page .header and .footer
│   │   ├── home_page.py
│   │   ├── login_page.py
│   │   ├── signup_page.py
│   │   ├── account_created_page.py
│   │   ├── account_deleted_page.py
│   │   ├── products_page.py
│   │   ├── product_detail_page.py
│   │   ├── category_products_page.py
│   │   ├── brand_products_page.py
│   │   ├── cart_page.py
│   │   ├── checkout_page.py
│   │   ├── payment_page.py
│   │   ├── order_placed_page.py
│   │   ├── contact_us_page.py
│   │   └── test_cases_page.py
│   ├── config.py                  # base URLs, reads credentials from .env
│   └── test_data.py               # generates unique user data
├── tests/
│   ├── api/
│   │   ├── api_1/ ... api_14/     # one folder per API scenario
│   │   └── conftest.py            # fixtures: base URL, credentials, test users
│   └── ui/
│       ├── test_case_1_.../ ...   # one folder per UI test case (1–26)
│       ├── test_files/            # files for upload tests
│       └── conftest.py            # fixtures: test users, ad blocking
├── .env.example                   # template for local credentials
├── pytest.ini
└── requirements.txt
```

## Page Object Model with components

One page object per page (URL) of the site. Every page inherits `BasePage`, so the header menu and footer are available on any page:

```python
home_page.header.click_products_link()
cart_page.footer.fill_subscription_email_input(email)
```

Blocks that appear on several pages are **components**, attached to the pages that have them. The same code then works everywhere the block appears:

```python
home_page.products.hover_on_product(index=0)
products_page.cart_modal.click_view_cart_link()
category_products_page.sidebar.click_subcategory(category="Men", name="Tshirts")
checkout_page.order_table.products_are_in_cart(product_names)
```

Tests only talk to pages, never to components directly, so each line of a test says which page the user is on.

## UI coverage

All 26 test cases from the site's [test case list](https://automationexercise.com/test_cases). In the Allure report they're grouped into stories:

| Story | Test cases |
|---|---|
| Register | 1 Register user · 5 Register user with existing email |
| Login | 2 Login with correct email and password · 3 Login with incorrect email and password · 4 Logout user |
| Contact Us | 6 Contact Us form (with file upload) |
| Navigation | 7 Test Cases page · 25 Scroll up with arrow · 26 Scroll up without arrow |
| Products | 8 All products and product detail · 9 Search product · 18 View category products · 19 View brand products · 21 Add review on product |
| Subscription | 10 Subscription on home page · 11 Subscription on cart page |
| Cart | 12 Add products · 13 Product quantity · 17 Remove products · 20 Cart after login · 22 Add from recommended items |
| Place Order | 14 Register while checkout · 15 Register before checkout · 16 Login before checkout · 23 Address details on checkout · 24 Download invoice |

## API coverage

All scenarios from the site's [API list](https://automationexercise.com/api_list):

| # | Scenario | Expected |
|---|----------|----------|
| 1 | GET all products | 200, products list |
| 2 | POST to products list | 405 |
| 3 | GET all brands | 200, brands list |
| 4 | PUT to brands list | 405 |
| 5 | POST search product | 200, matching products |
| 6 | POST search without parameter | 400 |
| 7 | POST verify login, valid details | 200, "User exists!" |
| 8 | POST verify login, missing email | 400 |
| 9 | DELETE to verify login | 405 |
| 10 | POST verify login, invalid details | 404, "User not found!" |
| 11 | POST create account | 201, "User created!" |
| 12 | DELETE account | 200, "Account deleted!" |
| 13 | PUT update account | 200, "User updated!" (change verified with API 14) |
| 14 | GET user details by email | 200, details match the created user |

## Design notes

### Test data and users
- **No shared accounts:** every test that needs a user gets a fresh one with a unique email (`uuid`). Fixtures create it before the test and delete it afterwards, even if the test fails.
- **Fast setup through the API:** UI tests that need an existing user (for example the login tests) create it through the API instead of clicking through the signup form, so each test only exercises what it's actually testing.
- **Cleanup doesn't assert:** fixture teardowns only clean up. Checking that deletion works is API 12's job, so one problem never shows up as two failures.

### Assertions
- **API status codes:** this API always returns HTTP 200 and puts the real result code in the response body (`responseCode`). Tests check the HTTP status first, then the body.
- **Exact matches:** messages and texts are compared exactly (`==`, `to_have_text`), not as substrings.
- **Screen position:** the scroll tests check `to_be_in_viewport()`, not `to_be_visible()`, because an element scrolled off screen still counts as "visible".

### Handling an unreliable test site
automationexercise.com is a free, heavily used demo site. It's often overloaded, and it sometimes blocks CI runners with a bot check. The framework is built so that site problems are retried and easy to tell apart from real bugs:
- **Targeted reruns:** failing tests are rerun only when the error shows the site was overloaded ("heavy load" or 503), not on every failure. Real bugs fail immediately.
- **Failures that explain themselves:** status codes are checked before parsing JSON, and page methods check that an element is visible before filling or reading it. When the site serves an error page, the failure message shows it.
- **JavaScript timing:** buttons handled by the site's JavaScript (add to cart, search, submit) wait for the page to finish loading before clicking.
- **Ads blocked:** ad network requests are blocked in every UI test, so ads can't cover elements or slow pages down.
- **Traces on failure:** every failing UI test saves a Playwright trace (screenshots, network, DOM). CI uploads them as an artifact.

### Where tests differ from the site's wording
- **Order success message (TC 14, 15, 16, 24):** "Your order has been placed successfully!" only flashes for a moment before the site redirects. The tests verify the order on the "Order Placed!" confirmation page instead, and a comment in each test explains why.
- **Category heading (TC 18):** the site's test case uses Dress as its example but expects the text "WOMEN - TOPS PRODUCTS". The test clicks Dress and checks "Women - Dress Products", and the step text says so.

### Credentials and CI
- **Credentials** are read from `.env`, which is not committed. In CI they come from GitHub Secrets.
- **CI** runs all tests on every push to `main` and on every pull request. The Allure report is published to GitHub Pages and keeps its run history.

## Setup

```bash
git clone https://github.com/TatoLale/automationexercise.git
cd automationexercise

python -m venv .venv
.venv\Scripts\Activate.ps1        # Windows PowerShell
# source .venv/bin/activate       # macOS / Linux

pip install -r requirements.txt
playwright install chromium
```

Copy `.env.example` to `.env` and fill in the credentials of a test account registered on the site:

```
AUTOMATIONEXERCISE_EMAIL=
AUTOMATIONEXERCISE_PASSWORD=
```

## Running tests

```bash
pytest                          # everything
pytest tests/api -v             # API tests
pytest tests/ui -v              # UI tests
pytest tests/ui -v --headed     # UI tests with a visible browser
pytest tests/api -n 4           # API tests in 4 parallel workers
```

Keep UI runs sequential. Several browsers at once overload the site and cause "heavy load" failures that have nothing to do with the tests.

### Allure report

```bash
pytest
allure serve allure-results
```

### Playwright traces

When a UI test fails, its trace is saved under `test-results/`. Open it with:

```bash
playwright show-trace test-results/<test-folder>/trace.zip
```