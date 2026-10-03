import logging

from selenium import webdriver
import pytest
from data.user_data import create_user, exiting_user,invalid_email_user,invalid_password_user
from pages.login_page import LoginPage
from data.user_datasets import INVALID_LOGIN_USERS


logger = logging.getLogger(__name__)

@pytest.mark.smoke
@pytest.mark.regression
def test_login_success(driver):
    login_page = LoginPage(driver)
    user = exiting_user()
    logger.info("Successfully logged in:username=%s", user.username)

    login_page.open_login_form()
    login_page.fill_email(user.username)
    login_page.fill_password(user.password)
    login_page.submit_login()


    assert login_page.is_logged_in() is True

@pytest.mark.regression
@pytest.mark.parametrize("user_factory",INVALID_LOGIN_USERS)
def test_login_rejected(driver,user_factory):
    login_page = LoginPage(driver)
    user = user_factory()

    logger.info("Testing rejected login: case = %s, username=%s",
                user_factory.__name__,
                user.username)

    login_page.open_login_form()
    login_page.fill_email(user.username)
    login_page.fill_password(user.password)
    login_page.submit_login()

    assert login_page.get_alert_text() == "Wrong email or password"
    login_page.accept_alert()
# def test_login_with_wrong_email(driver):
#     login_page = LoginPage(driver)
#     login_page.open_login_form()
#     login_page.fill_email(INVALID_EMAIL)
#     login_page.fill_password(VALID_PASSWORD)
#     login_page.submit_login()
#
#
#     assert login_page.get_alert_text() == "Wrong email or password"
#     login_page.accept_alert()

# def test_login_with_wrong_password(driver):
#     login_page = LoginPage(driver)
#     login_page.open_login_form()
#     login_page.fill_email(INVALID_EMAIL)
#     login_page.fill_password(INVALID_PASSWORD)
#     login_page.submit_login()
#
#
#     assert login_page.get_alert_text() == "Wrong email or password"
#     login_page.accept_alert()

# def test_login_with_unregistered_user(driver):
#     login_page = LoginPage(driver)
#     login_page.open_login_form()
#     login_page.fill_email("vitalii.dev2026@outlook.com")
#     login_page.fill_password("N7R4#vL9@xT2")
#     login_page.submit_login()
#
#
#     assert login_page.get_alert_text() == "Wrong email or password"
#     login_page.accept_alert()