import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data.locators import Locators
from data.data import *


@pytest.fixture(scope = "function")
def driver():
    options = Options() 
    options.add_argument('--window-size=1920,1080')      
    driver = webdriver.Chrome(options=options)
    driver.get(url_main_page)
    yield driver
    driver.quit() 


@pytest.fixture(scope = "function")
def success_registration(driver):
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.ENTER_BUTTON))
    driver.find_element(*Locators.ENTER_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.NO_ACCOUNT_BUTTON))
    driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()
    email = Helpers.make_random_email()
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.PASS_INPUT).send_keys(password)
    driver.find_element(*Locators.AGAIN_PASS_REG_INPUT).send_keys(password)
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.CREATE_ACCOUNT_BUTTON))
    driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()


@pytest.fixture(scope = "function")
def unsuccess_registration(driver):
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.ENTER_BUTTON))
    driver.find_element(*Locators.ENTER_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.NO_ACCOUNT_BUTTON))
    driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()
    email = Helpers.make_random_wrong_email()
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.PASS_INPUT).send_keys(password)
    driver.find_element(*Locators.AGAIN_PASS_REG_INPUT).send_keys(password)
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.CREATE_ACCOUNT_BUTTON))
    driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()


@pytest.fixture(scope = "function")
def exist_user_registration(driver):
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.ENTER_BUTTON))
    driver.find_element(*Locators.ENTER_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.NO_ACCOUNT_BUTTON))
    driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(exist_login)
    driver.find_element(*Locators.PASS_INPUT).send_keys(password)
    driver.find_element(*Locators.AGAIN_PASS_REG_INPUT).send_keys(password)
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.CREATE_ACCOUNT_BUTTON))
    driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()
    

@pytest.fixture(scope = "function")
def user_login(driver):
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.ENTER_BUTTON))
    driver.find_element(*Locators.ENTER_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.EMAIL_INPUT))
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(exist_login)
    driver.find_element(*Locators.PASS_INPUT).send_keys(password)
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.LOGIN_BUTTON))
    driver.find_element(*Locators.LOGIN_BUTTON).click() 
    WebDriverWait(driver, 3).until_not(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))


@pytest.fixture(scope = "function")
def user_logout(driver):
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.ENTER_BUTTON))
    driver.find_element(*Locators.ENTER_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.EMAIL_INPUT))
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(exist_login)
    driver.find_element(*Locators.PASS_INPUT).send_keys(password)
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.LOGIN_BUTTON))
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.LOGOUT_BUTTON))
    driver.find_element(*Locators.LOGOUT_BUTTON).click()