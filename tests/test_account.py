import allure
import urls
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.home_page import HomePage

class TestAccountPage:

    @allure.title('Проверяем переход по кнопке "Личный кабинет" в аккаунт пользователя')
    def test_pass_into_account(self, driver, client):

        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        account_page = AccountPage(driver)

        driver.get(urls.LOGIN_PAGE)
        home_page.wait_disappear_overlay_scroll()


        login_page.input_user_data(client['email'], client['password'])
        home_page.wait_disappear_overlay_scroll()

        home_page.click_account_cabinet_button()
        user_name = account_page.get_text_name_field()

        assert user_name == client['name']

    @allure.title('Проверяем переход в историю заказов пользователя')
    def test_pass_into_order_history(self, driver, login_user):

        home_page = HomePage(driver)
        account_page = AccountPage(driver)

        driver.get(urls.BASE_URL)

        home_page.wait_disappear_overlay_modal()
        home_page.click_account_cabinet_button()
        account_page.pass_into_order_history()

        home_page.wait_disappear_overlay_modal()

        assert account_page.get_url_page() == urls.ORDER_HISTORY

    @allure.title('Проверяем выход из аккаунта')
    def test_logout(self, driver, login_user):

        home_page = HomePage(driver)
        account_page = AccountPage(driver)
        driver.get(urls.BASE_URL)
        home_page.click_account_cabinet_button()
        account_page.logout_exit_button()
        account_page.wait_load_login_page()

        assert account_page.get_url_page() == urls.LOGIN_PAGE