from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


from locators import Locators
from curl import *

class TestAccount:
    def test_transition_to_personal_account(self, login): #переход по клику на «Личный кабинет»
        driver = login
        driver.find_element(*Locators.LK_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(account_url))
        assert driver.current_url == account_url

    def test_transition_from_personal_account_to_constructor(self,login ): #переход по клику из «Личного кабинета» на «Конструктор»
        driver = login
        driver.find_element(*Locators.LK_BUTTON).click()
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))
        assert driver.current_url == main_site


    def test_transition_from_personal_account_to_logo(self, login): # переход из «Личного кабинета» по клику на логотип Stellar Burgers.
        driver = login
        driver.find_element(*Locators.LK_BUTTON).click()
        driver.find_element(*Locators.LOGO_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))
        assert driver.current_url == main_site

    def test_logout(self, login): #выход по кнопке «Выйти» из «Личного кабинета».
        driver = login
        driver.find_element(*Locators.LK_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(account_url))
        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(login_url))
        assert driver.current_url == login_url


