from pages.login_page import LoginPage


def test_login_with_wrong_email(driver):
    page = LoginPage(driver)

    page.open()
    page.enter_email("wrong_user_123@vitalerter.com")

    assert page.is_error_text_visible(), \
        "Email error message is not shown"

    assert page.is_email_field_marked_invalid(), \
        "Email field is not marked invalid"

    assert not page.is_password_input_visible(), \
        "Password field should not be visible"
