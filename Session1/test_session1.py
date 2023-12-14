from SbisPage import FindHelper
from TenzorPage import TenzorPageHelper
from Locator import SbisSeacrhLocators, TenzorSearchLocators
import logging




def test_sbis(browser):
    sbis_page = FindHelper(browser, SbisSeacrhLocators.LOCATOR_URL)
    sbis_page.go_to_site()
    logging.info('преходим во вкладку контакты')
    sbis_page.click_on_the_contakt()
    logging.info('Переход по банеру Тензор')
    sbis_page.find_tenzer_baner()
    logging.info('Убеждаемся что баннер Тензор есть')
    assert sbis_page.find_tenzer_baner().is_displayed()
    logging.info('Переход по баннеру')
    sbis_page.click_on_the_baner()
    sbis_page.tab_brow_right_and_current_url()
    logging.info('Проверка прехода на страницу Тензор')
    assert sbis_page.tab_brow_right_and_current_url() == "https://tensor.ru/"



def test_tenzor(browser,):
    tenzor_page = TenzorPageHelper(browser, TenzorSearchLocators.LOCATOR_URL)
    tenzor_page.go_to_site()
    logging.info('Закрываем куки')
    tenzor_page.close_cooki()  # закрываем всплывающее сообщение о куках
    logging.info('Поиск блока - Сила в людях')
    assert tenzor_page.search_piple_block() == "Сила в людях"
    logging.info('Проверка перехода на по вкладке подробнее')
    assert tenzor_page.clic_in_deteil_piple() == "https://tensor.ru/about"
    logging.info('Проверка наличия картинок')
    assert tenzor_page.search_block_work_and_check() == True #Наличия картинок
    logging.info('Проверка размеров картинок')
    assert tenzor_page.checking_parametrs_img() == True, "все картинки неодного размера" # считываем параметры картинок
    # #assert tenzor_page.checking_parametrs_img() == True
