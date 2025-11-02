import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from data.data import *


@pytest.fixture(scope = "function")
def driver():
    options = Options() 
    options.add_argument('--window-size=1920,1080')      
    driver = webdriver.Chrome(options=options)
    driver.get(url_main_page)
    yield driver
    driver.quit() 
