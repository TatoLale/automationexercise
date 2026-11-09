# AutomationExercise – API & UI Test Automation

Test automation project for [automationexercise.com](https://automationexercise.com), a demo e-commerce site built for testing practice.

The project covers the site's public API and its UI test cases, using Python, pytest, Requests and Playwright with the Page Object Model.

[![Tests](https://github.com/TatoLale/automationexercise/actions/workflows/tests.yml/badge.svg)](https://github.com/TatoLale/automationexercise/actions/workflows/tests.yml)

> **Status:** work in progress. All 14 API scenarios are automated; UI test cases are being added.

## Tech stack

- Python 3.11
- pytest
- Requests (API tests)
- Playwright + pytest-playwright (UI tests)
- python-dotenv (credentials)
- pytest-xdist (parallel runs)
- GitHub Actions (CI)

## Project structure

```
automationexercise/
├── .github/workflows/
│   └── tests.yml                # CI pipeline
├── api/
│   ├── tests/
│   │   ├── api_1/ ... api_14/   # one folder per API scenario
│   ├── conftest.py              # fixtures: base URL, credentials, test users
│   └── test_data.py             # generates unique user data
├── ui/
│   ├── pages/                   # page objects
│   └── tests/                   # UI tests, one folder per test case
├── config.py                    # base URLs, reads credentials from .env
├── .env.example                 # template for local credentials
├── pytest.ini
└── requirements.txt
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
pytest api -v                  # API tests
pytest ui -v --headed          # UI tests, with a visible browser
pytest -n 4                    # everything, in 4 parallel workers
```