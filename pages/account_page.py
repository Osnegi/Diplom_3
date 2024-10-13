import urls
from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage
import allure

class AccountPage(BasePage):

    @allure.step('Получаем имя клиента из аккаунта (текст в поле "Имя")')
    def get_text_name_field(self):
        client_name = self.wait_and_find_element(AccountPageLocators.CLIENT_NAME).get_property('value')
        return client_name

    @allure.step('Переходим по ссылке "История заказов"')
    def pass_into_order_history(self):
        self.wait_and_find_element(AccountPageLocators.ORDER_HISTORY_LINK).click()

    @allure.step('Получаем номер заказа клиента из истории его заказов')
    def get_user_order(self):
        element = self.wait_and_find_element(AccountPageLocators.ORDER_NUMBER)
        return element.text

    @allure.step('Выходим из аккаунта по ссылке "Выход"')
    def logout_exit_button(self):
        self.wait_and_find_element(AccountPageLocators.EXIT_BUTTON)
        self.click_element(AccountPageLocators.EXIT_BUTTON)

    @allure.step('Ожидание страницы авторизации')
    def wait_load_login_page(self):
        self.wait_for_url(urls.LOGIN_PAGE)