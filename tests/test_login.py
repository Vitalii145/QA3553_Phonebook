from selenium import webdriver
from pages.login_page import LoginPage

VALID_EMAIL = 'vitalii.dev2026@outlook.com'
VALID_PASSWORD = 'N7!qR4#vL9@xT2'

def test_login_success(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.fill_email(VALID_EMAIL)
    login_page.fill_password(VALID_PASSWORD)
    login_page.submit_login()

