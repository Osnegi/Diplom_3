from selenium.webdriver.common.by import By

class FeedPageLocators:

    # номер первого заказа в ленте заказов
    ORDERS = (By.XPATH, ".//ul[@class = 'OrderFeed_list__OLh59']/li[1]/a/div/p[@class = 'text text_type_digits-default']")

    # ссылка на детали первого заказ в ленте заказов
    FIRST_ORDER = (By.XPATH, "(.//a[contains(@class, 'OrderHistory_link__1iNby')])[1]")

    # всплывающее окно деталей заказа в ленте заказов
    MODAL_WINDOW_HEAD = (By.XPATH, ".//div[contains(@class, 'Modal_orderBox')]/parent::div/parent::section")

    # заказы в списке заказов "Готовы:"
    ORDERS_READY = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderList")]/li')
    # номер заказа в списке заказов "В работе:"
    ORDER_IN_PROCESS = (By.XPATH, ".//ul[contains(@class,'OrderFeed_orderListReady')]/li")
    # текст "Все текущие заказы готовы!" под заголовком "В работе:"
    NO_ORDERS_IN_PROCESS = (By.XPATH, ".//li[text()='Все текущие заказы готовы!']")

    # счетчик заказов "Выполнено за все время:"
    ORDER_COUNTER_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    # счетчик заказов "Выполнено за сегодня:"
    ORDER_COUNTER_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")