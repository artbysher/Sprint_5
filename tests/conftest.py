import pytest

from selenium import webdriver


from curl import *
from data import Credentials
from locators import Locators


@pytest.fixture(scope="function")
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(MAIN_SITE)
    yield browser
    browser.quit()

@pytest.fixture
def authorize(driver):
    #Фикстура для авторизации пользователя.
    driver.find_element(*Locators.MAIN_PAGE_BUTTON).click()
    driver.find_element(*Locators.EMAIL).send_keys(Credentials.EMAIL)
    driver.find_element(*Locators.PASSWORD).send_keys(Credentials.PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    return driver
