from selenium import webdriver
from pages.login_page import LoginPage

VALID_EMAIL = 'vitalii.dev2026@outlook.com'
VALID_PASSWORD = 'N7!qR4#vL9@xT2'
INVALID_EMAIL = 'vitalii.dev2026outlook.com'
INVALID_PASSWORD = 'NqR4L9@xT2'

def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.open_login_form()
    login_page.fill_email(VALID_EMAIL)
    login_page.fill_password(VALID_PASSWORD)
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