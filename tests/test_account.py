from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


from locators import Locators
from curl import *

class TestAccount:
    def test_transition_to_personal_account(self, authorize): #переход по клику на «Личный кабинет»
        driver = authorize
        driver.find_element(*Locators.LK_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(ACCOUNT_URL))
        assert driver.current_url == ACCOUNT_URL

    def test_transition_from_personal_account_to_constructor(self,authorize ): #переход по клику из «Личного кабинета» на «Конструктор»
        driver = authorize
        driver.find_element(*Locators.LK_BUTTON).click()
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_SITE))
        assert driver.current_url == MAIN_SITE


    def test_transition_from_personal_account_to_logo(self, authorize): # переход из «Личного кабинета» по клику на логотип Stellar Burgers.
        driver = authorize
        driver.find_element(*Locators.LK_BUTTON).click()
        driver.find_element(*Locators.LOGO_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_SITE))
        assert driver.current_url == MAIN_SITE

    def test_logout(self, authorize): #выход по кнопке «Выйти» из «Личного кабинета».
        driver = authorize
        driver.find_element(*Locators.LK_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(ACCOUNT_URL))
        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))
        assert driver.current_url == LOGIN_URL


