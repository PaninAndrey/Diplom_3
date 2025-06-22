import allure

from pages.constructor_page import ConstructorPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from curl import Url


class TestConstructorPage:

    @allure.title('Проверяем переход по клику на раздел «Конструктор»')
    def test_open_constructor_by_click(self, driver):
        with allure.step('Дожидаемся загрузки сайта и кликаем по надписи "Лента заказов" в заголовке страницы'):
            main_page = MainPage(driver)
            main_page.main_page_loading_wait()
            main_page.click_order_feed_title()
        with allure.step('Кликаем по надписи "Конструктор" в заголовке страницы"'):
            main_page.click_constructor_title()
        with allure.step('Ждем перехода на вкладку "Конструктор" и отображения кнопки "Войти в аккаунт"'):
            main_page.wait_for_login_button()
        with allure.step('Проверяем, что текущий Url совпадает с Url главной страницы'):
            assert main_page.get_current_url() == Url.BASE_URL+'/', f'Текущий Url не совпадает с Url главной страницы'


    @allure.title('Проверяем переход по клику на раздел «Лента заказов»')
    def test_open_order_feed_by_click(self, driver):
        with allure.step('Дожидаемся загрузки сайта и кликаем по надписи "Лента заказов" в заголовке страницы'):
            main_page = MainPage(driver)
            main_page.main_page_loading_wait()
            main_page.click_order_feed_title()
        with allure.step('Ждем перехода на вкладку "Лента заказов" и отображения надписи "Выполнено за все время"'):
            order_feed_page = OrderFeedPage(driver)
            order_feed_page.wait_for_total_all_time_title()
        with allure.step('Проверяем, что текущий Url совпадает с Url главной страницы'):
            assert order_feed_page.get_current_url() == Url.ORDER_FEED_PAGE, f'Текущий Url не совпадает с Url страницы ленты заказов'


    @allure.title('Проверяем, что если кликнуть на ингредиент, то появится всплывающее окно с деталями')
    def test_open_ingredient_window(self, driver):
        with allure.step('Дожидаемся загрузки сайта'):
            main_page = MainPage(driver)
            main_page.main_page_loading_wait()
        with allure.step('Кликаем на ингредиент "Флюоресцентная булка"'):
            constructor_page = ConstructorPage(driver)
            constructor_page.click_bun_fluo()
            assert constructor_page.wait_for_ingredient_window(), f'Окно с деталями ингредиента не открывается'


    @allure.title('Проверяем, что всплывающее окно с деталями ингредиентов закрывается кликом по крестику')
    def test_ingredient_window_close_by_cross(self, driver):
        with allure.step('Дожидаемся загрузки сайта'):
            main_page = MainPage(driver)
            main_page.main_page_loading_wait()
        with allure.step('Кликаем на ингредиент "Флюоресцентная булка"'):
            constructor_page = ConstructorPage(driver)
            constructor_page.click_bun_fluo()
        with allure.step('Дожидаемся открытия модального окна с деталями ингредиента'):
            constructor_page.wait_for_ingredient_window()
        with allure.step('Кликаем на крестик'):
            constructor_page.click_ingredient_window_cross()
        with allure.step('Дожидаемся закрытия модального окна с деталями ингредиента'):
            constructor_page.ingredient_window_is_closed()
        with allure.step('Проверяем, что модальное окно с деталями ингредиента закрылось'):
            assert main_page.wait_for_login_button, f'Модальное окно с ингредентами не закрылось'


    @allure.title('Проверяем, что при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается.')
    def test_ingredient_counter_is_rising(self, driver):
        with allure.step('Дожидаемся загрузки сайта'):
            main_page = MainPage(driver)
            main_page.main_page_loading_wait()
        with allure.step('Получаем значение счётчика до добавления ингредиента'):
            constructor_page = ConstructorPage(driver)
            counter_before = constructor_page.get_counter()
        with allure.step('Перетаскиваем флюоресцентную булку из меню в конструктор бургера'):
            constructor_page.drag_and_drop_bun()
        with allure.step('Получаем значение счётчика после добавления ингредиента'):
            counter_after = constructor_page.get_counter()
        with allure.step('Проверяем, что счетчик ингредиента увеличился'):
            assert counter_after > counter_before, f'Счетчик ингредиента после его перетаскивания в бургер не увеличился'