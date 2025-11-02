import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data.locators import Locators
from data.data import *

class TestAuthorization:

    def test_success_authorization(self, driver):  #фейловый тест, так как остается url с авторизации вместо https://qa-desk.stand.praktikum-services.ru/
        
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.EMAIL_INPUT))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(exist_login)
        driver.find_element(*Locators.PASS_INPUT).send_keys(password)
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.LOGIN_BUTTON).click() 
        WebDriverWait(driver, 3).until_not(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))    
        assert driver.current_url == url_main_page
    
    @pytest.mark.parametrize(
            'user_data',
            [
                Locators.AVATAR_ON_MAIN, 
                Locators.NAME_ON_MAIN
            ])
    def test_success_authorization_avatar_name(self, driver, user_data): 
        
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.EMAIL_INPUT))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(exist_login)
        driver.find_element(*Locators.PASS_INPUT).send_keys(password)
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.LOGIN_BUTTON).click() 
        WebDriverWait(driver, 3).until_not(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        assert driver.find_element(*user_data)

    @pytest.mark.parametrize(
            'field_locator',
            [
                Locators.NAME_ON_MAIN, 
                Locators.AVATAR_ON_MAIN
            ])
    def test_success_logout_no_user_name_and_avatar(self, driver, field_locator):

        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.EMAIL_INPUT))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(exist_login)
        driver.find_element(*Locators.PASS_INPUT).send_keys(password)
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.LOGOUT_BUTTON))
        driver.find_element(*Locators.LOGOUT_BUTTON).click() 
        WebDriverWait(driver, 3).until_not(expected_conditions.visibility_of_element_located(field_locator)) 
        assert driver.find_element(*Locators.ENTER_BUTTON)
