from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    # Более надежные селекторы
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email'], input[type='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password'], input[type='password']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15) # Увеличили время ожидания

    def open(self):
        self.driver.get("https://app.vitalerter.com/login")

    def enter_email(self, email):
        el = self.wait.until(EC.element_to_be_clickable(self.EMAIL_INPUT))
        el.clear()
        el.send_keys(email)

    def enter_password(self, password):
        el = self.wait.until(EC.element_to_be_clickable(self.PASSWORD_INPUT))
        el.clear()
        el.send_keys(password)

    def click_login(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON))
        btn.click()