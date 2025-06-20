import pytest

from selenium import webdriver
from helper_methods import HelperMethods as Help
from curl import Url
from generators import UserData as UD
from data import RequestAndResponseKeys as Key
from pages.login_page import LoginPage
from pages.main_page import MainPage


### Фикстура для открытия окна веб-браузера ###
@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(Url.BASE_URL)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
        driver.get(Url.BASE_URL)
    yield driver
    driver.quit()

### Создаем пользователя и сохраняем его данные для удаления после завершения тестов ###
@pytest.fixture
def generate_user():
    # Генерируем email, пароль и имя нового пользователя
    user_data = UD.generate_new_user_data()
    # Отправляем запрос на создание уникального пользователя
    response = Help.register_new_user(user_data)
    # Получаем тело ответа в формате словаря
    response_dict = response.json()
    # Получаем авторизационный токен
    access_token = response_dict[Key.ACCESS_TOKEN]
    # Возвращаем данные пользователя
    yield user_data
    # Удаляем созданного пользователя после завершения теста
    Help.delete_user(access_token)

### Авторизуемся под созданным новым пользователем на сайте ###
@pytest.fixture
def login_user(driver, generate_user):
    # Получаем данные зарегестрированного пользователя
    email = generate_user[Key.EMAIL]
    password = generate_user[Key.PASSWORD]
    # Открываем главную страницу веб-приложения
    main_page = MainPage(driver)
    main_page.main_page_loading_wait()
    # Переходим на страницу авторизации пользователя
    main_page.go_to_login_page()
    # Вводим email и пароль созданного пользователя
    login_page = LoginPage(driver)
    login_page.enter_user_data(email, password)
    # Нажимаем на кнопку войти
    login_page.click_enter_button()
    # Дожидаемся отображения кнопки "Оформить заказ" на главной странице
    main_page.wait_for_order_button_visibility()
    return driver



