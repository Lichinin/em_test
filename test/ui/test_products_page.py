import allure

from pages.base_page import BasePage
from pages.products_page import ProductsPage


@allure.epic('EM test project')
@allure.suite('UI tests')
@allure.title('Авторизация пользователя')
def test_login(browser):
    page = BasePage(browser)
    page.fill_login_field()
    page.fill_password_field()
    page.click_login_button()
    page.assert_proceed_to_products_page()


@allure.epic('EM test project')
@allure.suite('UI tests')
@allure.title('Переход на страницу товара')
def test_go_to_product_page(login_as_user):
    page = login_as_user
    page.click_on_product_name()
    page.assert_proceed_to_product_page()


@allure.epic('EM test project')
@allure.suite('UI tests')
@allure.title('Добавления продукта в корзину')
def test_add_product_to_cart(login_as_user):
    page = login_as_user
    page.click_on_product_name()
    page.click_add_to_cart_button()
    page.assert_product_added_to_cart()


@allure.epic('EM test project')
@allure.suite('UI tests')
@allure.title('Переход в корзину')
def test_shopping_cart_button(login_as_user):
    page = login_as_user
    page.click_on_product_name()
    page.click_add_to_cart_button()
    page.click_shopping_cart_button()
    page.assert_proceed_to_checkout()


@allure.epic('EM test project')
@allure.suite('UI tests')
@allure.title('Нажатие на кнопку Checkout')
def test_checkout_button(login_as_user):
    page = login_as_user
    page.click_on_product_name()
    page.click_add_to_cart_button()
    page.click_shopping_cart_button()
    page.click_checkout_button()
    page.assert_proceed_to_user_information()


@allure.epic('EM test project')
@allure.suite('UI tests')
@allure.title('Заполнение данных пользователя')
def test_fill_user_data(login_as_user):
    page = login_as_user
    page.click_on_product_name()
    page.click_add_to_cart_button()
    page.click_shopping_cart_button()
    page.click_checkout_button()
    page.fill_first_name()
    page.fill_last_name()
    page.fill_postal_code()
    page.click_continue_button()
    page.assert_proceed_to_order_overwiev()


@allure.epic('EM test project')
@allure.suite('UI tests')
@allure.title('Testcase #1. Покупка товара пользователем')
def test_complete_purchase(browser):
    page = ProductsPage(browser)
    page.fill_login_field()
    page.fill_password_field()
    page.click_login_button()
    page.click_on_product_name()
    page.click_add_to_cart_button()
    page.click_shopping_cart_button()
    page.click_checkout_button()
    page.fill_first_name()
    page.fill_last_name()
    page.fill_postal_code()
    page.click_continue_button()
    page.click_finish_button()
    page.assert_complete_purchase()
