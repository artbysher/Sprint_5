from selenium.webdriver.common.by import By


class Locators: # Локаторы для регистрации
    LK_BUTTON = [By.XPATH, "//p[text()='Личный Кабинет']"]
    REG_BUTTON = [By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Зарегистрироваться']"]
    NAME = [By.XPATH, "(//input[@name='name'])[1]"]
    REG_EMAIL = [By.XPATH, "(//input[@name='name'])[2]"]
    REG_PASSWORD = [By.XPATH, "//input[@name='Пароль']"]
    REGISTER_BUTTON = [By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"]
    REG_ERROR = (By.XPATH, "//p[@class='input__error text_type_main-default' and text()='Некорректный пароль']")

    #Локаторы для входа
    EMAIL = [By.XPATH, "//input[@name='name']"]
    PASSWORD = [By.XPATH, "//input[@name='Пароль']"]
    LOGIN_BUTTON = [By.XPATH, "//button[text()='Войти']"]
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[name='email']")
    MAIN_PAGE_BUTTON = [By.XPATH, "//button[text()='Войти в аккаунт']"] #кнопка на стартовом экране "Войти в акккаунт"
    ORDER_BUTTON = [By.XPATH, "//button[text()='Оформить заказ']"]
    REG_LOG_BUTTON = [By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Войти']"]
    RESET_PASS_BUTTON = [By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Восстановить пароль']"]

    #Локаторы для проверок в личном кабинете

    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    CONSTRUCTOR_BUTTON = [By.XPATH, "//p[text()='Конструктор']"]
    LOGO_BUTTON = [By.CLASS_NAME, "AppHeader_header__logo__2D0X2"]

    #Локаторы для перехода по разделам
    SCROLL_ELEMENT = (By.XPATH, "//p[@class='BurgerIngredient_ingredient__text__yp3dH' and text()='Сыр с астероидной плесенью']")
    BUNS_BNT = (By.XPATH, "//span[text()='Булки']")
    BUNS_ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[text()='Булки']")
    SAUCES_BNT = (By.XPATH, "//span[text()='Соусы']")
    SAUCES_ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[text()='Соусы']")
    TOPPINGS_BNT = (By.XPATH, "//span[text()='Начинки']")
    TOPPINGS_ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[text()='Начинки']")