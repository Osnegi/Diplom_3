import urls
from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.base_page import BasePage
import allure

class ResetPasswordPage(BasePage):

    @allure.step('Ожидаем загрузки страницы обновления пароля')
    def wait_load_reset_password_page(self):
        self.wait_for_url(urls.RESET_PASSWORD_PAGE)

    @allure.step('Нажимаем на кнопку демонстрации пароля')
    def click_show_password(self):
        self.wait_and_find_element(ResetPasswordPageLocators.SHOW_PASSWORD_BUTTON)
        self.click_element(ResetPasswordPageLocators.SHOW_PASSWORD_BUTTON)

    @allure.step('Получаем тип класса поля для ввода пароля для определения активности поля - подсветки поля')
    def get_password_input_class_name(self):
        element_class = self.wait_and_find_element(ResetPasswordPageLocators.NEW_PASSWORD_INPUT).get_attribute('class')
        return element_class