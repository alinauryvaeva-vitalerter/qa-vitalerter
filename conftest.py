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
    options.add_argument("--window-size=1920,1080")
    # Добавляем User-Agent, чтобы сайт не выдавал пустую страницу
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")

    # Подключение к контейнеру Selenium, запущенному в Jenkins
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        options=options
    )
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def user_credentials():
    return {
        "email": os.getenv("EMAIL", "default_test@mail.com"),
        "password": os.getenv("PASSWORD", "default_password")
    }