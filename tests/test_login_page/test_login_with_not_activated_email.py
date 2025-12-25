from pages.login_page import LoginPage


def test_login_with_not_activated_email(driver):
    """
    Login with email that received invitation
    but was NOT activated via invite link

    Precondition:
    - invitation was sent
    - invite link was NOT opened

    Expected result:
    - error message is shown ("Wrong password")
    """

    page = LoginPage(driver)

    page.open()
    page.enter_email("not_activated_user@test.com")
    page.enter_password("ANY_PASSWORD_123")

    assert page.is_error_text_visible(), \
        "Error message is not shown for not activated email"

    assert page.is_password_field_marked_invalid(), \
        "Password field is not marked invalid"
