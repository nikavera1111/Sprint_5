from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data.locators import Locators
from data.data import *


class TestAddAnouncement:

    def test_add_announcement_without_auth(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.ADD_ANNOUNCEMENT_BUTTON)) 
        driver.find_element(*Locators.ADD_ANNOUNCEMENT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.NEED_AUTH_TO_ADD)) 
        assert driver.find_element(*Locators.NEED_AUTH_TO_ADD) 

    def test_add_announcement_in_profile(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.ENTER_BUTTON))
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.EMAIL_INPUT))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(exist_login)
        driver.find_element(*Locators.PASS_INPUT).send_keys(password)
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.LOGIN_BUTTON).click() 
        WebDriverWait(driver, 3).until_not(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.ADD_ANNOUNCEMENT_BUTTON).click()        
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PRODUCT_NAME_INPUT)) 
        driver.find_element(*Locators.PRODUCT_NAME_INPUT).send_keys(product_name)
        driver.find_element(*Locators.PRODUCT_DESCRIPTION_INPUT).send_keys(product_description)
        driver.find_element(*Locators.PRODUCT_COST_INPUT).send_keys(product_cost)
        all_dropdown = driver.find_elements(*Locators.BUTTON_DROPDOWNS)
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(all_dropdown[0])).click()
        driver.find_element(*Locators.CHOOSE_PRODUCT_CATEGORY).click()
        WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(all_dropdown[1])).click()
        driver.find_element(*Locators.CHOOSE_PRODUCT_CITY).click()
        driver.find_element(*Locators.PRODUCT_CONDITION_BUTTON).click()
        driver.find_element(*Locators.PUBLISH_ANNOUNCEMENT_BUTTON).click()
        WebDriverWait(driver, 10).until_not(expected_conditions.visibility_of_element_located(Locators.PUBLISH_ANNOUNCEMENT_BUTTON))
        profile = WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.AVATAR_ON_MAIN))
        driver.execute_script("arguments[0].scrollIntoView(true);", profile)
        profile = WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.AVATAR_ON_MAIN))
        profile.click()
        announcement = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(Locators.MY_ANNOUNCEMENT))
        driver.execute_script("arguments[0].scrollIntoView(true);", announcement)
        name_div = None
        while True:
            try:
                WebDriverWait(driver, 60).until(expected_conditions.visibility_of_all_elements_located(Locators.NAME_H2))
                name_div = driver.find_element(*Locators.CHECK_ANN)
                break
            except:
                try:
                    button = WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.ARROW_BUTTON))
                    button.click()
                except:
                    name_div = driver.find_element(*Locators.CHECK_ANN)
                    break

        assert name_div





