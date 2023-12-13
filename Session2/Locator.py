from selenium.webdriver.common.by import By

class SbisSeacrhLocators:
    LOCATOR_URL = "https://sbis.ru/"
    LOCATOR_SBIS_CONTACT = (By.XPATH, '//*[text()= "Контакты"]')
    LOCATOR_SBIS_SEARCH_REGION = (By.XPATH, '//span[@class="sbis_ru-Region-Chooser ml-16 ml-xm-0"]/child::span')
    LOCATOR_SBIS_SEARCH_PARTNER_LIST = (By.XPATH,'//div[@name="itemsContainer" ][1]')
    LOCATOR_SBIS_CHANGE_REGION_KOMCHATCA = (By.XPATH, '//span[@title="Камчатский край"]')
    LOCATOR_SBIS_SERCH_HEADER_REGION = (By.XPATH, '//div[@class="sbis_ru-Region-Panel__header-text"]/child::span')
    LOCATOR_TITLE = (By.XPATH,'/html/head/title')

class TextTest:
    title = "СБИС Контакты — Владимирская область"
    url = "https://sbis.ru/contacts/33-vladimirskaya-oblast?tab=clients"




