import os
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager

from dotenv import load_dotenv

load_dotenv()


@pytest.fixture
def base_url():
    return os.getenv("BASE_URL")


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
    return {
        "email": "not.activated@example.com",
        "password": "Password123"
    }


@pytest.fixture
def driver():
    use_remote = os.getenv("USE_REMOTE_DRIVER", "false").lower() == "true"

    if use_remote:
        # 🔥 Jenkins / Docker / Selenium
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            options=options,
        )
    else:
        # 💻 Локальный PyCharm
        options = Options()
        options.add_argument("--start-maximized")

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options,
        )

    yield driver
    driver.quit()
