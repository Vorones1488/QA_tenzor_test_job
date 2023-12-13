from selenium.webdriver.common.by import By

class SbisSeacrhLocators:
    LOCATOR_SBIS_CONTACT = (By.XPATH, '//*[text()= "Контакты"]')
    LOCATOR_SERCH_BANNER_TENZOR = (By.CSS_SELECTOR, '[alt^="Раз"]')
    LOCATOR_TABS = 1
    LOCATOR_URL = "https://sbis.ru/"


class TenzorSearchLocators:
    LOCATOR_URL = "https://tensor.ru/"
    LOCATOR_SEARSH_BLOK_PIPLE = (By.XPATH, '//*[contains(text(), "Сила") ]')
    LOCATOR_ClICK_DETAIL_PIPLE = (
        By.XPATH,
        '//div[contains(@class , "tensor_ru-Index__block4-content")]/descendant::*[text()="Подробнее"]'
    )
    LOCATOR_SEARCH_COOKI = (By.XPATH, '//*[@id="container"]/div[3]/div[2]/div[2]')
    LOCATOR_SEARCH_BLOk_IMG = (By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]')
    LOCATOR_IMG = (By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/descendant::img')