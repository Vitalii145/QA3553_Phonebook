import time

from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class ContactsPage(BasePage):
    CONTACT_NAV_LINK = (By.CSS_SELECTOR, "[href='/contacts']")
    CONTACT_CARDS = (By.CLASS_NAME,"contact-item_card__2SOIM")
    EDIT_BUTTON = (By.XPATH, "//button[text()='Edit']")
    EDIT_SAVE_BTN = (By.XPATH, "//button[text()='Save']")
    EDIT_NAME = (By.CSS_SELECTOR, "input[placeholder='Name']")
    EDIT_LAST_NAME = (By.CSS_SELECTOR, "input[placeholder='Last Name']")
    EDIT_PHONE = (By.CSS_SELECTOR, "input[placeholder='Phone']")
    EDIT_EMAIL = (By.CSS_SELECTOR, "input[placeholder='email']")
    EDIT_ADDRESS = (By.CSS_SELECTOR, "input[placeholder='Address']")
    EDIT_DESCRIPTION = (By.CSS_SELECTOR, "input[placeholder='desc']")
    REMOVE_BUTTON = (By.XPATH, "//button[text()='Remove']")

    def open_contact_link(self):
        self.click(self.CONTACT_NAV_LINK)
        WebDriverWait(self.driver, 5).until(
            EC.url_contains("/contacts")
         )
        time.sleep(1)

    def open_contact_details(self,phone):
      locator = (By.XPATH, f"//h3[text()='{phone}']")
      self.click(locator)


    def contact_card_visible(self, phone):
        locator = (By.XPATH, f"//h3[text()='{phone}']")
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(locator))
        return element.is_displayed()


    def contact_cards_count(self, phone):
       return len(self.driver.find_elements(By.XPATH, f"//h3[text()='{phone}']"))


    def open_edit_mode(self):
        self.click(self.EDIT_BUTTON)

    def set_edit_field(self,locator,value):
        self.fill(locator,value)

    def submit_edit(self):
        self.click(self.EDIT_SAVE_BTN)
        time.sleep(3)

    # def submit_new_contact
    def contact_name_for_phone(self, phone):
        card = self.driver.find_element(By.XPATH, f"//h3[text()='{phone}']/..")
        return card.find_element(By.TAG_NAME,"h2").text

    def get_edit_contact(self,locator):
        return self.find(locator).get_attribute("value")

    def click_remove_button(self):
        self.click(self.REMOVE_BUTTON)

    def is_contact_present_by_phone(self, phone):
        time.sleep(3)
        contact_locator = (By.XPATH, f"//h3[text()='{phone}']/..")
        elements = self.driver.find_elements(*contact_locator)
        return len(elements) > 0