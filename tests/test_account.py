import allure
import urls
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.home_page import HomePage
from locators.home_page_locators import HomePageLocators

class TestAccountPage:

    @allure.title('Проверяем переход по кнопке "Личный кабинет" в аккаунт пользователя')
    def test_pass_into_account(self, driver, client):

        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        account_page = AccountPage(driver)

        driver.get(urls.LOGIN_PAGE)
        login_page.wait_element_disappearing(HomePageLocators.OVERLAY_SCROLL)
        login_page.input_user_data(client['email'], client['password'])
        home_page.wait_element_disappearing(HomePageLocators.OVERLAY_SCROLL)
        home_page.click_account_cabinet_button()
        account_page.wait_element_disappearing(HomePageLocators.OVERLAY_SCROLL)
        user_name = account_page.get_text_name_field()

        assert user_name == client['name']

    @allure.title('Проверяем переход в историю заказов пользователя')
    def test_pass_into_order_history(self, driver, login_user):

        home_page = HomePage(driver)
        account_page = AccountPage(driver)

        driver.get(urls.BASE_URL)
        home_page.wait_element_disappearing(HomePageLocators.OVERLAY_SCROLL)
        home_page.click_account_cabinet_button()
        home_page.wait_element_disappearing(HomePageLocators.OVERLAY_SCROLL)
        account_page.wait_element_disappearing(HomePageLocators.OVERLAY_SCROLL)
        account_page.pass_into_order_history()
        account_page.wait_element_disappearing(HomePageLocators.OVERLAY_SCROLL)

        assert account_page.get_url_page() == urls.ORDER_HISTORY

    @allure.title('Проверяем выход из аккаунта')
    def test_logout(self, driver, login_user):

        home_page = HomePage(driver)
        account_page = AccountPage(driver)

        driver.get(urls.BASE_URL)
        home_page.wait_element_disappearing(HomePageLocators.OVERLAY_SCROLL)
        home_page.click_account_cabinet_button()
        account_page.wait_element_disappearing(HomePageLocators.OVERLAY_SCROLL)
        account_page.wait_element_disappearing(HomePageLocators.OVERLAY_SCROLL)
        account_page.logout_exit_button()
        account_page.wait_element_disappearing(HomePageLocators.OVERLAY_SCROLL)
        account_page.wait_load_login_page()

        assert account_page.get_url_page() == urls.LOGIN_PAGE