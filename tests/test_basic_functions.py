import urls
from pages.home_page import HomePage
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
import allure

class TestBasicFunctions:

    @allure.title('Проверяем переход на главную страницу по кнопке "Конструктор"')
    def test_pass_into_constructor(self, driver):

        home_page = HomePage(driver)
        login_page = LoginPage(driver)

        driver.get(urls.LOGIN_PAGE)
        home_page.wait_disappear_overlay_scroll()

        login_page.click_constructor_button()
        home_page.wait_load_home_page()

        assert home_page.get_url_page() == urls.BASE_URL

    @allure.title('Проверяем переход в ленту заказов')
    def test_pass_into_feed_orders_list(self, driver):

        home_page = HomePage(driver)
        feed_page = FeedPage(driver)

        driver.get(urls.BASE_URL)
        home_page.wait_load_home_page()

        home_page.click_feed_button()
        feed_page.wait_load_feed_page()

        assert feed_page.get_url_page() == urls.FEED_ORDERS_LIST_PAGE

    @allure.title('Проверяем нажатием на картинку ингридиента открытие всплывающего окна с инфо об ингридиенте')
    def test_open_ingredient_modal_window(self, driver):

        home_page = HomePage(driver)

        driver.get(urls.BASE_URL)
        home_page.wait_load_home_page()

        home_page.click_ingredient()

        assert home_page.get_ingredient_modal_window()

    @allure.title('Проверяем нажатием на кнопку закрытия окна (крестик) закрытие всплывающего окна с инфо об ингридиенте')
    def test_close_ingredient_modal(self, driver):

        home_page = HomePage(driver)

        driver.get(urls.BASE_URL)
        home_page.wait_load_home_page()
        home_page.click_ingredient()

        home_page.get_ingredient_modal_window()
        home_page.close_ingredient_modal_window()

        assert home_page.check_ingredient_modal_window() == False

    @allure.title('Проверяем увеличение счетчика на 2 при добавлении ингредиента булка в заказ')
    def test_increasing_bun_ingredient_counter(self, driver):
        home_page = HomePage(driver)

        driver.get(urls.BASE_URL)
        home_page.wait_load_home_page()

        selected_ingredient = home_page.select_bun_ingredient()
        home_page.add_basket_ingredient(selected_ingredient)

        assert home_page.get_actual_counter(selected_ingredient) == 2

    @allure.title('Проверяем увеличение счетчика на 1 при добавлении ингредиента не булка в заказ')
    def test_increasing_non_bun_ingredient_counter(self, driver):

        home_page = HomePage(driver)

        driver.get(urls.BASE_URL)
        home_page.wait_load_home_page()

        selected_ingredient = home_page.select_non_bun_ingredient()
        home_page.add_basket_ingredient(selected_ingredient)

        assert home_page.get_actual_counter(selected_ingredient) == 1

    @allure.title('Проверяем возможность оформления заказа авторизованным пользователем')
    def test_make_order_user_authorized(self, driver, login_user):

        home_page = HomePage(driver)

        driver.get(urls.LOGIN_PAGE)
        home_page.wait_load_home_page()

        selected_ingredient = home_page.select_bun_ingredient()
        home_page.add_basket_ingredient(selected_ingredient)
        home_page.click_order_button()

        assert home_page.get_order_modal_window()