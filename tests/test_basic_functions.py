import urls
from pages.home_page import HomePage
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
import allure
from locators.home_page_locators import HomePageLocators

class TestBasicFunctions:

    @allure.title('Проверяем переход на главную страницу по кнопке "Конструктор"')
    def test_pass_into_constructor(self, driver):

        home_page = HomePage(driver)
        login_page = LoginPage(driver)

        driver.get(urls.LOGIN_PAGE)
        home_page.wait_element_disappearing(HomePageLocators.OVERLAY_SCROLL)
        login_page.click_constructor_button()
        home_page.wait_load_home_page()

        assert home_page.get_url_page() == urls.BASE_URL

    @allure.title('Проверяем переход в ленту заказов')
    def test_pass_into_feed_orders_list(self, driver):

        home_page = HomePage(driver)
        feed_page = FeedPage(driver)

        driver.get(urls.BASE_URL)
        home_page.wait_load_home_page()
        home_page.wait_element_disappearing(HomePageLocators.OVERLAY_SCROLL)
        home_page.click_feed_button()
        feed_page.wait_load_feed_page()

        assert feed_page.get_url_page() == urls.FEED_ORDERS_LIST_PAGE

    @allure.title('Проверяем нажатием на картинку ингридиента открытие всплывающего окна с инфо об ингридиенте')
    def test_open_ingredient_modal_window(self, driver):

        home_page = HomePage(driver)

        driver.get(urls.BASE_URL)
        home_page.wait_load_home_page()
        home_page.wait_element_disappearing(HomePageLocators.OVERLAY_SCROLL)
        home_page.click_ingredient()

        assert home_page.get_ingredient_modal_window()

    @allure.title('Проверяем нажатием на кнопку закрытия окна (крестик) закрытие всплывающего окна с инфо об ингридиенте')
    def test_close_ingredient_modal(self, driver):

        home_page = HomePage(driver)

        driver.get(urls.BASE_URL)
        home_page.wait_load_home_page()
        home_page.wait_element_disappearing(HomePageLocators.OVERLAY_SCROLL)
        home_page.click_ingredient()

        home_page.get_ingredient_modal_window()
        home_page.close_ingredient_modal_window()

        assert home_page.check_ingredient_modal_window() == False

    @allure.title('Проверяем увеличение счетчика ингридиента при добавлении этого ингредиента в заказ')
    def test_increasing_ingredient_counter(self, driver):

        home_page = HomePage(driver)

        driver.get(urls.BASE_URL)
        home_page.wait_load_home_page()
        selected_ingredient = home_page.select_ingredient()
        home_page.add_basket_ingredient(selected_ingredient)
        if 'булка' in selected_ingredient.text:
            expected_counter = 2
        else:
            expected_counter = 1
        assert home_page.get_actual_counter(selected_ingredient) == expected_counter

    @allure.title('Проверяем возможность оформления заказа авторизованным пользователем')
    def test_make_order_user_authorized(self, driver, login_user):

        home_page = HomePage(driver)

        driver.get(urls.LOGIN_PAGE)
        home_page.wait_load_home_page()

        selected_ingredient = home_page.select_ingredient()
        home_page.add_basket_ingredient(selected_ingredient)
        home_page.wait_element_disappearing(HomePageLocators.OVERLAY_SCROLL)
        home_page.click_order_button()

        assert home_page.get_order_modal_window()