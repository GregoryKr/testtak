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
    partners_quantity_nn = sbis_main_page.find_partners_block_nn()
    assert len(partners_quantity_nn) > 0
    sbis_main_page.click_my_region()
    time.sleep(3)
    kamchatka_region = sbis_main_page.find_kamchatka_region()
    assert kamchatka_region == "41 Камчатский край"
    sbis_main_page.find_kamchatka_link()
    time.sleep(5)
    partners_quantity_kamchatka = sbis_main_page.find_partners_block_kamchatka()
    assert len(partners_quantity_kamchatka) > 0
    assert partners_quantity_nn != partners_quantity_kamchatka
    url = sbis_main_page.check_url()
    assert '41-kamchatskij-kraj' in url
    webpage_title = sbis_main_page.find_kamchatka_webpage_title()
    assert webpage_title == "СБИС Контакты — Камчатский край"



