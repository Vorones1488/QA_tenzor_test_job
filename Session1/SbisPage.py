from BaseApp import BasePage
from Locator import SbisSeacrhLocators


class FindHelper(BasePage):
    def click_on_the_contakt(self):
        return self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_CONTACT, time=5).click()

    def find_tenzer_baner(self):
        return self.find_element(SbisSeacrhLocators.LOCATOR_SERCH_BANNER_TENZOR, time=5)

    def click_on_the_baner(self):
        return self.find_element(SbisSeacrhLocators.LOCATOR_SERCH_BANNER_TENZOR, time=5).click()

    def tab_brow_right_and_current_url(self):
        tab = self.driver.window_handles
        self.driver.switch_to.window(tab[1])
        return self.driver.current_url




