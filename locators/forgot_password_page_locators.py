from selenium.webdriver.common.by import By

class ForgotPasswordPageLocators:

    # поле ввода email
    EMAIL_INPUT = (By.XPATH, ".//*[text()='Email']/following-sibling::input")
    # кнопка "Восстановить"
    RESTORE_PASSWORD_BUTTON = (By.XPATH, ".//button[text()='Восстановить']")