import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL_API= "https://automationexercise.com/api"
BASE_URL_UI= "https://automationexercise.com/api"
EMAIL = os.getenv("AUTOMATIONEXERCISE_EMAIL")
PASSWORD = os.getenv("AUTOMATIONEXERCISE_PASSWORD")
