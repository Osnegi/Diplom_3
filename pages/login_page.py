from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
import allure

class LoginPage(BasePage):

    @allure.step('Заполняем поле "email"')
    def fill_email_field(self, email):
        self.send_data_into_field(LoginPageLocators.INPUT_EMAIL, email)

    @allure.step('Заполняем поле "Пароль"')
    def fill_password_field(self, password):
        self.send_data_into_field(LoginPageLocators.INPUT_PASSWORD, password)

    @allure.step('Авторизуем пользователя')
    def input_user_data(self, email, password):
        self.fill_email_field(email)
        self.fill_password_field(password)
        self.click_element(LoginPageLocators.ENTER_BUTTON)

    @allure.step('Нажимаем кнопку "Восстановить пароль"')
    def click_restore_password(self):
        self.wait_and_find_element(LoginPageLocators.RESTORE_PASSWORD_LINK)
        self.click_element(LoginPageLocators.RESTORE_PASSWORD_LINK)

    @allure.step('Нажимаем кнопку "Конструктор"')
    def click_constructor_button(self):
        self.wait_and_find_element(LoginPageLocators.CONSTRUCTOR_BUTTON)
        self.click_element(LoginPageLocators.CONSTRUCTOR_BUTTON)