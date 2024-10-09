from BaseApp2 import BasePage
from selenium.webdriver.common.by import By

# webpage class

class SbisLocators:
    CONTACTS = (By.XPATH, './/div[contains(@class, "sbisru-Header-ContactsMenu js-ContactsMenu")]')
    REGIONS_CONTACTS = (By.XPATH, './/a[@href = "/contacts"]')
    MY_REGION = (By.XPATH, './/span[text()="Нижегородская обл."]')
    PARTNERS_CONTACTS = (By.XPATH, './/i[@title="Сертифицированный партнер"]')
    KAMCHATKA_REGION = (By.XPATH, './/span[text()="41 Камчатский край"]')


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
        my_region = self.find_element(SbisLocators.MY_REGION)
        return my_region.text

    def find_partners_block(self):
        partners_block = self.find_element(SbisLocators.PARTNERS_CONTACTS)
        return partners_block.text

    def click_my_region(self):
        my_region_link = self.find_element(SbisLocators.MY_REGION)
        my_region_link.click()
        return my_region_link

    def find_kamchatka_region(self):
        kamchatka_region = self.find_element(SbisLocators.KAMCHATKA_REGION)
        return kamchatka_region.text

