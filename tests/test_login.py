from selenium import webdriver

from data.user_data import create_user, exiting_user
from pages.login_page import LoginPage



def test_login_success(driver):
    login_page = LoginPage(driver)
    user = exiting_user()
    login_page.open_login_form()
    login_page.fill_email(user.username)
    login_page.fill_password(user.password)
    login_page.submit_login()


    assert login_page.is_logged_in() is True


def test_login_with_wrong_email(driver):
    login_page = LoginPage(driver)
    login_page.open_login_form()
    login_page.fill_email(INVALID_EMAIL)
    login_page.fill_password(VALID_PASSWORD)
    login_page.submit_login()


    assert login_page.get_alert_text() == "Wrong email or password"
    login_page.accept_alert()

def test_login_with_wrong_password(driver):
    login_page = LoginPage(driver)
    login_page.open_login_form()
    login_page.fill_email(INVALID_EMAIL)
    login_page.fill_password(INVALID_PASSWORD)
    login_page.submit_login()


    assert login_page.get_alert_text() == "Wrong email or password"
    login_page.accept_alert()

def test_login_with_unregistered_user(driver):
    login_page = LoginPage(driver)
    login_page.open_login_form()
    login_page.fill_email("vitalii.dev2026@outlook.com")
    login_page.fill_password("N7R4#vL9@xT2")
    login_page.submit_login()


    assert login_page.get_alert_text() == "Wrong email or password"
    login_page.accept_alert()