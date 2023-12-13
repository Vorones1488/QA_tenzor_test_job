from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains




class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.base_url = url
        self.action = ActionChains(driver)
        self.wait = WebDriverWait(driver, 10)



    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        WebDriverWait(self.driver, 10).until_not(EC.new_window_is_opened(self.base_url))
        return self.driver.get(self.base_url)





