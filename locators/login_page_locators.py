from selenium.webdriver.common.by import By

class LoginPageLocators:

    # поля ввода email в форме входа в аккаунт
    INPUT_EMAIL = (By.XPATH, ".//input[@name = 'name']")
    # поле ввода password в форме входа в аккаунт
    INPUT_PASSWORD = (By.XPATH, ".//input[@name = 'Пароль']")
    # вход в аккаунт (кнопка Войти)
    ENTER_BUTTON = (By.XPATH, ".//button[text() = 'Войти']")

    #ссылка 'Восстановить пароль' на форму восстановления пароля.
    RESTORE_PASSWORD_LINK = (By.XPATH, ".//a[text() = 'Восстановить пароль']")

    # переход через кнопку «Конструктор»
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text() = 'Конструктор']")