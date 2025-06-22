## Дипломный проект. Задание 3: Автотесты для UI

## Студент: Андрей Панин

## <h>Когорта: #21</h>
<hr>

## <h>Инструкция по запуску:</h>

### <h>1. Установите зависимости:</h>

> pip install -r requirements.txt</h>

### <h>2. Запустить все тесты и записать отчет:</h>

> pytest --alluredir=./allure-results

### <h>3. Посмотреть отчет по прогону html</h>

> allure serve ./allure-results


<hr>

<h3 align="left" style="color:yellow">Project files and description:</h3>

| Название файла               | Содержание файла                               |
|------------------------------|------------------------------------------------|
| allure-results.dir           | Папка с отчетами Allure                        |                                                               |
| locators                     | Директория с локаторами                        |
| constructor_page_locators.py | Локаторы для "Конструктора"                    |
| login_page_locators.py       | Локаторы для страницы авторизации              |
| main_page_locators.py        | Локаторы главной страницы                      |
| orfer_feed_page_locators.py  | Локаторы страницы "Лента заказов"              |
| pages.dir                    | Папка с методами пейджей                       |
| base_page.py                 | Главные методы работы с элементами на странице |
| constructor_page.py          | Методы для проверки раздела "Конструктор"      
| login_page.py                | Методы для раздела авторизации                 |
| main_page.py                 | Методы для главной страницы                    |
| order_feed_page.py           | Методы для работы раздела "Лента заказов"      |
| tests                        | Папка с тестами                                |        
| conftest.py                  | Фикстуры                                       |
| test_basic_functionality.py  | Тесты базовой функциональности                 |
| .gitignore                   | Файл .gitignore                                |
| curl.py                      | URL-ы                                          |
| data.py                      | Файл со вспомогательными данными               |
| generators.py                | Файл для генерации тестовых данных             |
| helper_methods.py            | Файл со вспомогательными методами              |
| README.md                    | README-файл                                    |
| requirements.txt             | Файл с зависимостями                           |