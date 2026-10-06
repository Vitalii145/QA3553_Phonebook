
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import logging


logger = logging.getLogger(__name__)
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        logger.info(f"click on {locator}")
        self.wait_until_clicable(locator).click()


    def fill(self, locator, value):
        logger.info(f"fill{locator} with {value}")
        element = self.wait_until_visible(locator)
        element.clear()
        element.send_keys(value)

        # self.find(locator).clear()
        # self.find(locator).send_keys(value)

    def get_alert_text(self):
        # alert = WebDriverWait(self.driver, 5).until(
        #    EC.alert_is_present()
        # )
        return self.wait_until_alert_present().text


    def accept_alert(self):
        self.driver.switch_to.alert.accept()


    def wait_until_visible(self,locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(locator))

    def wait_until_clicable(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable(locator))

    def wait_until_url_matches(self,locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.url_matches(locator))

    def wait_until_alert_present(self, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.alert_is_present())