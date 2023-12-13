from SbisPage import FindHelper
from Locator import SbisSeacrhLocators



def test_sbis_session2(browser):
    page_sbis = FindHelper(browser, SbisSeacrhLocators.LOCATOR_URL)
    page_sbis.go_to_site()
    page_sbis.click_on_the_contakt()
    assert page_sbis.region_comparison() == 'Владимирская обл.', "Указан не мой регион"
    assert page_sbis.partner_list_serch() == True, "Нет списка партнеров"
    assert page_sbis.change_region() == True
    assert page_sbis.partner_list_serch() == True, "Нет списка партнеров"


