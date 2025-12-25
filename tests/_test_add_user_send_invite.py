from pages.users_page import UserPage
from pages.navigation import Navigation
import time

def test_add_user_send_invite(logged_in_driver):

    driver = logged_in_driver
    navigation = Navigation(driver)
    users_page = UserPage(driver)

    navigation.go_to_users()
    assert users_page.is_opened()

    users_page.click_add_user()
    users_page.select_user_permission()

    test_email = f"autotesr_user_{int(time.time())}@test.com"
    users_page.enter_email(test_email)
    users_page.send_invite()

    assert users_page.is_invite_sent(), \
        "Invite was not sent"