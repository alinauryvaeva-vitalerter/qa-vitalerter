from pages.login_page import LoginPage


def test_login_without_password(driver, base_url, valid_user):
    login_page = LoginPage(driver, base_url)
    login_page.open()

    login_page.enter_email(valid_user["email"])
    login_page.click_next()

    login_page.click_sign_in()

    assert "/login" in driver.current_url
