import random
from faker import Faker
from models.contacts import Contact
from pages import login_page
from pages.add_contact_page import ContactPage

fake = Faker()
def test_add_contact_success_all_fields(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    random_suffix = random.randint(1,1_000_000)
    contact = Contact(
        "Anna",
        "Test",
        f"05012{random_suffix}",
        f"anna_test_{random_suffix}@gmail.com",
        "Kiev",
        "QA lesson contact"
    )

    contact_page.open_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    assert contact_page.contact_card_visible(contact.phone)

def test_add_contact_success_req_fields(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    random_suffix = random.randint(1,1_000_000)
    contact = Contact(
        name=fake.first_name(),
        last_name=fake.last_name(),
        # phone=f"05012{random_suffix}",
        phone=fake.numerify("05##########"),
        email=fake.unique.email(),
        address=fake.street_address(),
        description=fake.sentence(nb_words=5),
    )

    contact_page.open_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    assert contact_page.contact_card_visible(contact.phone)