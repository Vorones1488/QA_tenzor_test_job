from BaseApp import BasePage
from Locator import SbisSeacrhLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class FindHelper(BasePage):
    # Переход на страницу контакт
    def click_on_the_contakt(self):
        self.wait.until(EC.text_to_be_present_in_element(
            SbisSeacrhLocators.LOCATOR_SBIS_WAIT,
        "Используя официальный сайт sbis.ru, вы даете согласие на работу с cookie и Яндекс.Метрикой для сбора технических данных."))
        return self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_CONTACT, time=5).click()
    # Поискк банера Тензор
    def find_tenzer_baner(self):
        return self.find_element(SbisSeacrhLocators.LOCATOR_SERCH_BANNER_TENZOR, time=5)
    # Переход оп баннеру
    def click_on_the_baner(self):
        return self.find_element(SbisSeacrhLocators.LOCATOR_SERCH_BANNER_TENZOR, time=5).click()
    # считываем url
    def tab_brow_right_and_current_url(self):
        tab = self.driver.window_handles
        self.driver.switch_to.window(tab[1])
        return self.driver.current_url




