import pytest
from selenium import webdriver
import requests
from helper import RandomUserData
import urls
from pages.login_page import LoginPage
from pages.home_page import HomePage

@pytest.fixture(scope = 'function', params = ['chrome','firefox'])
def driver(request):

    driver = None
    if request.param == 'firefox':
        driver = webdriver.Firefox()

    elif request.param == 'chrome':
        driver = webdriver.Chrome()

    yield driver
    driver.quit()

@pytest.fixture(scope = 'function')
def new_user():
    user_data_generator = RandomUserData()
    user_data = user_data_generator.user_data_generation()
    return user_data

@pytest.fixture(scope = 'function')
def client(new_user):
    response = requests.post(urls.BASE_URL + urls.REGISTRATION_USER_ENDPOINT, data = new_user)
    access_token = response.json()['accessToken']

    yield new_user

    requests.delete(urls.BASE_URL + urls.USER_DATA_ENDPOINT, headers = {'Authorization': access_token})

@pytest.fixture(scope = 'function')
def login_user(driver, client):

    driver.get(urls.LOGIN_PAGE)

    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    home_page.wait_disappear_overlay_scroll()
    home_page.wait_disappear_overlay_modal()
    login_page.input_user_data(client['email'], client['password'])
    home_page.wait_load_home_page()

