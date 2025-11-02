from selenium.webdriver.common.by import By
from data.data import *


class Locators:

    ENTER_BUTTON = (By.XPATH, './/*[text()="Вход и регистрация"]') #кнопка «Вход и регистрация»
    NO_ACCOUNT_BUTTON = (By.XPATH, './/*[text()="Нет аккаунта"]') #кнопка «Нет аккаунта»
    EMAIL_INPUT = (By.XPATH, './/*[@name="email"]') #поле ввода email вход и регистрация
    PASS_INPUT = (By.XPATH, './/*[@name="password"]') #поле ввода пароля при регистрации
    AGAIN_PASS_REG_INPUT = (By.XPATH, './/*[@name="submitPassword"]') #поле повтора пароля при регистрации
    CREATE_ACCOUNT_BUTTON = (By.XPATH, './/*[text()="Создать аккаунт"]') #кнопка создания аккаунта
    AVATAR_ON_MAIN = (By.XPATH, './/*[@class="circleSmall"]') #аватар пользователя на главной
    NAME_ON_MAIN = (By.XPATH, './/*[@class="profileText name" and text()="User."]') #имя пользователя на главной
    ERROR_EMAIL_FIELD = (By.XPATH, './/*[@name="email"]/parent::div[@class="input_inputError__fLUP9"]') #поле email при ошибке регистрации
    ERROR_PASS_FIELD = (By.XPATH, './/*[@name="password"]/parent::div[@class="input_inputError__fLUP9"]') #поле пароль при ошибке регистрации
    ERROR_AGAIN_PASS_FIELD = (By.XPATH, './/*[@name="submitPassword"]/parent::div[@class="input_inputError__fLUP9"]') #поле повторный пароль при ошибке регистрации
    ERROR_MESSAGE_REGISTRATION = (By.XPATH,'.//span[text()="Ошибка"]') #сообщение об ошибке при регистрации
    WAIT_RED_BORDER = (By.CSS_SELECTOR, "div.input_inputError__fLUP9")#класс с ошибкой
    LOGIN_BUTTON = (By.XPATH, './/*[text()="Войти"and @type="submit"]') #кнопка Войти
    LOGOUT_BUTTON = (By.XPATH, './/*[text()="Выйти"]') #кнопка Выйти
    ADD_ANNOUNCEMENT_BUTTON = (By.XPATH, '//*[text()="Разместить объявление"]') # кнопка Разместить обьявление без авторизации
    NEED_AUTH_TO_ADD = (By.XPATH, '//*[text()="Чтобы разместить объявление, авторизуйтесь"]') #Чтобы разместить объявление, авторизуйтесь
    PRODUCT_NAME_INPUT = (By.XPATH, './/*[@name="name"]') #поле ввода название
    PRODUCT_DESCRIPTION_INPUT = (By.XPATH, './/textarea[@name="description"]') #поле ввода описание
    PRODUCT_COST_INPUT = (By.XPATH, './/*[@name="price"]') #поле ввода стоимость
    BUTTON_DROPDOWNS = (By.XPATH, '*//button[contains(@class,"dropDownMenu_arrowDown")]')
    CHOOSE_PRODUCT_CATEGORY = (By.XPATH, '//*[text()="Хобби"]') #категория Хобби
    CHOOSE_PRODUCT_CITY = (By.XPATH, '//*[text()="Екатеринбург"]') #город Екатеринбург 
    PRODUCT_CONDITION_BUTTON = (By.XPATH, '//*[@class="radioUnput_inputRegular__FbVbr"]') #выбор состояния БУ
    NAME_H2 = (By.CSS_SELECTOR, "h2.h2")#теги h2
    CHECK_ANN = (By.XPATH, f"//*[text()='{product_name}']")#обьявление с текстом
    PUBLISH_ANNOUNCEMENT_BUTTON = (By.XPATH, '//*[@type="submit" and text()="Опубликовать"]') #кнопка опубликовать
    MY_ANNOUNCEMENT = (By.XPATH, '//*[text()="Мои объявления"]') #мои объявления 
    ARROW_BUTTON = (By.XPATH, '//*[@class="arrowButton arrowButton--right undefined"]')#листать объявления

