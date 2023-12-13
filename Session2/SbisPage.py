from BaseApp import BasePage
from Locator import SbisSeacrhLocators, TextTest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class FindHelper(BasePage):
# Переход на страницу контак
    def click_on_the_contakt(self):
        return self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_CONTACT, time=5).click()

# Поиск надписи региона

    def region_comparison(self):
        find_region = self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_SEARCH_REGION, 5)
        return find_region.text
# Ищем список партнеров
    def partner_list_serch(self):
        find_partner = self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_SEARCH_PARTNER_LIST,5)
        if find_partner:
            return True
        else:
            return False
# Смена региона
    def change_region(self):
        find_regions = self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_SEARCH_REGION, 5)
        print(find_regions)
        self.action.move_to_element(find_regions)
        self.action.click(find_regions)
        self.action.perform()
        self.wait.until(EC.text_to_be_present_in_element(
            (By.XPATH, '//div[@class="sbis_ru-Region-Panel__header-text"]/child::span'),"Выберите свой регион")
        )
        self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_CHANGE_REGION_KOMCHATCA, 5).click()
        url = self.driver.current_url
        title = self.driver.title
        if title == TextTest.title and url == TextTest.url:
            return True
        else:
            return False





    # def find_tenzer_baner(self):
    #     return self.find_element(SbisSeacrhLocators.LOCATOR_SERCH_BANNER_TENZOR, time=5)

    # def click_on_the_baner(self):
    #     return self.find_element(SbisSeacrhLocators.LOCATOR_SERCH_BANNER_TENZOR, time=5).click()

    def tab_brow_right_and_current_url(self):
        tab = self.driver.window_handles
        self.driver.switch_to.window(tab[0])
        return self.driver.current_url




