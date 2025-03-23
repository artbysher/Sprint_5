import click
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


class TestSectionNavigation:

    def test_navigate_to_buns_section(self, driver): # тест для перехода в раздел «Булки»
        scroll_element = driver.find_element(*Locators.SCROLL_ELEMENT)
        driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
        driver.find_element(*Locators.BUNS_BNT).click()
        buns_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.BUNS_ELEMENT))
        assert buns_element.is_displayed()

    def test_navigate_to_sauces_section(self, driver): # тест для перехода в раздел «Соусы»
        driver.find_element(*Locators.SAUCES_BNT).click()
        sauces_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.SAUCES_ELEMENT))
        assert sauces_element.is_displayed()

    def test_navigate_to_toppings_section(self, driver): # тест для перехода в раздел «Начинки»
        driver.find_element(*Locators.TOPPINGS_BNT).click()
        topping_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.TOPPINGS_ELEMENT))
        assert topping_element.is_displayed()
