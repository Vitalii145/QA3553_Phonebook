import random
import pytest
from faker import Faker
from data.Contact_data import create_contact
from models.contacts import Contact
from pages.add_contact_page import ContactPage
from pages.contacts_page import ContactsPage

fake = Faker()
def test_add_contact_success_all_fields(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)
    random_suffix = random.randint(1,1_000_000)
    contact = create_contact()

    contact_page.open_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    assert contacts_page.contact_card_visible(contact.phone)

def test_add_contact_success_req_fields(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)
    contact = create_contact(description="")

    contact_page.open_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    assert contacts_page.contact_card_visible(contact.phone)

PHONE_ALERT_TEXT = "Phone not valid: Phone number must contain only digits! And length min 10, max 15!"
EMAIL_ALERT_TEXT = "Email not valid: must be a well-formed email address"

def test_add_contact_empty_name(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact(name="")

    contact_page.open_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    assert contact_page.is_add_button_active()
    contacts_page.open_contact_link()
    assert contacts_page.contact_cards_count(contact.phone) == 0


def test_add_contact_empty_last_name(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)
    contact = create_contact(last_name="")

    contact_page.open_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    assert contact_page.is_add_button_active()

    contacts_page.open_contact_link()
    assert contacts_page.contact_cards_count(contact.phone) == 0

@pytest.mark.xfail (reason = "BUG-123: Contact with empty mail")
def test_add_contact_empty_email(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)
    contact = create_contact(email="")


    contact_page.open_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    assert contact_page.is_add_button_active()

    contacts_page.open_contact_link()
    assert contacts_page.contact_cards_count(contact.phone) == 0


def test_add_contact_empty_address(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)
    contact = create_contact(address="")

    contact_page.open_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    assert contact_page.is_add_button_active()

    contacts_page.open_contact_link()
    assert contacts_page.contact_cards_count(contact.phone) == 0

def test_add_contact_invalid_phone(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)
    contact = create_contact(phone="0504")

    contact_page.open_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    assert contact_page.get_alert_text().strip() == PHONE_ALERT_TEXT
    contact_page.accept_alert()
    assert contact_page.is_add_button_active()

    contacts_page.open_contact_link()
    assert contacts_page.contact_cards_count(contact.phone) == 0

# @pytest.mark.skip(reason = "Bug-123: Contact with empty mail")
# @pytest.mark.xfail(reason = "Bug-123: Contact with empty mail")
def test_add_contact_invalid_email(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)
    contact = create_contact(email="invalid_email_format")

    contact_page.open_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    assert contact_page.get_alert_text().strip() == EMAIL_ALERT_TEXT
    contact_page.accept_alert()
    assert contact_page.is_add_button_active()

    contacts_page.open_contact_link()
    assert contacts_page.contact_cards_count(contact.phone) == 0

def test_add_contact_duplicate_phone_rejected(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)
    shared_phone = fake.unique.numerify("05########")
    first_contact = create_contact(phone=shared_phone)
    second_contact = create_contact(phone=shared_phone)

    contact_page.open_contact_form()
    contact_page.fill_contact_form(first_contact)
    contact_page.submit_contact()
    assert contacts_page.contact_card_visible(shared_phone)

    contact_page.open_contact_form()
    contact_page.fill_contact_form(second_contact)
    contact_page.submit_contact()

    contacts_page.open_contact_link()
    assert contacts_page.contact_cards_count(shared_phone) == 1
