import pytest
from selenium import webdriver
import logging
from data.Contact_data import create_contact
from data.user_data import exiting_user
from pages.add_contact_page import ContactPage
from pages.contacts_page import ContactsPage
from pages.login_page import LoginPage
from utils.logger_config import configure_logging

configure_logging()
logger = logging.getLogger(__name__)


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://telranedu.web.app/")

    yield driver
    driver.quit()


@pytest.fixture
def authenticated_driver(driver):
    # driver = webdriver.Chrome()
    # driver.implicitly_wait(5)

    user = exiting_user()
    login_page = LoginPage(driver)
    login_page.open_login_form()
    login_page.fill_email(user.username)
    login_page.fill_password(user.password)
    login_page.submit_login()

    return driver

@pytest.fixture
def ensure_min_contacts(authenticated_driver):
    contacts_page = ContactsPage(authenticated_driver)
    contact_page = ContactPage(authenticated_driver)

    contacts_page.open_contact_link()
    while contacts_page.total_contacts_count() < 3:
        contact_page.create_contact_steps(create_contact())
        contacts_page.open_contact_link()

    return authenticated_driver

