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

def test_open_browser(browser):
    browser.get("https://sbis.ru/contacts/")
    # time.sleep(5)
    # переходим на сайт компании Тензор
    tenzor_path = './/a[@title = "tensor.ru"]'
    tenzor_bunner = browser.find_element(By.XPATH, tenzor_path).get_attribute("href")

    assert len(tenzor_bunner) > 0
    assert tenzor_bunner == "https://tensor.ru/"
    browser.get(tenzor_bunner)
    more_details = './/a[@href = "/about" and text()="Подробнее"]'
    button_more_details = browser.find_element(By.XPATH, more_details)
    print(button_more_details)
    # assert len(button_more_details) > 0
    browser.get(button_more_details.get_attribute("href"))
    # time.sleep(5)
    # разыскиваем блок Работаем и фотографии
    working_block_path = './/h2[contains(@class, "tensor_ru-header-h2 tensor_ru-About__block-title")]'
    working_block = browser.find_element(By.XPATH, working_block_path)
    print(working_block.text) # проверяем, что нашли блок работаем
    photos_div_path = './/div[contains(@class, "tensor_ru-container tensor_ru-section tensor_ru-About__block3")]' # path block with photos
    block_photos = browser.find_element(By.XPATH, photos_div_path)
    print(block_photos.tag_name, block_photos.location, block_photos.rect, block_photos.text) # проверяем, что нашли блок с фотографиями
    # working_block_photos_path = './/img[contains(@class, "tensor_ru-About__block3-image new_lazy loaded")]'
    working_block_photos = block_photos.find_elements(By.TAG_NAME, 'img')
    # working_block_photos = block_photos.find_elements(By.XPATH, working_block_photos_path)
    size_of_photos = []
    for i in working_block_photos:
        size_of_photos.append(i.size)
        # print(i.tag_name, i.location, i.rect, i.get_attribute('src'))
    print(f'Размеры фотографий: {size_of_photos}')
    # print(peoples_power.tag_name, peoples_power.location, peoples_power.rect, peoples_power.text)
    index = 0
    while index < len(size_of_photos) - 1:
        # print(photo)
        if (size_of_photos[index].get('height') != size_of_photos[index+1].get('height') or
                size_of_photos[index].get('width') != size_of_photos[index+1].get('width')):
            print('Фото не одного размера')
            index += 1
        else:
            print('Фото одного размера')
            index += 1

    # browser.quit()


# if __name__ == "__main__":
#     open_browser()


