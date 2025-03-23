from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


from helper import create_user_credentials
from locators import Locators
from curl import *

class TestRegistration: #тетсты на регистрацию
    def test_success_registration(self,driver): #тест на успешную регистрацию
        name, email, password = create_user_credentials()
        driver.find_element(*Locators.LK_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON).click()

        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver.find_element(*Locators.REG_PASSWORD).send_keys(password)

        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))
        assert driver.current_url == LOGIN_URL

    def test_registration_with_invalid_password(self, driver): #тест на ошибку для некорректного пароля.
        name, email, password = create_user_credentials()
        driver.find_element(*Locators.LK_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON).click()

        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver.find_element(*Locators.REG_PASSWORD).send_keys('1234')

        driver.find_element(*Locators.REGISTER_BUTTON).click()
        reg_error = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REG_ERROR)).text
        assert reg_error == 'Некорректный пароль'