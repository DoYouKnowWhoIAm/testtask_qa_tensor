from pages.base_page import BasePage
from selenium.webdriver.common.by import By

from logging_utils import log_me


class MainPage(BasePage):
    SBIS_URL = "https://sbis.ru/"
    CONTACTS_MENU = (By.CLASS_NAME, "sbisru-Header-ContactsMenu")
    TENSOR_BANNER = (By.XPATH, "(//a[@href='https://tensor.ru/'])[1]")
    MORE_OFFICES = (By.CLASS_NAME, "sbisru-Header-ContactsMenu__arrow-icon")
    REGION = (By.CLASS_NAME, "sbis_ru-Region-Chooser__text")
    REGION_KAMCHATKA = (By.CSS_SELECTOR, "span[title='Камчатский край']")
    PARTNERS = (By.CLASS_NAME, "sbisru-Contacts-List__name")
    DOWNLOAD_LINK = (By.LINK_TEXT, "Скачать локальные версии")
    PLUGIN_DOWNLOAD = (By.CLASS_NAME, "sbis_ru-DownloadNew-loadLink__link")

    @log_me
    def open_sbis_ru(self):
        self.open_site(self.SBIS_URL)

    @log_me
    def click_to_contacts(self):
        contact_button = self.find_element(self.CONTACTS_MENU)
        contact_button.click()

    @log_me
    def click_more_offices(self):
        more_offices_button = self.find_element(self.MORE_OFFICES)
        more_offices_button.click()

    @log_me
    def click_tensor_banner(self):
        tensor_banner = self.find_element(self.TENSOR_BANNER)
        tensor_banner.click()

    @log_me
    def switch_to_tensor_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @log_me
    def find_region(self):
        return self.find_element(self.REGION)

    @log_me
    def get_region(self):
        return self.find_region().text

    @log_me
    def get_partners(self):
        partners = self.find_elements(self.PARTNERS)
        return [partner.text for partner in partners]

    @log_me
    def change_region(self):
        self.find_region().click()
        self.find_element(self.REGION_KAMCHATKA).click()
        self.wait_text(self.REGION, "Камчатский край")

    @log_me
    def click_download_link(self):
        download_link_button = self.find_element(self.DOWNLOAD_LINK)
        download_link_button.click()

    @log_me
    def download_file(self):
        download_button = self.find_elements(self.PLUGIN_DOWNLOAD)[0]
        download_button.click()
        return float(download_button.text.split(" ")[2])
