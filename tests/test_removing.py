from faker import Faker
import pytest
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