import urls
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage
from pages.login_page import LoginPage
import allure

class TestResetPassword:

    @allure.title('Проверяем переход на страницу восстановления пароля по ссылке «Восстановить пароль»')
    def test_pass_into_forgot_password_page(self, driver):

        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)

        driver.get(urls.LOGIN_PAGE)
        forgot_password_page.wait_disappear_overlay_scroll()
        login_page.click_restore_password()
        forgot_password_page.wait_load_forgot_password_page()

        assert forgot_password_page.get_url_page() == urls.FORGOT_PASSWORD_PAGE

    @allure.title('Проверяем переход на страницу восстановления пароля по кнопке «Восстановить»')
    def test_open_reset_page(self, driver):

        email_for_reset = 'abracadabra@gmail.ru'
        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)

        driver.get(urls.FORGOT_PASSWORD_PAGE)
        forgot_password_page.fill_email_field(email_for_reset)
        forgot_password_page.wait_disappear_overlay_scroll()

        forgot_password_page.click_restore_password_button()
        reset_password_page.wait_load_reset_password_page()

        assert forgot_password_page.get_url_page() == urls.RESET_PASSWORD_PAGE

    @allure.title('Проверка что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_show_password(self, driver):

        email_for_reset = 'abracadabra@gmail.ru'
        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)

        driver.get(urls.FORGOT_PASSWORD_PAGE)
        forgot_password_page.fill_email_field(email_for_reset)
        forgot_password_page.wait_disappear_overlay_scroll()

        forgot_password_page.click_restore_password_button()

        reset_password_page.wait_load_reset_password_page()
        forgot_password_page.wait_disappear_overlay_scroll()

        reset_password_page.click_show_password()

        assert 'input_status_active' in reset_password_page.get_password_input_class_name()