from BaseApp1 import BasePage
from selenium.webdriver.common.by import By

# webpage class

class TenzorLocators:
    TENZOR_BUNNER = (By.XPATH, './/a[@title = "tensor.ru"]')
    MORE_DETAILS = (By.XPATH, './/a[@href = "/about" and text()="Подробнее"]')
    WORKING_BLOCK = (By.XPATH, './/p[contains(@class, "tensor_ru-Index__card-title tensor_ru-pb-16") and contains(text(),'
                               '"Сила в людях")]')
    PHOTOS_BLOCK = (By.XPATH, './/div[contains(@class, "tensor_ru-container tensor_ru-section tensor_ru-About__block3")]')


class SearchHelper(BasePage):

    def open_tenzor_main_page(self):
        tenzor_link = self.find_element(TenzorLocators.TENZOR_BUNNER).get_attribute("href")
        tenzor_webpage = self.driver.get(tenzor_link)
        return tenzor_link

    def move_to_more_details_link(self):
        more_details_link = self.find_element(TenzorLocators.MORE_DETAILS).get_attribute("href")
        more_details_page = self.driver.get(more_details_link)
        return more_details_link

    def check_working_block(self):
        working_block = self.find_element(TenzorLocators.WORKING_BLOCK)
        return working_block.text

# check photos size in working block
    def check_photos_size(self):
        photos_block = self.find_element(TenzorLocators.PHOTOS_BLOCK)
        photos = photos_block.find_elements(By.TAG_NAME, 'img')
        photos_list = []
        for photo in photos:
            photos_list.append(photo.size)
        print(photos_list)
        index = 0
        while index < len(photos_list) - 1:

            if (photos_list[index].get('height') != photos_list[index + 1].get('height') or
                    photos_list[index].get('width') != photos_list[index + 1].get('width')):
                index += 1
                return 'Фото не одного размера'
            else:
                index += 1
                return 'Фото одного размера'


