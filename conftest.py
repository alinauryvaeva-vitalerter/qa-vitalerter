import os
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    remote_url = os.getenv("SELENIUM_REMOTE_URL")

    options = Options()
    # чтобы в CI не нужен был дисплей
    if os.getenv("HEADLESS", "true").lower() == "true":
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    if remote_url:
        drv = webdriver.Remote(command_executor=remote_url, options=options)
    else:
        drv = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    yield drv
    drv.quit()


@pytest.fixture(scope="session")
def user_credentials():
    email = os.getenv("USER_EMAIL")
    password = os.getenv("USER_PASSWORD")
    if not email or not password:
        pytest.skip("USER_EMAIL/USER_PASSWORD not set")
    return email, password
