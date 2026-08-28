from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class LoginPage(BasePage):

    LOGIN_NAV_LINK = (By.CSS_SELECTOR, "[href='/login']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Login']")
    SIGN_OUT_BUTTON = (By.XPATH, "//*[text()='Sign Out']")

    # def __init__(self, driver):
    #     self.driver = driver

    def open_login_form(self):
        # self.driver.find_element(*self.LOGIN_NAV_LINK).click()
        self.click(self.LOGIN_NAV_LINK)

    def fill_email(self, email):
        # self.driver.find_element(*self.EMAIL_INPUT).clear()
        # self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.fill(self.EMAIL_INPUT, email)


    def fill_password(self, password):
        # self.driver.find_element(*self.PASSWORD_INPUT).clear()
        # self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.fill(self.PASSWORD_INPUT,password)

    def submit_login(self):
        self.click(self.LOGIN_BUTTON)

    # def is_logged(self):
    #     try:
    #         self.driver.find_element(*self.SIGN_OUT_BUTTON)
    #         return True
    #     except NoSuchElementException:
    #         return False

    def is_logged_in(self):
        try:
            WebDriverWait(self.driver, 5).until(
                expected_conditions.visibility_of_element_located(self.SIGN_OUT_BUTTON)
            )
            return True
        except TimeoutException:
            return False

    def get_alert_text(self):
        alert = WebDriverWait(self.driver, 5).until(
            expected_conditions.alert_is_present()
        )
        return alert.text

    def accept_alert(self):
        self.driver.switch_to.alert.accept()
