from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import pytest


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    yield driver
    driver.quit()







