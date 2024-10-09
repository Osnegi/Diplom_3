import urls
from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage
import allure

class FeedPage(BasePage):
    @allure.step('Ожидаем загрузки страницы с лентой заказов')
    def wait_load_feed_page(self):
        self.wait_for_url(urls.FEED_ORDERS_LIST_PAGE)

    @allure.step('Нажимаем на верхний заказ в ленте заказов')
    def click_first_order_feed(self):
        self.wait_and_find_element(FeedPageLocators.FIRST_ORDER)
        self.click_element(FeedPageLocators.FIRST_ORDER)

    @allure.step('Получаем всплывающее окно с инфо о заказе')
    def get_order_modal_window(self):
        element = self.wait_and_find_element(FeedPageLocators.MODAL_WINDOW_HEAD)
        return element

    @allure.step('Получаем номер заказа')
    def get_order(self):
        element = self.wait_and_find_element(FeedPageLocators.ORDERS)
        return element.text

    @allure.step('Получаем число заказов за все время')
    def get_count_orders_all_time(self):
        element = self.wait_and_find_element(FeedPageLocators.ORDER_COUNTER_ALL_TIME)
        return int(element.text)

    @allure.step('Получаем число заказов за сегодня')
    def get_count_orders_today(self):
        element = self.wait_and_find_element(FeedPageLocators.ORDER_COUNTER_TODAY)
        return int(element.text)

    @allure.step('Получаем список заказов в работе')
    def get_orders_in_process(self):

        self.wait_and_find_element(FeedPageLocators.NO_ORDERS_IN_PROCESS)
        self.wait_element_disappearing(FeedPageLocators.NO_ORDERS_IN_PROCESS)
        element = self.wait_and_find_element(FeedPageLocators.ORDER_IN_PROCESS)
        return element.text.lstrip('#')