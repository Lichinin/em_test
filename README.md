**Тестовое задание: EM**

Автор: Виталий Личинин

**Оглавление**
- [Цели](#цели)
- [Используемые библиотеки](#используемые-библиотеки)
- [Структура проекта](#структура-проекта)
- [Описание тестов](#описание-тестов)
- [Запуск проекта](#запуск-проекта)
- [Результаты выполнения тестов](#результаты-выполнения-тестов)


***
### Цели.
- Автоматизация UI-тестов веб-ресурса saucedemo.com
- Автоматизация API-тестов для работы с  GitHub API
- Построение отчетности через Allure
- Внедрение логирования для критически важного функционала
***

### Используемые библиотеки.
python 3.10
allure-pytest 2.13.5
pytest 8.3.3
pytest-xdist 3.6.1
python-dotenv 1.0.1
requests 2.32.3
selenium 4.24.0
***
### Структура проекта.
```
em_test                                                                            
├─ allure-report                                                                   
├─ allure-results                                                                  
├─ api_client                                                                      
│  └─ api_client.py                                                                
├─ locators                                                                        
│  └─ locators.py                                                                  
├─ log                                                                             
├─ pages                                                                           
│  ├─ base_page.py                                                                 
│  └─ products_page.py                                                             
├─ test                                                                            
│  ├─ api                                                                          
│  │  └─ test_api.py                                                               
│  └─ ui                                                                           
│     └─ test_products_page.py                                                     
├─ conftest.py                                                                     
├─ LICENSE                                                                         
├─ pytest.ini                                                                      
├─ README.md                                                                       
└─ requirements.txt                                                                
```
* Папка **/allure-report**: Сгенерированный Allure-отчет.

* Папка **/allure-results**: Файлы для генерации Allure-отчета.

* Папка **/api_client**:
  * **api_client.py**: Файл, в котором реализованы методы для выполнения запросов к API

* Папка **/locators**:
  * **locators.py**: Содержит класс с локаторами.

* Папка **/log**: Лог работы.

* Папка **/pages**:
    * **base_page.py**: Базовый класс PageObject , содержащий общие методы и свойства для всех страниц.
    * **products_page.py**: Класс PageObject для взаимодействия со страницей продуктов.

* Папка **/tests**:
    * Папка **/api**:
        * **test_api_appeals.py**: Автотесты API для ресурса Github API.
    * Папка **/test_ui**:
        * **test_appeals.py**: Автотесты UI для веб-ресурса saucedemo.com.

* **conftest.py**: Файл с общими фикстурами для тестов, включая настройку браузера, логгера, тестовых данных и другой общей функциональности.

    Содержит следующие настройки и фикстуры:
    - **pytest_addoption**: Добавляет команды для запуска тестов с различными параметрами, такими как выбор браузера, URL-адрес, уровень логирования, исполнитель (Selenoid) и версия браузера.
    - **logger**: Настраивает логгер RotatingFileHandler для записи информации о ходе выполнения тестов в файл. Создает файл логов с ограничением размера и количества бэкапов. Уровень логирования задается параметром --log_level.
    - **browser**: Настраивает и запускает веб-драйвер для выбранного браузера (Chrome, Firefox или Edge) в зависимости от параметров запуска. Поддерживает запуск тестов локально или в Selenoid.
    - **login_as_user**: Фикстура готовит ProductsPage объект с авторизованной главной страницей проекта.
    - **create_test_repository**: Setup-фикстура, создает тестовый репозиторий.
    - **delete_test_repository**: Teardown-фикстура, удаляет тестовый репозиторий.

* **pytest.ini**: Файл конфигурации для pytest, содержащий настройки для запуска тестов.
* **README.md**: Файл с описанием проекта, инструкциями по установке и запуску тестов.
* **requirements.txt**: Файл, содержащий список зависимостей проекта, необходимых для его работы.

***
### Описание тестов.
* API-тесты:
    * **test_getting_repositories.py**: Тест проверяет получение списка репозиториев для пользователя.
    * **test_create_repository.py**: Тест проверяет создание нового публичного репозитория с указанным именем.
    * **test_delete_repository.py**: Тест проверяет удаление репозитория с указанным именем.
* UI-тесты:
    * **test_login.py**: Тест проверяет, что пользователь может успешно залогиниться на сайте.
    * **test_go_to_product_page.py**: Тест проверяет, что пользователь может перейти на страницу продукта.
    * **test_add_product_to_cart.py**: Тест проверяет, что пользователь может добавить продукт в корзину.
    * **test_shopping_cart_button.py**: Тест проверяет, что пользователь может перейти на страницу корзины.
    * **test_checkout_button.py**: Тест проверяет, что пользователь может перейти на страницу ввода информации о покупателе.
    * **test_fill_user_data.py**: Тест проверяет, что пользователь может ввести данные покупателя и перейти к обзору заказа.
    * **test_complete_purchase.py**: Тест проверяет всё цепочку действий пользователя при покупке - от авторизации до завершения покупки.


### Запуск проекта.
1. Скачать репозиторий.
    ```
    git clone https://github.com/Lichinin/em_test.git
    ```
2. Установите виртуальное окружение:
    ```
    python -m venv venv
    ```
3. Активируйте виртуальное окружение:
    ```
    source venv/script/activate
    ```
4. Установите зависимости:
    ```
    pip install -r requirements.txt
    ```
5. В корне проекта создайте файл ".env", в котором заполните следуюшие данные:
    * LOGIN_URL = URL-ресурса для UI-тестов
    * LOGIN = Логин для авторизации на веб-ресурсе
    * PASSWORD = Пароль для авторизации на веб-ресурсе
    * GIT_USER = Имя пользователя Github
    * GIT_TOKEN = Токен пользователя Github
6. Запустить pytest:
    Для запуска pytest можно использовать следующие флаги:
    * --browser: Выбор браузера для тестов(chrome, firefox, edge)
    * --browser_version: Версия браузера
    * --alluredir=allure-results: Для сохранения папки с отчетностью allure в корень директории проекта
    * -n 2: Количество одновременно запускаемых тестов (в данном примере 2)
    * -vv: Расширенная информация о тестах

    Пример запуска:
    ```
    pytest -n 1 -vv --alluredir=allure-results  --browser='chrome' --browser_version='100'
    ```
### Результат выполнения тестов.
```
$ pytest -n 1 -vv --alluredir=allure-results  --browser='chrome' --browser_version='100'
========================================================================= test session starts =========================================================================
platform win32 -- Python 3.10.6, pytest-8.3.3, pluggy-1.5.0 -- E:\Dev\em_test\venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: E:\Dev\em_test
configfile: pytest.ini
plugins: allure-pytest-2.13.5, xdist-3.6.1
1 worker [10 items]    
scheduling tests via LoadScheduling

test/api/test_api.py::test_getting_repositories
[gw0] [ 10%] PASSED test/api/test_api.py::test_getting_repositories 
test/api/test_api.py::test_create_repository
[gw0] [ 20%] PASSED test/api/test_api.py::test_create_repository 
test/api/test_api.py::test_delete_repository 
[gw0] [ 30%] PASSED test/api/test_api.py::test_delete_repository 
test/ui/test_products_page.py::test_login 
DevTools listening on ws://127.0.0.1:57626/devtools/browser/4f21bcea-b3bc-44f5-a96c-c978e7690249

[gw0] [ 40%] PASSED test/ui/test_products_page.py::test_login
test/ui/test_products_page.py::test_go_to_product_page
DevTools listening on ws://127.0.0.1:57661/devtools/browser/2fe438f6-9a10-4546-b816-8c6b6ac67cb3

[gw0] [ 50%] PASSED test/ui/test_products_page.py::test_go_to_product_page
DevTools listening on ws://127.0.0.1:57626/devtools/browser/4f21bcea-b3bc-44f5-a96c-c978e7690249

[gw0] [ 40%] PASSED test/ui/test_products_page.py::test_login
test/ui/test_products_page.py::test_go_to_product_page
DevTools listening on ws://127.0.0.1:57661/devtools/browser/2fe438f6-9a10-4546-b816-8c6b6ac67cb3

DevTools listening on ws://127.0.0.1:57626/devtools/browser/4f21bcea-b3bc-44f5-a96c-c978e7690249

[gw0] [ 40%] PASSED test/ui/test_products_page.py::test_login
test/ui/test_products_page.py::test_go_to_product_page
DevTools listening on ws://127.0.0.1:57661/devtools/browser/2fe438f6-9a10-4546-b816-8c6b6ac67cb3
DevTools listening on ws://127.0.0.1:57626/devtools/browser/4f21bcea-b3bc-44f5-a96c-c978e7690249

[gw0] [ 40%] PASSED test/ui/test_products_page.py::test_login
test/ui/test_products_page.py::test_go_to_product_page
DevTools listening on ws://127.0.0.1:57626/devtools/browser/4f21bcea-b3bc-44f5-a96c-c978e7690249

[gw0] [ 40%] PASSED test/ui/test_products_page.py::test_login
DevTools listening on ws://127.0.0.1:57626/devtools/browser/4f21bcea-b3bc-44f5-a96c-c978e7690249

[gw0] [ 40%] PASSED test/ui/test_products_page.py::test_login
DevTools listening on ws://127.0.0.1:57626/devtools/browser/4f21bcea-b3bc-44f5-a96c-c978e7690249
DevTools listening on ws://127.0.0.1:57626/devtools/browser/4f21bcea-b3bc-44f5-a96c-c978e7690249

[gw0] [ 40%] PASSED test/ui/test_products_page.py::test_login
test/ui/test_products_page.py::test_go_to_product_page
DevTools listening on ws://127.0.0.1:57661/devtools/browser/2fe438f6-9a10-4546-b816-8c6b6ac67cb3

[gw0] [ 50%] PASSED test/ui/test_products_page.py::test_go_to_product_page
test/ui/test_products_page.py::test_add_product_to_cart
DevTools listening on ws://127.0.0.1:57691/devtools/browser/b1cc7417-1ea3-4f8e-889e-a1bb482733e7

[gw0] [ 60%] PASSED test/ui/test_products_page.py::test_add_product_to_cart
test/ui/test_products_page.py::test_shopping_cart_button
DevTools listening on ws://127.0.0.1:57721/devtools/browser/0009f95d-9c5a-4c4c-8434-656d7c34dae2

[gw0] [ 70%] PASSED test/ui/test_products_page.py::test_shopping_cart_button
test/ui/test_products_page.py::test_checkout_button
DevTools listening on ws://127.0.0.1:57748/devtools/browser/6116a98a-44eb-4b6f-ad91-45106289b996

[gw0] [ 80%] PASSED test/ui/test_products_page.py::test_checkout_button
test/ui/test_products_page.py::test_fill_user_data
DevTools listening on ws://127.0.0.1:57775/devtools/browser/36359634-8c5b-4a86-8aa2-8fce1ff3b2a9

[gw0] [ 90%] PASSED test/ui/test_products_page.py::test_fill_user_data
test/ui/test_products_page.py::test_complete_purchase
DevTools listening on ws://127.0.0.1:57802/devtools/browser/349d4a57-2014-40bd-a2b3-1b4994d88e04

[gw0] [100%] PASSED test/ui/test_products_page.py::test_complete_purchase

==================================================================== 10 passed in 76.43s (0:01:16) ==================================================================== 
```
