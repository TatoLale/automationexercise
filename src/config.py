import os

from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

BASE_URL_API = "https://automationexercise.com/api"
BASE_URL_UI = "https://automationexercise.com"
EMAIL = os.getenv("AUTOMATIONEXERCISE_EMAIL")
PASSWORD = os.getenv("AUTOMATIONEXERCISE_PASSWORD")
PROJECT_ROOT = Path(__file__).resolve().parent
TEST_FILES_DIR = PROJECT_ROOT / "ui" / "test_files"
