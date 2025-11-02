import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data.locators import Locators
from data.data import *
from helpers import Helpers

class TestRegistration:
    
    def test_success_registration_url(self, driver):  #фейловый тест, так как остается url с авторизации вместо https://qa-desk.stand.praktikum-services.ru/

        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.NO_ACCOUNT_BUTTON))
        driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()
        email = Helpers.make_random_email()
        WebDriverWait(driver, 3).until_not(expected_conditions.visibility_of_element_located(Locators.NO_ACCOUNT_BUTTON))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASS_INPUT).send_keys(password)
        driver.find_element(*Locators.AGAIN_PASS_REG_INPUT).send_keys(password)
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()
        assert WebDriverWait(driver, 3).until_not(expected_conditions.visibility_of_element_located(Locators.ENTER_BUTTON))
        assert driver.current_url == url_main_page


    def test_success_registration_avatar_name(self, driver):   
    
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.NO_ACCOUNT_BUTTON))
        driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()
        email = Helpers.make_random_email()
        WebDriverWait(driver, 3).until_not(expected_conditions.visibility_of_element_located(Locators.NO_ACCOUNT_BUTTON))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASS_INPUT).send_keys(password)
        driver.find_element(*Locators.AGAIN_PASS_REG_INPUT).send_keys(password)
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.AVATAR_ON_MAIN))
        assert driver.find_element(*Locators.NAME_ON_MAIN)


    @pytest.mark.parametrize(
            'field_locator',
            [
                Locators.ERROR_EMAIL_FIELD, 
                Locators.ERROR_PASS_FIELD,
                Locators.ERROR_AGAIN_PASS_FIELD
            ])
    def test_registration_wrong_email_red_fields(self, field_locator, driver):
        
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.NO_ACCOUNT_BUTTON))
        driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()
        email = Helpers.make_random_wrong_email()
        WebDriverWait(driver, 3).until_not(expected_conditions.visibility_of_element_located(Locators.NO_ACCOUNT_BUTTON))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASS_INPUT).send_keys(password)
        driver.find_element(*Locators.AGAIN_PASS_REG_INPUT).send_keys(password)
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.CREATE_ACCOUNT_BUTTON))
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.WAIT_RED_BORDER))
        current_field = driver.find_element(*field_locator)
        assert current_field.value_of_css_property("border-color") == red_colour_of_border

    def test_registration_wrong_email_error_message(self, driver):
        
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.NO_ACCOUNT_BUTTON))
        driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()
        email = Helpers.make_random_wrong_email()
        WebDriverWait(driver, 3).until_not(expected_conditions.visibility_of_element_located(Locators.NO_ACCOUNT_BUTTON))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASS_INPUT).send_keys(password)
        driver.find_element(*Locators.AGAIN_PASS_REG_INPUT).send_keys(password)
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ERROR_MESSAGE_REGISTRATION))
        assert driver.find_element(*Locators.ERROR_MESSAGE_REGISTRATION)
    
    @pytest.mark.parametrize(
            'field_locator',
            [
                Locators.ERROR_EMAIL_FIELD, 
                Locators.ERROR_PASS_FIELD,
                Locators.ERROR_AGAIN_PASS_FIELD
            ])
    def test_registration_exist_email_red_fields(self, field_locator, driver):

        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.NO_ACCOUNT_BUTTON))
        driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until_not(expected_conditions.visibility_of_element_located(Locators.NO_ACCOUNT_BUTTON))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(exist_login)
        driver.find_element(*Locators.PASS_INPUT).send_keys(password)
        driver.find_element(*Locators.AGAIN_PASS_REG_INPUT).send_keys(password)
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.CREATE_ACCOUNT_BUTTON))
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.WAIT_RED_BORDER))
        current_field = driver.find_element(*field_locator)
        assert current_field.value_of_css_property("border-color") == red_colour_of_border

    def test_registration_exist_email_error_message(self, driver):

        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.NO_ACCOUNT_BUTTON))
        driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until_not(expected_conditions.visibility_of_element_located(Locators.NO_ACCOUNT_BUTTON))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(exist_login)
        driver.find_element(*Locators.PASS_INPUT).send_keys(password)
        driver.find_element(*Locators.AGAIN_PASS_REG_INPUT).send_keys(password)
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.CREATE_ACCOUNT_BUTTON))
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ERROR_MESSAGE_REGISTRATION))
        assert driver.find_element(*Locators.ERROR_MESSAGE_REGISTRATION).text == error_registration_message