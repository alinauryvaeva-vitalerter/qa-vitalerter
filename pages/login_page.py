from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LoginPage:
    def __init__(self, driver, base_url: str):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 15)

    # ======================
    # Locators
    # ======================

    EMAIL_INPUT = (By.XPATH, "//input[@type='email']")
    NEXT_BUTTON = (By.XPATH, "//button[.//text()[contains(., 'Next')]]")

    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    SIGN_IN_BUTTON = (By.XPATH, "//button[.//text()[contains(., 'Sign in')]]")

    PASSWORD_REQUIRED_ERROR = (
        By.XPATH,
        "//*[contains(text(), 'required') or contains(text(), 'Password')]"
    )

    NOT_ACTIVATED_ERROR = (
        By.XPATH,
        "//*[contains(text(), 'activate') or contains(text(), 'not activated')]"
    )

    # ======================
    # Navigation
    # ======================

    def open(self):
        self.driver.get(self.base_url)

    # ======================
    # Actions
    # ======================

    def enter_email(self, email: str):
        el = self.wait.until(
            EC.visibility_of_element_located(self.EMAIL_INPUT)
        )
        el.clear()
        el.send_keys(email)

    def click_next(self):
        self.wait.until(
            EC.element_to_be_clickable(self.NEXT_BUTTON)
        ).click()

    def enter_password(self, password: str):
        el = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        )
        el.clear()
        el.send_keys(password)

    def click_sign_in(self):
        self.wait.until(
            EC.element_to_be_clickable(self.SIGN_IN_BUTTON)
        ).click()

    # ======================
    # State checks (KEY!)
    # ======================

    def is_password_input_visible(self) -> bool:
        try:
            self.wait.until(
                EC.visibility_of_element_located(self.PASSWORD_INPUT)
            )
            return True
        except TimeoutException:
            return False

    def is_password_required_error_visible(self) -> bool:
        try:
            self.wait.until(
                EC.visibility_of_element_located(self.PASSWORD_REQUIRED_ERROR)
            )
            return True
        except TimeoutException:
            return False

    def is_not_activated_error_visible(self) -> bool:
        try:
            self.wait.until(
                EC.visibility_of_element_located(self.NOT_ACTIVATED_ERROR)
            )
            return True
        except TimeoutException:
            return False

    def is_still_on_login_page(self) -> bool:
        return "/login" in self.driver.current_url
