from tenzorpage1 import SearchHelper
import time

def test_tenzor_page(browser):
    tenzor_page = SearchHelper(browser)
    tenzor_page.go_to_site()
    time.sleep(3)
    tenzor_page.open_tenzor_main_page()
    time.sleep(5)
    tenzor_page.move_to_more_details_link()
    time.sleep(5)
    tenzor_page.check_working_block()
    tenzor_page.check_photos_size()
    