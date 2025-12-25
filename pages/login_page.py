from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    URL = "https://app-dev.vitalerter.com"

    # ----------- LOCATORS -----------

    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name*='username']")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    ERROR_TEXT = (By.CSS_SELECTOR, "span.error-span")

    EMAIL_ERROR_CONTAINER = (By.CSS_SELECTOR, "div.input-wrap.error")
    PASSWORD_ERROR_CONTAINER = (By.CSS_SELECTOR, "div.pwrd-input.error")

    # ----------- INIT -----------

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # ----------- ACTIONS -----------

    def open(self):
        self.driver.get(self.URL)

    def enter_email(self, email: str):
        email_input = self.wait.until(
            EC.visibility_of_element_located(self.EMAIL_INPUT)
        )
        email_input.clear()
        email_input.send_keys(email)
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def enter_password(self, password: str):
        password_input = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        )
        password_input.clear()
        password_input.send_keys(password)
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    # ----------- CHECKS -----------

    def is_logged_in(self) -> bool:
        self.wait.until(EC.url_contains("/monitor"))
        return "/monitor" in self.driver.current_url

    def is_error_text_visible(self) -> bool:
        error = self.wait.until(
            EC.visibility_of_element_located(self.ERROR_TEXT)
        )
        text = error.text.lower()

        return any(word in text for word in [
            "invalid",
            "incorrect",
            "wrong",
            "not secure",
            "not found"
        ])

    def is_email_field_marked_invalid(self) -> bool:
        container = self.driver.find_element(*self.EMAIL_ERROR_CONTAINER)
        return "error" in container.get_attribute("class").lower()

    def is_password_field_marked_invalid(self) -> bool:
        container = self.driver.find_element(*self.PASSWORD_ERROR_CONTAINER)
        return "error" in container.get_attribute("class").lower()

    def is_password_input_visible(self) -> bool:
        return len(self.driver.find_elements(*self.PASSWORD_INPUT)) > 0
