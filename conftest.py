import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://telranedu.web.app/")

    yield driver
    driver.quit()


