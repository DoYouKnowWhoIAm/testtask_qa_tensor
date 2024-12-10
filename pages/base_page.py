from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(self.driver, 10)

    def open_site(self, url):
        return self.driver.get(url)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def wait_text(self, locator, text):
        return self.wait.until(EC.text_to_be_present_in_element(locator, text_=text))
