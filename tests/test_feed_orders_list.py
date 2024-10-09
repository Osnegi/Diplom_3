import urls
from pages.feed_page import FeedPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from locators.home_page_locators import HomePageLocators
import allure

class TestOrderFeed:

    @allure.title('Проверяем открытие окна с инфо о заказе в ленте заказов')
    def test_open_order_modal_window(self, driver):

        feed_page = FeedPage(driver)

        driver.get(urls.FEED_ORDERS_LIST_PAGE)
        feed_page.wait_load_feed_page()
        feed_page.click_first_order_feed()

        assert feed_page.get_order_modal_window()

    @allure.title('Увеличение счетчика заказов за день')
    def test_increasing_counter_orders_today(self, driver, login_user):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        feed_page = FeedPage(driver)

        driver.get(urls.BASE_URL)
        home_page.wait_load_home_page()
        home_page.wait_element_disappearing(HomePageLocators.OVERLAY_SCROLL)
        home_page.click_feed_button()
        feed_page.wait_load_feed_page()
        count_before = feed_page.get_count_orders_today()

        login_page.click_constructor_button()
        home_page.wait_load_home_page()
        ingredient = home_page.select_ingredient()
        home_page.add_basket_ingredient(ingredient)
        home_page.click_order_button()
        home_page.wait_order_created()
        home_page.close_order_modal_window()

        home_page.click_feed_button()
        feed_page.wait_load_feed_page()
        count_after = feed_page.get_count_orders_today()

        assert count_after == count_before + 1

    @allure.title('Отображение созданного заказа "В работе"')
    def test_new_order_in_process_orders_list(self, driver, login_user):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        feed_page = FeedPage(driver)

        driver.get(urls.BASE_URL)
        home_page.wait_load_home_page()

        login_page.click_constructor_button()
        home_page.wait_load_home_page()
        ingredient = home_page.select_ingredient()
        home_page.add_basket_ingredient(ingredient)
        home_page.click_order_button()
        home_page.wait_order_created()
        new_order = home_page.get_order_number()
        home_page.close_order_modal_window()

        home_page.click_feed_button()
        feed_page.wait_load_feed_page()
        order_in_work = feed_page.get_orders_in_process()

        assert new_order in order_in_work

    @allure.title('Проверяем отображение в ленте заказов заказа пользователя из истории его заказов')
    def test_user_order_in_feed(self, driver, login_user):
            home_page = HomePage(driver)
            feed_page = FeedPage(driver)
            account_page = AccountPage(driver)

            driver.get(urls.BASE_URL)
            home_page.wait_load_home_page()
            selected_ingredient = home_page.select_ingredient()
            home_page.add_basket_ingredient(selected_ingredient)
            home_page.wait_element_disappearing(HomePageLocators.OVERLAY_SCROLL)
            home_page.click_order_button()

            home_page.wait_order_created()
            home_page.close_order_modal_window()
            home_page.click_account_cabinet_button()

            account_page.pass_into_order_history()
            user_order_history = account_page.get_user_order()

            home_page.click_feed_button()
            feed_page.wait_load_feed_page()
            user_order_feed = feed_page.get_order()

            assert user_order_history == user_order_feed

    @allure.title('Увеличение счетчика заказов за все время')
    def test_increasing_counter_orders_all_time(self, driver, login_user):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        feed_page = FeedPage(driver)

        driver.get(urls.BASE_URL)
        home_page.wait_load_home_page()
        home_page.wait_element_disappearing(HomePageLocators.OVERLAY_SCROLL)
        home_page.click_feed_button()
        feed_page.wait_load_feed_page()
        count_before = feed_page.get_count_orders_all_time()

        login_page.click_constructor_button()
        home_page.wait_load_home_page()
        ingredient = home_page.select_ingredient()
        home_page.add_basket_ingredient(ingredient)
        home_page.click_order_button()
        home_page.wait_order_created()
        home_page.close_order_modal_window()

        home_page.click_feed_button()
        feed_page.wait_load_feed_page()
        count_after = feed_page.get_count_orders_all_time()

        assert count_after == count_before + 1
