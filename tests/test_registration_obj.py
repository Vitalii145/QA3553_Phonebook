import uuid

from models.users import User
from pages import registration_page
from pages.registration_page import RegistrationPage


def test_registration_success(driver):
    registration_page = RegistrationPage(driver)

    random_suffix = uuid.uuid4().hex[:8]

    user = User(
        f"bond_jeans{random_suffix}@gmail.com",
        "Password456@",
    )

    registration_page.open_registration_form()
    registration_page.fill_email(user.username)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()

    assert registration_page.is_registered() is True


def test_registration_wrong_email(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        "bond_jeansgmail.com",
        "Password456@",
    )

    registration_page.open_registration_form()
    registration_page.fill_email(user.username)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()


    assert "Wrong email or password format" in registration_page.get_alert_text()
    registration_page.accept_alert()


def test_registration_wrong_password(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        "bond_jeans@gmail.com",
        "Passwor56@",
    )

    registration_page.open_registration_form()
    registration_page.fill_email(user.username)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()

    assert "Wrong email or password format" in registration_page.get_alert_text()
    registration_page.accept_alert()

def test_registration_exists_user(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        "vitalii.dev2026@outlook.com",
        "N7!qR4#vL9@xT2",
    )

    registration_page.open_registration_form()
    registration_page.fill_email(user.username)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()

    assert registration_page.get_alert_text() == "User already exists"
    registration_page.accept_alert()