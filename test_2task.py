from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome

import time
import pytest


@pytest.fixture
def browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test2_open_browser(browser):
    browser.get("https://sbis.ru/")
    # time.sleep(5)
    # переходим на сайт компании Тензор
    contacts_path = './/div[contains(@class, "sbisru-Header-ContactsMenu js-ContactsMenu")]'
    contacts = browser.find_element(By.XPATH, contacts_path)
    contacts.click()
    # time.sleep(10)
    # my_region_path = './/span[text()="Нижегородская обл."]'
    # my_region = browser.find_element(By.XPATH, my_region_path)

    regions_contacts_path = './/a[@href = "/contacts"]'
    regions_contacts = browser.find_element(By.XPATH, regions_contacts_path).get_attribute('href')
    browser.get(regions_contacts)
    # time.sleep(10)
    my_region_path = './/span[text()="Нижегородская обл."]'
    my_region = browser.find_element(By.XPATH, my_region_path)
    # assert len(my_region) > 0

    partners_contacts_path = './/i[@title="Сертифицированный партнер"]'
    partners_contacts = browser.find_element(By.XPATH, partners_contacts_path)
    # browser.get(partners_contacts)
    # assert len(partners_contacts) > 0
    my_region.click() # переходим на вкладку с контактами всех регионов

    kamchatka_path = './/span[@title="Камчатский край"]'
    kamchatka_region = browser.find_element(By.XPATH, kamchatka_path)
    kamchatka_region.click()
    time.sleep(10)
