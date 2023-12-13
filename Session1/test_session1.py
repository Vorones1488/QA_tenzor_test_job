from SbisPage import FindHelper
from TenzorPage import TenzorPageHelper
from Locator import SbisSeacrhLocators, TenzorSearchLocators
from time import sleep
import logging


def test_sbis(browser):
    sbis_page = FindHelper(browser, SbisSeacrhLocators.LOCATOR_URL)
    sbis_page.go_to_site()
    sbis_page.click_on_the_contakt()

    sbis_page.find_tenzer_baner()
    assert sbis_page.find_tenzer_baner().is_displayed()

    sbis_page.click_on_the_baner()
    sbis_page.tab_brow_right_and_current_url()
    assert sbis_page.tab_brow_right_and_current_url() == "https://tensor.ru/"


def test_tenzor(browser,):
    tenzor_page = TenzorPageHelper(browser, TenzorSearchLocators.LOCATOR_URL)
    tenzor_page.go_to_site()
    tenzor_page.close_cooki()  # закрываем всплывающее сообщение о куках
    assert tenzor_page.search_piple_block() == "Сила в людях"
    assert tenzor_page.clic_in_deteil_piple() == "https://tensor.ru/about"
    assert tenzor_page.search_block_work_and_check() == True #Наличия картинок

    assert tenzor_page.checking_parametrs_img() == True, "все картинки неодного размера" # считываем параметры картинок
    # #assert tenzor_page.checking_parametrs_img() == True
