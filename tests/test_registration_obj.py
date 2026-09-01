import uuid
from data.user_data import create_user,invalid_email_user,invalid_password_user,exiting_user
from models.users import User
from pages import registration_page
from pages.registration_page import RegistrationPage


def test_registration_success(driver):
    registration_page = RegistrationPage(driver)

    user = create_user()

    registration_page.open_registration_form()
    registration_page.fill_email(user.username)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()

    assert registration_page.is_registered() is True

def test_registration_wrong_email(driver):
    registration_page = RegistrationPage(driver)

    user = invalid_email_user()

    registration_page.open_registration_form()
    registration_page.fill_email(user.username)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()


    assert "Wrong email or password format" in registration_page.get_alert_text()
    registration_page.accept_alert()


def test_registration_wrong_password(driver):
    registration_page = RegistrationPage(driver)

    user = invalid_password_user()

    registration_page.open_registration_form()
    registration_page.fill_email(user.username)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()

    assert "Wrong email or password format" in registration_page.get_alert_text()
    registration_page.accept_alert()

def test_registration_exists_user(driver):
    registration_page = RegistrationPage(driver)

    user = exiting_user()

    registration_page.open_registration_form()
    registration_page.fill_email(user.username)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()

    assert registration_page.get_alert_text() == "User already exists"
    registration_page.accept_alert()