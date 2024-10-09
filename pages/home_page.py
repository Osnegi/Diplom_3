import urls
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage
from random import choice
import allure

class HomePage(BasePage):

    @allure.step('Переходим в аккаунт пользователя по кнопке "Личный кабинет" ')
    def click_account_cabinet_button(self):
        self.wait_and_find_element(HomePageLocators.ENTER_CABINET_BUTTON)
        self.click_element(HomePageLocators.ENTER_CABINET_BUTTON)

    @allure.step('Переходим в аккаунт пользователя по кнопке "Войти в аккаунт"')
    def click_login_button(self):
        self.wait_and_find_element(HomePageLocators.ENTER_ACCOUNT_BUTTON)
        self.click_element(HomePageLocators.ENTER_ACCOUNT_BUTTON)

    @allure.step('Ожидаем загрузки главной страницы')
    def wait_load_home_page(self):
        self.wait_for_url(urls.BASE_URL)
        self.wait_and_find_element(HomePageLocators.INGREDIENTS_LIST)

    @allure.step('Переходим по кнопке "Лента заказов" в ленту заказов')
    def click_feed_button(self):
        self.wait_and_find_element(HomePageLocators.FEED_BUTTON)
        self.click_element(HomePageLocators.FEED_BUTTON)

    @allure.step('Нажимаем на картинку ингридиента')
    def click_ingredient(self):
        self.wait_and_find_element(HomePageLocators.FIRST_INGREDIENT)
        self.click_element(HomePageLocators.FIRST_INGREDIENT)

    @allure.step('Получаем всплывающее окно с инфо об ингридиенте')
    def get_ingredient_modal_window(self):
        element = self.wait_and_find_element(HomePageLocators.MODAL_INGREDIENT_HEAD)
        return element

    @allure.step('Проверяем отображение всплывающего окна с инфо об ингридиенте')
    def check_ingredient_modal_window(self):
        return self.check_element_visibility(HomePageLocators.MODAL_INGREDIENT_HEAD)

    @allure.step('Закрываем всплывающее окно с инфо об ингридиенте')
    def close_ingredient_modal_window(self):
        self.wait_and_find_element(HomePageLocators.CLOSE_MODAL_INGREDIENT_BUTTON)
        self.click_element(HomePageLocators.CLOSE_MODAL_INGREDIENT_BUTTON)

    @allure.step('Выбираем ингридиент из списка')
    def select_ingredient(self):
        ingredients = self.driver.find_elements(*HomePageLocators.INGREDIENTS_LIST)
        selected_ingredient = choice(ingredients)
        return selected_ingredient

    @allure.step('Добавляем ингридиент в корзину')
    def add_basket_ingredient(self, ingredient):
        basket = self.wait_and_find_element(HomePageLocators.BASKET)
        self.drag_and_drop(ingredient, basket)

    @allure.step('Получаем счетчик выбранного ингридиента')
    def get_actual_counter(self, ingredient):
        return int(ingredient.text[0])

    @allure.step('Нажимаем на кнопку "Оформить заказ"')
    def click_order_button(self):
        self.wait_and_find_element(HomePageLocators.MAKE_ORDER_BUTTON)
        self.click_element(HomePageLocators.MAKE_ORDER_BUTTON)

    @allure.step('Получаем всплывающее окно вновь созданного заказа')
    def get_order_modal_window(self):
        element = self.wait_and_find_element(HomePageLocators.MODAL_NEW_ORDER_TEXT)
        return element

    @allure.step('Ожидаем обновления номера нового аказа')
    def wait_order_created(self):
        order_number = "9999"
        while order_number == "9999":
            order_number = self.wait_and_find_element(HomePageLocators.MODAL_NEW_ORDER_NUMBER).text
        return order_number

    @allure.step('Получаем номер нового заказа')
    def get_order_number(self):
        element = self.wait_and_find_element(HomePageLocators.MODAL_NEW_ORDER_NUMBER)
        return element.text
    @allure.step('Закрываем окно вновь созданного заказа')
    def close_order_modal_window(self):
        self.wait_and_find_element(HomePageLocators.CLOSE_MODAL_NEW_ORDER_BUTTON)
        self.click_element(HomePageLocators.CLOSE_MODAL_NEW_ORDER_BUTTON)

