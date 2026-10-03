
import pytest
import logging
from faker import Faker
from data.Contact_data import create_contact
from data.contact_datasets import INVALID_CONTACT_FIELDS,SUCCESS_DESCRIPTIONS
from pages.add_contact_page import ContactPage
from pages.contacts_page import ContactsPage

fake = Faker()
logger = logging.getLogger(__name__)


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("description",SUCCESS_DESCRIPTIONS)
def test_add_contact_success_all_fields(authenticated_driver):
    logger.info(f"Testing adding all fields")
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()

    contact_page.create_contact_steps(contact)
    assert contacts_page.contact_card_visible(contact.phone)

def test_add_contact_success_req_fields(authenticated_driver,description):
    logger.info("Test: test_add_contact_success_all_fields")
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)
    contact = create_contact() if description is None else create_contact(description=description)

    logger.info("Testing contact creation: description = %s, phone =%s",
                description,
                contact.phone)
    contact_page.create_contact_steps(contact)
    assert contacts_page.contact_card_visible(contact.phone)

def test_add_contact_empty_name(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)
    contact = create_contact(name="")

    logger.info("Testing contact creation with empty name: phone=%s", contact.phone)

    contact_page.create_contact_steps(contact)
    assert contact_page.is_add_button_active()
    contacts_page.open_contact_link()
    assert contacts_page.contact_cards_count(contact.phone) == 0


def test_add_contact_empty_last_name(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)
    contact = create_contact(last_name="")

    logger.info("Testing contact creation with empty last name: phone=%s", contact.phone)
    assert contact_page.is_add_button_active()
    contacts_page.open_contact_link()
    assert contacts_page.contact_cards_count(contact.phone) == 0

@pytest.mark.xfail (reason = "BUG-123: Contact with empty mail")
def test_add_contact_empty_email(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)
    contact = create_contact(email="")

    logger.info("Testing contact creation with empty email: phone=%s", contact.phone)

    contact_page.create_contact_steps(contact)
    assert contact_page.is_add_button_active()
    contacts_page.open_contact_link()
    assert contacts_page.contact_cards_count(contact.phone) == 0


def test_add_contact_empty_address(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)
    contact = create_contact(address="")

    logger.info("Testing contact creation with empty address: phone=%s", contact.phone)

    contact_page.create_contact_steps(contact)
    assert contact_page.is_add_button_active()
    contacts_page.open_contact_link()
    assert contacts_page.contact_cards_count(contact.phone) == 0

@pytest.mark.regression
@pytest.mark.parametrize("field,value,expected_alert", INVALID_CONTACT_FIELDS)
def test_add_contact_invalid_field_rejected(authenticated_driver,field,value,expected_alert):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)
    contact = create_contact(**{field: value})

    logger.info("Testing invalid contact field: field=%s, phone=%s",
                field,
                contact.phone)
    contact_page.create_contact_steps(contact)
    assert contact_page.get_alert_text().strip() == expected_alert
    contact_page.accept_alert()
    assert contact_page.is_add_button_active()

    contacts_page.open_contact_link()
    assert contacts_page.contact_cards_count(contact.phone) == 0

# def test_add_contact_invalid_phone_too_short(authenticated_driver):
#     contact_page = ContactPage(authenticated_driver)
#     contacts_page = ContactsPage(authenticated_driver)
#     contact = create_contact(phone="0504")
#
#     contact_page.open_contact_form()
#     contact_page.fill_contact_form(contact)
#     contact_page.submit_contact()
#
#     assert contact_page.get_alert_text().strip() == PHONE_ALERT_TEXT
#     contact_page.accept_alert()
#     assert contact_page.is_add_button_active()
#
#     contacts_page.open_contact_link()
#     assert contacts_page.contact_cards_count(contact.phone) == 0
#
# def test_add_contact_invalid_phone_too_long(authenticated_driver):
#     contact_page = ContactPage(authenticated_driver)
#     contacts_page = ContactsPage(authenticated_driver)
#     contact = create_contact(phone=fake.numerify("#"*20))
#
#     contact_page.create_contact_steps(contact)
#
#     assert contact_page.get_alert_text().strip() == PHONE_ALERT_TEXT
#     contact_page.accept_alert()
#     assert contact_page.is_add_button_active()
#
#     contacts_page.open_contact_link()
#     assert contacts_page.contact_cards_count(contact.phone) == 0


# def test_add_contact_invalid_phone_letters(authenticated_driver):
#     contact_page = ContactPage(authenticated_driver)
#     contacts_page = ContactsPage(authenticated_driver)
#     contact = create_contact(phone="jfhkdfghkfdh")
#
#     contact_page.create_contact_steps(contact)
#
#
#     assert contact_page.get_alert_text().strip() == PHONE_ALERT_TEXT
#     contact_page.accept_alert()
#     assert contact_page.is_add_button_active()
#
#     contacts_page.open_contact_link()
#     assert contacts_page.contact_cards_count(contact.phone) == 0
# # @pytest.mark.skip(reason = "Bug-123: Contact with empty mail")
# # @pytest.mark.xfail(reason = "Bug-123: Contact with empty mail")
# def test_add_contact_invalid_email(authenticated_driver):
#     contact_page = ContactPage(authenticated_driver)
#     contacts_page = ContactsPage(authenticated_driver)
#     contact = create_contact(email="invalid_email_format")
#
#     contact_page.open_contact_form()
#     contact_page.fill_contact_form(contact)
#     contact_page.submit_contact()
#
#     assert contact_page.get_alert_text().strip() == EMAIL_ALERT_TEXT
#     contact_page.accept_alert()
#     assert contact_page.is_add_button_active()
#
#     contacts_page.open_contact_link()
#     assert contacts_page.contact_cards_count(contact.phone) == 0
@pytest.mark.xfail(reason="BUG-124: Duplicate phone")
def test_add_contact_duplicate_phone_rejected(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    shared_phone = fake.unique.numerify("05########")
    first_contact = create_contact(phone=shared_phone)
    second_contact = create_contact(phone=shared_phone)

    logger.info("Testing duplicate contact phone: phone=%s", shared_phone)
    contact_page.create_contact_steps(first_contact)
    assert contacts_page.contact_card_visible(shared_phone)

    contact_page.create_contact_steps(second_contact)

    contacts_page.open_contact_link()
    assert contacts_page.contact_cards_count(shared_phone) == 1
