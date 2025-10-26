import pytest
import selenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data.locators import Locators
from data.data import *

class TestAuthorization:

    def test_success_authorization(self, driver, user_login):  #фейловый тест, так как остается url с авторизации вместо https://qa-desk.stand.praktikum-services.ru/
        assert driver.current_url == url_main_page

    def test_success_authorization_avatar(self, driver, user_login): 
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.AVATAR_ON_MAIN))  
        assert driver.find_element(*Locators.AVATAR_ON_MAIN)

    def test_success_authorization_user_name(self, driver, user_login):   
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.NAME_ON_MAIN)) 
        assert driver.find_element(*Locators.NAME_ON_MAIN).text == name_on_main_after_authorization

    def test_success_logout_exist_login_button(self, driver, user_logout): 
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER_BUTTON))   
        assert driver.find_element(*Locators.ENTER_BUTTON)

    @pytest.mark.parametrize(
            'field_locator',
            [
                Locators.NAME_ON_MAIN, 
                Locators.AVATAR_ON_MAIN
            ])
    def test_success_logout_no_user_name_and_avatar(self, driver, user_logout, field_locator): 
        WebDriverWait(driver, 3).until_not(expected_conditions.visibility_of_element_located(field_locator)) 
        result = False
        try:
            driver.find_element(*field_locator)
            result = False
        except selenium.common.exceptions.NoSuchElementException:
            result = True
        assert result
