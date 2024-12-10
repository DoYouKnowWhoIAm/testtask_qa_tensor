from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    SBIS_URL = "https://sbis.ru/"
    CONTACTS_MENU = (By.CLASS_NAME, "sbisru-Header-ContactsMenu")
    TENSOR_BANNER = (By.XPATH, "(//a[@href='https://tensor.ru/'])[1]")
    MORE_OFFICES = (By.CLASS_NAME, "sbisru-Header-ContactsMenu__arrow-icon")
    REGION = (By.CLASS_NAME, "sbis_ru-Region-Chooser__text")
    REGION_KAMCHATKA = (By.CSS_SELECTOR, "span[title='Камчатский край']")
    PARTNERS = (By.CLASS_NAME, "sbisru-Contacts-List__name")

    def open_sbis_ru(self):
        self.open_site(self.SBIS_URL)

    def click_to_contacts(self):
        contact_button = self.find_element(self.CONTACTS_MENU)
        contact_button.click()

    def click_more_offices(self):
        more_offices_button = self.find_element(self.MORE_OFFICES)
        more_offices_button.click()

    def click_tensor_banner(self):
        tensor_banner = self.find_element(self.TENSOR_BANNER)
        tensor_banner.click()

    def switch_to_tensor_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def find_region(self):
        return self.find_element(self.REGION)

    def get_region(self):
        return self.find_region().text

    def get_partners(self):
        partners = self.find_elements(self.PARTNERS)
        return [partner.text for partner in partners]

    def change_region(self):
        self.find_region().click()
        self.find_element(self.REGION_KAMCHATKA).click()
        self.wait_text(self.REGION, "Камчатский край")
