from faker import Faker
import pytest
import logging
from data.Contact_data import create_contact
from pages.add_contact_page import ContactPage
from pages.contacts_page import ContactsPage


fake = Faker()
logger =logging.getLogger(__name__)

def test_edit_contact_name_updated(authenticated_driver):
    logger.info("Запуск теста: test_edit_contact_name_updated")
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()
    contact_page.create_contact_steps(contact)
    new_name = fake.first_name()

    logger.info("Updating contact field: field = name, phone = %s, new_value=%s",
                contact.phone,
                new_name)

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

    logger.info("Updating contact field: field = last_name, phone = %s, new_value=%s",
                contact.phone,
                new_last_name)

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_field(contacts_page.EDIT_LAST_NAME, new_last_name)
    contacts_page.submit_edit()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    assert contacts_page.get_edit_contact(contacts_page.EDIT_LAST_NAME) == new_last_name

@pytest.mark.smoke
@pytest.mark.regression
def test_edit_contact_phone_updated(ensure_min_contacts):
    logger.info("Test: edit_contact_phone_updated")
    contact_page = ContactPage(ensure_min_contacts)
    contacts_page = ContactsPage(ensure_min_contacts)

    contact = create_contact()
    contact_page.create_contact_steps(contact)
    new_phone = fake.unique.numerify("050#######")

    logger.debug(f"Old phone:{contact.phone}")
    logger.debug(f"New phone{new_phone}")
    logger.info("Updating contact field: field = phone, old_phone = %s, new_phone=%s",
                contact.phone,
                new_phone)

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
    logger.info("Updating contact field: field = email, phone = %s, new_value=%s",
                contact.phone,
                new_email)

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
    logger.info("Updating contact field: field = address, phone = %s, new_value=%s",
                contact.phone,
                new_address)

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

    logger.info("Updating contact field: field = description, phone = %s, new_value=%s",
                contact.phone,
                new_description)

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_field(contacts_page.EDIT_DESCRIPTION, new_description)
    contacts_page.submit_edit()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    assert contacts_page.get_edit_contact(contacts_page.EDIT_DESCRIPTION) == new_description

@pytest.mark.regression
def test_edit_contact_empty_name_rejected(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()
    contact_page.create_contact_steps(contact)
    logger.info("Testing empty edited empty name: phone = %s",
                contact.phone,
                )

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

    logger.info("Testing empty edited empty last name: phone = %s",
                contact.phone,
                )

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

    logger.info("Testing empty edited empty phone: phone = %s",
                contact.phone,
                )
    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_field(contacts_page.EDIT_PHONE, "")
    contacts_page.submit_edit()

    assert contacts_page.contact_cards_count(contact.phone) == 1

@pytest.mark.regression
def test_edit_contact_empty_email_rejected(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()
    contact_page.create_contact_steps(contact)
    logger.info("Testing empty edited empty phone: phone = %s",
                contact.phone,
                )

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
    logger.info("Testing empty edited empty address: phone = %s",
                contact.phone,
                )

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

    logger.info("Testing duplicate edited phone: existing_phone=%s, other_phone=%s",
                existing_contact.phone,
                other_contact.phone)

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
    logger.info("Testing duplicate edited email: existing_phone=%s, other_phone=%s",
                existing_contact.phone,
                other_contact.phone)
    contact_page.create_contact_steps(existing_contact)
    contact_page.create_contact_steps(other_contact)

    contacts_page.open_contact_details(other_contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_field(contacts_page.EDIT_EMAIL, existing_contact.email)
    contacts_page.submit_edit()

    contacts_page.open_contact_details(other_contact)
    contacts_page.open_edit_mode()
    assert contacts_page.get_edit_contact(contacts_page.EDIT_EMAIL) == other_contact.email


