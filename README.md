# AutomationExercise – API & UI Test Automation

Test automation project for [automationexercise.com](https://automationexercise.com), a demo e-commerce site built for testing practice.

The project covers the site's public API and its UI test cases, using Python, pytest, Requests and Playwright with the Page Object Model.

[![Tests](https://github.com/TatoLale/automationexercise/actions/workflows/tests.yml/badge.svg)](https://github.com/TatoLale/automationexercise/actions/workflows/tests.yml)

> **Status:** work in progress. All 14 API scenarios are automated; UI test cases are being added (1–13 of 26 done so far).
> The project changes often, so parts of this README may be out of date.

## Tech stack

- Python 3.11
- pytest
- Requests (API tests)
- Playwright + pytest-playwright (UI tests)
- python-dotenv (credentials)
- pytest-xdist (parallel runs)
- pytest-rerunfailures (retries when the site is overloaded)
- Allure (reports)
- GitHub Actions (CI)

## Project structure

```
automationexercise/
├── .github/workflows/
│   └── tests.yml                 # CI pipeline + Allure report on GitHub Pages
├── src/
│   ├── components/               # parts shared by many pages
│   │   ├── header.py             # top menu
│   │   ├── footer.py             # footer + subscription
│   │   ├── product_list.py       # product cards grid
│   │   └── cart_modal.py         # "Added!" popup
│   ├── pages/                    # page objects, all inherit BasePage
│   │   ├── base_page.py          # gives every page .header and .footer
│   │   └── ...                   # home, login, signup, products, cart, ...
│   ├── config.py                 # base URLs, reads credentials from .env
│   └── test_data.py              # generates unique user data
├── tests/
│   ├── api/
│   │   ├── api_1/ ... api_14/    # one folder per API scenario
│   │   └── conftest.py           # fixtures: base URL, credentials, test users
│   └── ui/
│       ├── test_case_1_.../      # one folder per UI test case
│       ├── test_files/           # files for upload tests
│       └── conftest.py           # fixtures: test users, ad blocking
├── .env.example                  # template for local credentials
├── pytest.ini
└── requirements.txt
```

### Page Object Model with components

Every page object inherits `BasePage`, so the header menu and footer are available on any page:

```python
home_page.header.click_products_link()
cart_page.footer.fill_subscription_email_input(email)
```

Blocks that appear on several pages (product grid, cart popup) are components attached to the pages that have them:

```python
products_page.products.hover_on_product(index=0)
products_page.cart_modal.click_view_cart_link()
```

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

- **Status codes:** this API always returns HTTP 200 and puts the real result code in the response body (`responseCode`). Tests assert both, so this behavior is documented in the tests.
- **Test users:** API 11–14 never depend on a shared account. Fixtures create a user with a unique email (via `uuid`) before the test and delete it afterwards, even if the test fails.
- **Assertions:** messages are checked with exact matches (`==`), not substring checks.
- **Credentials** are read from `.env`, which is not committed. In CI they come from GitHub Secrets.
- **CI:** all tests run automatically with GitHub Actions on every push to `main` and on every Pull Request.

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
pytest tests/api -v            # API tests
pytest tests/ui -v --headed    # UI tests, with a visible browser
pytest -n 4                    # everything, in 4 parallel workers
```

### Allure report

```bash
pytest
allure serve allure-results
```