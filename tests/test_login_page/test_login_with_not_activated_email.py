from pages.login_page import LoginPage


def test_login_with_not_activated_email(driver, base_url, not_activated_user):
    """
    Login with email that received invitation
    but was NOT activated via invite link

    Expected result:
    - error message is shown
    """

    login_page = LoginPage(driver, base_url)
    login_page.open()

    login_page.enter_email(not_activated_user["email"])
    login_page.click_next()

    login_page.enter_password(not_activated_user["password"])
    login_page.click_sign_in()

    assert login_page.is_not_activated_error_visible()
