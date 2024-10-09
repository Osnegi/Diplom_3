from selenium.webdriver.common.by import By

class AccountPageLocators:

    # имя клиента в личном кабинете
    CLIENT_NAME = (By.XPATH, ".//label[text()='Имя']/parent::div/input")

    # переход в историю заказов клиента
    ORDER_HISTORY_LINK = (By.XPATH, "//*[@href='/account/order-history']")
    # номер заказа клиента из его истории заказов
    ORDER_NUMBER = (By.XPATH, ".//p[@class = 'text text_type_digits-default']")
    # ссылка История заказов белым цветом - активная
    ORDER_HISTORY_ACTIVE = (By.XPATH, ".//a[contains(@class, 'Account_link_active')]")

    # кнопка Выход в личном кабинете
    EXIT_BUTTON = (By.XPATH, ".//button[text() = 'Выход']")
