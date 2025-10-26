from selenium import webdriver
from selenium.webdriver.common.by import By
from data.data import *


class Locators:
    ENTER_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[1]/div/button') #кнопка «Вход и регистрация»
    NO_ACCOUNT_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[3]/button[2]') #кнопка «Нет аккаунта»
    EMAIL_INPUT = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[2]/div[1]/div/div/input') #поле ввода email вход и регистрация
    PASS_INPUT = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[2]/div[2]/div/div/input') #поле ввода пароля при регистрации
    AGAIN_PASS_REG_INPUT = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[2]/div[3]/div/div/input') #поле повтора пароля при регистрации
    CREATE_ACCOUNT_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[3]/button[1]') #кнопка создания аккаунта
    AVATAR_ON_MAIN = (By.XPATH, '//*[@id="root"]/div/div[1]/div/div[1]/button') #аватар пользователя на главной
    NAME_ON_MAIN = (By.XPATH, '//*[@id="root"]/div/div[1]/div/div[1]/div/h3') #имя пользователя на главной
    ERROR_EMAIL_FIELD = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[2]/div[1]/div/div') #поле email при ошибке регистрации
    ERROR_PASS_FIELD = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[2]/div[2]/div/div') #поле пароль при ошибке регистрации
    ERROR_AGAIN_PASS_FIELD = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[2]/div[3]/div/div') #поле повторный пароль при ошибке регистрации
    ERROR_MESSAGE_REGISTRATION = (By.XPATH,'//*[@id="root"]/div/div[2]/div[5]/form/div[2]/div[1]/span') #сообщение об ошибке при регистрации
    LOGIN_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[3]/button[1]') #кнопка Войти
    LOGOUT_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[1]/div/div[1]/div/button') #кнопка Выйти
    ADD_ANNOUNCEMENT_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[1]/div/button[2]') # кнопка Разместить обьявление без авторизации
    ADD_ANNOUNCEMENT_AUTH_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[1]/div/button[1]') # кнопка Разместить обьявление с авторизацией 
    NEED_AUTH_TO_ADD = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[1]/h1') #Чтобы разместить объявление, авторизуйтесь
    PRODUCT_NAME_INPUT = (By.XPATH, '//*[@id="root"]/div/div[2]/div/form/div[2]/div[1]/div/div/input') #поле ввода название
    PRODUCT_DESCRIPTION_INPUT = (By.XPATH, '//*[@id="root"]/div/div[2]/div/form/div[4]/div/textarea') #поле ввода описание
    PRODUCT_COST_INPUT = (By.XPATH, '//*[@id="root"]/div/div[2]/div/form/div[5]/div/div/input') #поле ввода стоимость
    OPEN_PRODUCT_CATEGORY_DROPDOWN = (By.XPATH, '//*[@id="root"]/div/div[2]/div/form/div[2]/div[2]/div[1]/button') #стрелка раскрыть список категорий
    CHOOSE_PRODUCT_CATEGORY = (By.XPATH, '//*[@id="root"]/div/div[2]/div/form/div[2]/div[2]/div[2]/button[4]') #категория Хобби
    OPEN_PRODUCT_CITY_DROPDOWN = (By.XPATH, '//*[@id="root"]/div/div[2]/div/form/div[3]/div[1]/button') #стрелка раскрыт список городов
    CHOOSE_PRODUCT_CITY = (By.XPATH, '//*[@id="root"]/div/div[2]/div/form/div[3]/div[2]/button[4]') #город Екатеринбург 
    PRODUCT_CONDITION_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[2]/div/form/fieldset/div/div[2]/div') #выбор состояния БУ
    PUBLISH_ANNOUNCEMENT_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[2]/div/form/button') #кнопка опубликовать
    GO_TO_PROFILE_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[1]/div/div[1]/button') #кнопка перехода в профиль
    MY_ANNOUNCEMENT = (By.XPATH, '//*[@id="root"]/div/div[2]/div[4]/h1') #мои объявления 
    WAIT_RED_BORDER = (By.CSS_SELECTOR, "div.input_inputError__fLUP9")#класс с ошибкой
    ARROW_BUTTON = (By.XPATH, "/html/body/div/div/div[2]/div[4]/div/div[2]/button[2]")#листать объявления
    NAME_H2 = (By.CSS_SELECTOR, "h2.h2")#теги h2
    CHECK_ANN = (By.XPATH, f"//*[text()='{product_name}']")#обьявление с текстом
    
    