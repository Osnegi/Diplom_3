from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from locators.home_page_locators import HomePageLocators
import allure

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Кликаем по элементу')
    def click_element(self, locator):
        WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Заполняем поле данными')
    def send_data_into_field(self, locator, text):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Получаем элемент страницы')
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))

        return self.driver.find_element(*locator)

    @allure.step('Проверяем отображение элемента на странице')
    def check_element_visibility(self, locator):
        try:
            self.driver.find_element(locator)
            return True
        finally:
            return False

    @allure.step('Ожидание удаления элемента со страницы')
    def wait_element_disappearing (self, locator):
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located(locator))

    @allure.step('Получаем URL страницы')
    def get_url_page(self):
        current_url = self.driver.current_url
        return current_url

    @allure.step('Ожидание смены URL страницы')
    def wait_for_url(self, url):
        WebDriverWait(self.driver, 20).until(EC.url_to_be(url))

    @allure.step('Переносим drag&drop элемент с одного места на другое')
    def drag_and_drop(self, source, target):

        action_chains = ActionChains(self.driver)
        drag = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(source))
        drop = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(target))
        action_chains.drag_and_drop(drag, drop).perform()

    @allure.step('Ждем исчезновения оверлэй объекта - скролл')
    def wait_disappear_overlay_scroll(self):
        self.wait_element_disappearing(HomePageLocators.OVERLAY_SCROLL)

    @allure.step('Ждем исчезновения оверлэй объекта - модальное окно')
    def wait_disappear_overlay_modal(self):
        self.wait_element_disappearing(HomePageLocators.OVERLAY_MODAL)