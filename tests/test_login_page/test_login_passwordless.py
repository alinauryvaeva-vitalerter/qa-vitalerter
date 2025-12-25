from pages.login_page import LoginPage


def test_login_with_wrong_password(driver, user_credentials):
    page = LoginPage(driver)

    page.open()
    page.enter_email(user_credentials["email"])
    page.enter_password("WRONG_PASSWORD_123")

    assert page.is_error_text_visible(), \
        "Password error message is not shown"

    assert page.is_password_field_marked_invalid(), \
        "Password field is not marked invalid"
