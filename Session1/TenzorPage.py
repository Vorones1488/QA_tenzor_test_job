
from Locator import TenzorSearchLocators
from BaseApp import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By





class TenzorPageHelper(BasePage):

    def close_cooki(self):
        self.wait.until(EC.text_to_be_present_in_element(
            (By.TAG_NAME, "body"),
    "Используя официальный сайт tensor.ru, вы даете согласие на работу с cookie и Яндекс.Метрикой для сбора технических данных. ")
                                           )
        return self.find_element(TenzorSearchLocators.LOCATOR_SEARCH_COOKI).click()

    def search_piple_block(self):
        piple_block = self.find_element(TenzorSearchLocators.LOCATOR_SEARSH_BLOK_PIPLE, 10)
        return piple_block.text

    def clic_in_deteil_piple(self):
        click_button = self.find_element(TenzorSearchLocators.LOCATOR_ClICK_DETAIL_PIPLE, 10)
        self.action.move_to_element(click_button)
        print(click_button)
        self.action.click(click_button)
        self.action.perform()
        self.wait.until(EC.text_to_be_present_in_element_attribute(
            (By.ID, 'wasaby-content'), 'application', "TensorRuWasaby/Index")
        )
        return self.driver.current_url

    def search_block_work_and_check(self):
    # Находим блок с картинками
        block_img = self.find_element(TenzorSearchLocators.LOCATOR_SEARCH_BLOk_IMG, 10)
        self.action.move_to_element(block_img)
        img_element = self.find_elements(TenzorSearchLocators.LOCATOR_IMG, 10)
        self.action.perform()
        if img_element:
            return True
        else:
            return False

    def checking_parametrs_img(self):
        block_img = self.find_element(TenzorSearchLocators.LOCATOR_SEARCH_BLOk_IMG, 10)
        self.action.move_to_element(block_img)
        imges = self.find_elements(TenzorSearchLocators.LOCATOR_IMG, 10)
        self.action.perform()
        width_lst = []
        hight_lst = []
        for img in imges:
            widh = img.get_attribute('width')
            hight = img.get_attribute('height')
            width_lst.append(widh)
            hight_lst.append(hight)
            if len(set(width_lst)) == 1 and len(set(hight_lst)) == 1:
                return True
            else:
                return False



