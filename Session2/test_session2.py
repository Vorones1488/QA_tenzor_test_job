from SbisPage import FindHelper
from Locator import SbisSeacrhLocators
import logging


def test_sbis_session2(browser):
    page_sbis = FindHelper(browser, SbisSeacrhLocators.LOCATOR_URL)
    page_sbis.go_to_site()
    logging.info('преходим во вкладку контакты')
    page_sbis.click_on_the_contakt()
    logging.info('Проверка своего региона')
    assert page_sbis.region_comparison() == 'Владимирская обл.', "Указан не мой регион"
    logging.info('Проверка есть ли партнеры')
    assert page_sbis.partner_list_serch() == True, "Нет списка партнеров"
    logging.info('Смена региона')
    assert page_sbis.change_region() == True
    logging.info('Проверка есть ли партнеры')
    assert page_sbis.partner_list_serch() == True, "Нет списка партнеров"


