from selenium import webdriver
import pytest
import logging


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    yield driver
    driver.quit()

@pytest.fixture(autouse=True)
def setup_logging(request):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler('test.log')
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)