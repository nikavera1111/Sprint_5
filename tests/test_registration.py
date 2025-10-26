import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data.locators import Locators
from data.data import *

class TestRegistration:

    def test_success_registration_url(self, driver, success_registration):   #фейловый тест, так как остается url с авторизации вместо https://qa-desk.stand.praktikum-services.ru/
        assert driver.current_url == url_main_page

    def test_success_registration_avatar(self, driver, success_registration):   
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.AVATAR_ON_MAIN))
        assert driver.find_element(*Locators.AVATAR_ON_MAIN)

    def test_success_registration_user_name(self, driver, success_registration):  
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.NAME_ON_MAIN))
        assert driver.find_element(*Locators.NAME_ON_MAIN).text == name_on_main_after_registration


    @pytest.mark.parametrize(
            'field_locator',
            [
                Locators.ERROR_EMAIL_FIELD, 
                Locators.ERROR_PASS_FIELD,
                Locators.ERROR_AGAIN_PASS_FIELD
            ])
    def test_registration_wrong_email_red_fields(self, field_locator, driver, unsuccess_registration):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.WAIT_RED_BORDER))
        current_field = driver.find_element(*field_locator)
        assert current_field.value_of_css_property("border-color") == red_colour_of_border

    def test_registration_wrong_email_error_message(self, driver, unsuccess_registration):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ERROR_MESSAGE_REGISTRATION))
        assert driver.find_element(*Locators.ERROR_MESSAGE_REGISTRATION).text == error_registration_message

    @pytest.mark.parametrize(
            'field_locator',
            [
                Locators.ERROR_EMAIL_FIELD, 
                Locators.ERROR_PASS_FIELD,
                Locators.ERROR_AGAIN_PASS_FIELD
            ])
    def test_registration_exist_email_red_fields(self, field_locator, driver, exist_user_registration):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.WAIT_RED_BORDER))
        current_field = driver.find_element(*field_locator)
        assert current_field.value_of_css_property("border-color") == red_colour_of_border

    def test_registration_exist_email_error_message(self, driver, exist_user_registration):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ERROR_MESSAGE_REGISTRATION))
        assert driver.find_element(*Locators.ERROR_MESSAGE_REGISTRATION).text == error_registration_message





    



     


        