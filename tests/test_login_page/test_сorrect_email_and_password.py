from pages.login_page import LoginPage


def test_login_positive(driver, user_credentials):
    page = LoginPage(driver)

    page.open()
    page.enter_email(user_credentials["email"])
    page.enter_password(user_credentials["password"])

    assert page.is_logged_in(), "User was not logged in"
