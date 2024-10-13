from selenium.webdriver.common.by import By

class HomePageLocators:

    # кнопка перехода в "Ленту заказов"
    FEED_BUTTON = (By.XPATH, ".//p[text()='Лента Заказов']")

    # лист ингридиентов
    BUN_INGREDIENTS_LIST = (By.XPATH, ".//p[contains(text(), 'булка')]//parent::a[contains(@href, '/ingredient/')]")
    NON_BUN_INGREDIENTS_LIST = (By.XPATH, ".//p[not(contains(text(), 'булка'))]//parent::a[contains(@href, '/ingredient/')]")
    # первый ингридиент в картинках ингридиентов для бургера
    FIRST_INGREDIENT = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient_')][1]")
    # заголовок всплывающего окна с инфо об ингридиенте
    MODAL_INGREDIENT_HEAD = (By.XPATH, ".// h2[text() = 'Детали ингредиента']")
    # кнопка-крестик "Закрыть" окно с инфо об ингридиенте
    CLOSE_MODAL_INGREDIENT_BUTTON = (By.XPATH, './/button[contains(@class,"Modal_modal__close_modified")]')
    # ингридиент, который можно посчитать - соус Острый
    INGREDIENT_SAUCE = (By.XPATH, "//img[@alt='Соус Spicy-X']")
    # счетчик для соуса Острый
    COUNTER_INGREDINET_SAUCE = (By.XPATH, "//p[normalize-space()='1']")
    # половинки булки в корзине
    BASKET = (By.CLASS_NAME, 'constructor-element_pos_top')

    # вход в аккаунт через кнопку «Войти в аккаунт» на главной странице
    ENTER_ACCOUNT_BUTTON = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")
    # вход в аккаунт через кнопку «Личный кабинет» на главной странице
    ENTER_CABINET_BUTTON = (By.XPATH, ".//p[text() = 'Личный Кабинет']")

    # кнопка "Оформить заказ"
    MAKE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
    # надпись "идентификатор заказа" во вспылвающем окне с инфо о вновь созданном заказе
    MODAL_NEW_ORDER_TEXT = (By.XPATH, ".//p[text()='идентификатор заказа']")
    # номер заказа во вспылвающем окне с инфо о вновь созданном заказе
    MODAL_NEW_ORDER_NUMBER = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow')]")
    # кнопка закрытия всплываюшего окна о внось созданном заказе
    CLOSE_MODAL_NEW_ORDER_BUTTON = (By.XPATH, ".//button[contains(@class,'Modal_modal__close_modified')]")

    OVERLAY_SCROLL = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")
    OVERLAY_MODAL = (By.XPATH, './/img[contains(@class, "Modal_modal__loading")]')