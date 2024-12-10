import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(autouse=True)
def driver(request):
    chrome_options = Options()
    prefs = {
        "download.default_directory": os.getcwd(),
        "safebrowsing.enabled": True
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver = driver
    yield
    driver.quit()

