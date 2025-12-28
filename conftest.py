import os
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


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
def driver():
    is_ci = os.getenv("CI") == "true"

    options = Options()
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    if is_ci:
        # ✅ Jenkins / Docker / CI
        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            desired_capabilities=DesiredCapabilities.CHROME,
            options=options,
        )
    else:
        # ✅ Local PyCharm
        driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()
