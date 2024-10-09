from sbispages2 import SearchHelper
import time

def test_sbis_page(browser):
    sbis_main_page = SearchHelper(browser)
    sbis_main_page.go_to_site()
    sbis_main_page.contacts_link()
    time.sleep(5)
    sbis_main_page.find_regions_contacts()
    my_region = sbis_main_page.find_my_region()
    assert my_region == "Нижегородская обл."
    sbis_main_page.click_my_region()
    time.sleep(3)
    kamchatka_region = sbis_main_page.find_kamchatka_region()
    assert kamchatka_region == "41 Камчатский край"


