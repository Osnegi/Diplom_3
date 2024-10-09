import urls
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage
import allure

class ForgotPasswordPage(BasePage):

    @allure.step('Ожидаем загрузки страницы "Восстановление пароля"')
    def wait_load_forgot_password_page(self):
        self.wait_for_url(urls.FORGOT_PASSWORD_PAGE)

    @allure.step('Заполняем поле "emai"')
    def fill_email_field(self, email):
        self.wait_and_find_element(ForgotPasswordPageLocators.EMAIL_INPUT)
        self.send_data_into_field(ForgotPasswordPageLocators.EMAIL_INPUT, email)

    @allure.step('Нажимаем кнопку "Восстановить"')
    def click_restore_password_button(self):
        self.wait_and_find_element(ForgotPasswordPageLocators.RESTORE_PASSWORD_BUTTON)
        self.click_element(ForgotPasswordPageLocators.RESTORE_PASSWORD_BUTTON)