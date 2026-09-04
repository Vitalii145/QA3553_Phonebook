from faker import Faker
import pytest
from data.Contact_data import create_contact
from pages.add_contact_page import ContactPage
from pages.contacts_page import ContactsPage

fake = Faker()
def test_edit_contact_name_updated(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()
    contact_page.create_contact_steps(contact)
    new_name = fake.first_name()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_field(contacts_page.EDIT_NAME, new_name)
    contacts_page.submit_edit()

    assert contacts_page.contact_name_for_phone(contact.phone) == new_name


def test_edit_contact_last_name_updated(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()
    contact_page.create_contact_steps(contact)
    new_last_name = fake.last_name()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_field(contacts_page.EDIT_LAST_NAME, new_last_name)
    contacts_page.submit_edit()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    assert contacts_page.get_edit_contact(contacts_page.EDIT_LAST_NAME) == new_last_name


def test_edit_contact_phone_updated(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()
    contact_page.create_contact_steps(contact)
    new_phone = fake.unique.numerify("050#######")

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_field(contacts_page.EDIT_PHONE, new_phone)
    contacts_page.submit_edit()

    assert contacts_page.contact_card_visible(new_phone)
    assert contacts_page.contact_cards_count(contact.phone) == 0


def test_edit_contact_email_updated(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()
    contact_page.create_contact_steps(contact)
    new_email = fake.unique.email()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_field(contacts_page.EDIT_EMAIL, new_email)
    contacts_page.submit_edit()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    assert contacts_page.get_edit_contact(contacts_page.EDIT_EMAIL) == new_email


def test_edit_contact_address_updated(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()
    contact_page.create_contact_steps(contact)
    new_address = fake.city()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_field(contacts_page.EDIT_ADDRESS, new_address)
    contacts_page.submit_edit()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    assert contacts_page.get_edit_contact(contacts_page.EDIT_ADDRESS) == new_address


@pytest.mark.skip(reason="BUG-130: Editing description saves literal string '[Object Undefined]'")
def test_edit_contact_description_updated(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()
    contact_page.create_contact_steps(contact)
    new_description = fake.sentence()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_field(contacts_page.EDIT_DESCRIPTION, new_description)
    contacts_page.submit_edit()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    assert contacts_page.get_edit_contact(contacts_page.EDIT_DESCRIPTION) == new_description


def test_edit_contact_empty_name_rejected(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()
    contact_page.create_contact_steps(contact)

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_field(contacts_page.EDIT_NAME, "")
    contacts_page.submit_edit()

    assert contacts_page.contact_name_for_phone(contact.phone) == contact.name


def test_edit_contact_empty_last_name_rejected(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()
    contact_page.create_contact_steps(contact)

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_field(contacts_page.EDIT_LAST_NAME, "")
    contacts_page.submit_edit()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    assert contacts_page.get_edit_contact(contacts_page.EDIT_LAST_NAME) == contact.last_name


def test_edit_contact_empty_phone_updated(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()
    contact_page.create_contact_steps(contact)

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_field(contacts_page.EDIT_PHONE, "")
    contacts_page.submit_edit()

    assert contacts_page.contact_cards_count(contact.phone) == 1


def test_edit_contact_empty_email_rejected(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()
    contact_page.create_contact_steps(contact)

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_field(contacts_page.EDIT_EMAIL, "")
    contacts_page.submit_edit()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    assert contacts_page.get_edit_contact(contacts_page.EDIT_EMAIL) == contact.email


def test_edit_contact_empty_address_rejected(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()
    contact_page.create_contact_steps(contact)

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_field(contacts_page.EDIT_ADDRESS, "")
    contacts_page.submit_edit()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    assert contacts_page.get_edit_contact(contacts_page.EDIT_ADDRESS) == contact.address




@pytest.mark.skip(reason="BUG-124: Duplicate phone")
def test_edit_contact_duplicate_phone_negative(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)
    existing_contact = create_contact()
    other_contact = create_contact()
    contact_page.create_contact_steps(existing_contact)
    contact_page.create_contact_steps(other_contact)

    contacts_page.open_contact_details(other_contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_field(contacts_page.EDIT_PHONE, existing_contact.phone)
    contacts_page.submit_edit()
    assert contacts_page.contact_cards_count(existing_contact.phone) == 1

@pytest.mark.skip
def test_edit_contact_duplicate_email_negative(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    existing_contact = create_contact()
    other_contact = create_contact()

    contact_page.create_contact_steps(existing_contact)
    contact_page.create_contact_steps(other_contact)

    contacts_page.open_contact_details(other_contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_field(contacts_page.EDIT_EMAIL, existing_contact.email)
    contacts_page.submit_edit()

    contacts_page.open_contact_details(other_contact)
    contacts_page.open_edit_mode()
    assert contacts_page.get_edit_contact(contacts_page.EDIT_EMAIL) == other_contact.email


