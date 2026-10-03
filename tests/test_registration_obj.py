import logging
import pytest
from data.user_data import create_user,invalid_email_user,invalid_password_user,exiting_user
from data.user_datasets import INVALID_REGISTRATION_USERS
from pages.registration_page import RegistrationPage

logger = logging.getLogger(__name__)

@pytest.mark.smoke
@pytest.mark.regression

def test_registration_success(driver):
    registration_page = RegistrationPage(driver)
    user = create_user()
    logger.info("Testing successful registration: username=%s", user.username)

    registration_page.open_registration_form()
    registration_page.fill_email(user.username)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()

    assert registration_page.is_registered() is True

@pytest.mark.parametrize("user_factory", INVALID_REGISTRATION_USERS)
def test_registration_invalid_data(driver, user_factory):
    registration_page = RegistrationPage(driver)
    user = user_factory()
    logger.info("Testing invalid registration: case = %s, username=%s",
                user_factory.__name__,
                user.username)
    registration_page.open_registration_form()
    registration_page.fill_email(user.username)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()


    assert "Wrong email or password format" in registration_page.get_alert_text()
    registration_page.accept_alert()


# def test_registration_wrong_password(driver):
#     registration_page = RegistrationPage(driver)
#
#     user = invalid_password_user()
#
#     registration_page.open_registration_form()
#     registration_page.fill_email(user.username)
#     registration_page.fill_password(user.password)
#     registration_page.submit_registration()
#
#     assert "Wrong email or password format" in registration_page.get_alert_text()
#     registration_page.accept_alert()

@pytest.mark.regression
def test_registration_exists_user(driver):
    registration_page = RegistrationPage(driver)

    user = exiting_user()
    logger.info("Testing registration of existing user: username=%s", user.username)
    registration_page.open_registration_form()
    registration_page.fill_email(user.username)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()

    assert registration_page.get_alert_text() == "User already exists"
    registration_page.accept_alert()