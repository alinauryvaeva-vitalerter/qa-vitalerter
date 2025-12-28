import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Подключаемся к контейнеру selenium, который запущен в Jenkins
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        options=options
    )
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def user_credentials():
    return {
        "email": os.getenv("EMAIL"),
        "password": os.getenv("PASSWORD")
    }