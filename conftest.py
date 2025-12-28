import os
import pytest
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# ======================
# Load .env
# ======================

load_dotenv()


# ======================
# Base URL
# ======================

@pytest.fixture
def base_url():
    return os.getenv("BASE_URL")


# ======================
# Users
# ======================

@pytest.fixture
def valid_user():
    return {
        "email": os.getenv("LOGIN_EMAIL"),
        "password": os.getenv("LOGIN_PASSWORD"),
    }


@pytest.fixture
def invalid_user_credentials():
    return {
        "email": "wrong@example.com",
        "password": "wrong-password",
    }


@pytest.fixture
def not_activated_user():
    """
    Email exists, invitation sent,
    but invite link was NOT opened
    """
    return {
        "email": "not.activated@example.com",
        "password": "some-password",
    }


# ======================
# WebDriver
# ======================

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    yield driver
    driver.quit()
