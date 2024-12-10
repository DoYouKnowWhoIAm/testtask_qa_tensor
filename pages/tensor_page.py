from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class TensorPage(BasePage):
    POWER_OF_PEOPLE = (By.XPATH, "//p[contains(text(), 'Сила в людях')]")
    ABOUT_BUTTON = (By.XPATH, "(//a[@href='/about'])[2]")
    WORK_PHOTOS = (By.CSS_SELECTOR, "img.tensor_ru-About__block3-image")

    def check_people_strength_block(self):
        return self.find_element(self.POWER_OF_PEOPLE)

    def click_more_details(self):
        more_details_button = self.find_element(self.ABOUT_BUTTON)
        more_details_button.click()

    def check_photos_equal_size(self):
        photos = self.find_elements(self.WORK_PHOTOS)
        photo_sizes = [(photo.get_attribute('width'), photo.get_attribute('height')) for photo in photos]
        return len(set(photo_sizes)) == 1
