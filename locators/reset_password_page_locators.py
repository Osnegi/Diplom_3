from selenium.webdriver.common.by import By

class ResetPasswordPageLocators:

    # поле для ввода нового пароля
    NEW_PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/parent::div")
    # глазик для видимости вводимого пароля
    SHOW_PASSWORD_BUTTON = (By.XPATH, ".//div[contains(@class, 'input__icon')]")