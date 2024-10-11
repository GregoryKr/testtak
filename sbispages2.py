from BaseApp2 import BasePage
from selenium.webdriver.common.by import By

# webpage class

class SbisLocators:
    CONTACTS = (By.XPATH, './/div[contains(@class, "sbisru-Header-ContactsMenu js-ContactsMenu")]')
    REGIONS_CONTACTS = (By.XPATH, './/a[@href = "/contacts"]')
    MY_REGION = (By.XPATH, './/span[text()="Нижегородская обл."]')
    MY_REGION2 = (By.XPATH,'//div[not(contains(@class, \"sbisru-Footer__data\"))]'
                           '/span[contains(@class,"sbis_ru-Region-Chooser")]'
                           '/span[contains(@class,"sbis_ru-Region-Chooser__text sbis_ru-link") and contains(text(), '
                           '"Нижегородская обл.")]')
    PARTNERS_CONTACTS = (By.XPATH, './/i[@title="Сертифицированный партнер"]')
    PARTNERS_QUANTITY_NN = (By.XPATH, './/div[contains(@class, "sbisru-Contacts-City__item-count sbisru-Contacts__text--md ws-flex-shrink-0")]')
    PARTNERS_QUANTITY_KAMCHATKA = (By.XPATH, './/div[contains(@class, "sbisru-Contacts-City__item-count sbisru-Contacts__text--md ws-flex-shrink-0")]')
    KAMCHATKA_REGION = (By.XPATH, './/span[text()="41 Камчатский край"]')
    # KAMCHATKA_REGION_WEBPAGE_NAME = (By.TAG_NAME, 'title')


class SearchHelper(BasePage):

    def contacts_link(self):
        find_contacts = self.find_element(SbisLocators.CONTACTS)
        find_contacts.click()
        return find_contacts

    def find_regions_contacts(self):
        regions_contacts = self.find_element(SbisLocators.REGIONS_CONTACTS).get_attribute('href')
        contacts_page = self.driver.get(regions_contacts)
        return regions_contacts

    def find_my_region(self):
        my_region = self.find_element(SbisLocators.MY_REGION2)
        return my_region.text

    def find_partners_block_nn(self):
        partners_block = self.find_elements(SbisLocators.PARTNERS_QUANTITY_NN)
        return partners_block

    def click_my_region(self):
        my_region_link = self.find_element(SbisLocators.MY_REGION)
        my_region_link.click()
        return my_region_link

    def find_kamchatka_region(self):
        kamchatka_region = self.find_element(SbisLocators.KAMCHATKA_REGION)
        return kamchatka_region.text

    def find_kamchatka_link(self):
        kamchatka_link = self.find_element_clickable(SbisLocators.KAMCHATKA_REGION)
        kamchatka_link.click()
        return kamchatka_link

    def find_partners_block_kamchatka(self):
        partners_block = self.find_elements(SbisLocators.PARTNERS_QUANTITY_KAMCHATKA)
        return partners_block

    def find_kamchatka_webpage_title(self):
        title = self.driver.title
        print(title)
        return title

    def check_url(self):
        url = self.driver.current_url
        print('Current URL:', url )
        return url

