import os

from pages.sbis_page import MainPage
from pages.tensor_page import TensorPage


class TestScripts:

    def setup_method(self):
        self.main_page = MainPage(self.driver)
        self.tensor_page = TensorPage(self.driver)

    def test_script_one(self):
        self.main_page.open_sbis_ru()
        self.main_page.click_to_contacts()
        self.main_page.click_more_offices()
        self.main_page.click_tensor_banner()
        self.main_page.switch_to_tensor_tab()
        assert self.tensor_page.check_people_strength_block() is not None, "Не найден блок 'Сила в людях'"
        self.tensor_page.click_more_details()
        assert self.driver.current_url == "https://tensor.ru/about", "Не перешли на страницу 'О нас'"
        assert self.tensor_page.check_photos_equal_size(), "Размеры фотографий разные"

    def test_script_two(self):
        self.main_page.open_sbis_ru()
        self.main_page.click_to_contacts()
        self.main_page.click_more_offices()
        region = self.main_page.get_region()
        assert region == "Республика Татарстан"
        partners_my_region = self.main_page.get_partners()
        self.main_page.change_region()
        region = self.main_page.get_region()
        assert region == "Камчатский край"
        partners_new_region = self.main_page.get_partners()
        assert partners_my_region != partners_new_region
        assert "41-kamchatskij-kraj" in self.driver.current_url
        assert "Камчатский край" in self.driver.title
        print(partners_my_region, partners_new_region, self.driver.current_url, self.driver.title)

    def test_script_three(self):
        self.main_page.open_sbis_ru()
        self.main_page.click_download_link()
        expected_size = self.main_page.download_file()
        self.main_page.wait_download(os.getcwd())
        assert os.path.exists(f"{os.getcwd()}/sbisplugin-setup-web.exe")
        assert round(
            os.path.getsize(
                os.path.join(os.getcwd(), "sbisplugin-setup-web.exe")
            ) / (1024 * 1024), 2
        ) == expected_size
