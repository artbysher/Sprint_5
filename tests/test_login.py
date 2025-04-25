from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import Credentials
from locators import Locators
from curl import *

class TestLogin:

    def test_login_via_personal_account_button(self,driver):#Вход через кнопку «Личный кабинет»
        driver.find_element(*Locators.LK_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.LK_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(ACCOUNT_URL))
        assert driver.current_url == ACCOUNT_URL


    def test_login_via_main_page_login_button(self, driver):# Вход по кнопке «Войти в аккаунт» на главной
        driver.find_element(*Locators.MAIN_PAGE_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        order_batten = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert order_batten.is_displayed()

    def test_login_via_registration_form_button(self, driver):#Вход через кнопку в форме регистрации

        driver.find_element(*Locators.LK_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.REG_LOG_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_SITE))
        assert driver.current_url == MAIN_SITE

    def test_login_via_password_recovery_form_button(self, driver):#Вход через кнопку в форме восстановления пароля
        driver.find_element(*Locators.MAIN_PAGE_BUTTON).click()
        driver.find_element(*Locators.RESET_PASS_BUTTON).click()
        driver.find_element(*Locators.REG_LOG_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_SITE))
        assert driver.current_url == MAIN_SITE


