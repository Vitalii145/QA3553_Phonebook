import time

from faker import Faker
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from data.Contact_data import create_contact
from pages.add_contact_page import ContactPage
from pages.contacts_page import ContactsPage

def test_delete_contact(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()
    contact_page.create_contact_steps(contact)

    contacts_page.open_contact_details(contact.phone)
    contacts_page.click_remove_button()

    assert contacts_page.is_contact_present_by_phone(contact.phone) is False

# def test_delete_one_contact(ensure_min_contacts):
#     contacts_page = ContactsPage(ensure_min_contacts)
#
#     contacts_page.open_contact_link()
#     count_before = contacts_page.total_contacts_count()
#     contacts_page.open_first_contact()
#     contacts_page.click_remove_button()
#     count_after = contacts_page.total_contacts_count()
#     WebDriverWait(ensure_min_contacts, 5).until(
#         lambda driver: contacts_page.total_contacts_count() < count_before
#     )
#     assert count_after == count_before - 1

def test_delete_one_contact(authenticated_driver):
    contacts_page = ContactsPage(authenticated_driver)

    contacts_page.open_contact_link()
    count_before = contacts_page.total_contacts_count()
    contacts_page.open_first_contact()
    time.sleep(1)
    button = authenticated_driver.find_element(*contacts_page.REMOVE_BUTTON)
    authenticated_driver.execute_script("arguments[0].click();", button)
    time.sleep(3)
    contacts_page.open_contact_link()
    time.sleep(2)
    count_after = contacts_page.total_contacts_count()
    print(f"\n--- Было: {count_before}, Стало: {count_after} ---")
    assert count_after == count_before - 1

def test_delete_all_contacts(ensure_min_contacts):
    contacts_page = ContactsPage(ensure_min_contacts)

    contacts_page.open_contact_link()
    contacts_page.remove_all_contacts()
    assert contacts_page.total_contacts_count() == 0

