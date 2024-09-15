import allure

from locators.locators import Selectors
from pages.base_page import BasePage

class ProductsPage(BasePage):

    @allure.step('Выполняется клик по названию товара')
    def click_on_product_name(self):
        self.get_element(Selectors.PRODUCT_NAME).click()

    @allure.step('Выполняется клик кнопке добавления товара в корзину')
    def click_add_to_cart_button(self):
        self.get_element(Selectors.ADD_TO_CART_BUTTON).click()

    @allure.step('Выполняется клик по иконке корзины')
    def click_shopping_cart_button(self):
        self.get_element(Selectors.SHOPPING_CART_BADGE).click()

    @allure.step('Выполняется клик по кнопке Checkout')
    def click_checkout_button(self):
        self.get_element(Selectors.CHECKOUT_BUTTON).click()

    @allure.step('Заполняется поле First Name')
    def fill_first_name(self):
        self.fill_the_field(Selectors.FIRST_NAME, 'firstname')

    @allure.step('Заполняется поле Last Name')
    def fill_last_name(self):
        self.fill_the_field(Selectors.LAST_NAME, 'lastname')

    @allure.step('Заполняется поле Postal Code')
    def fill_postal_code(self):
        self.fill_the_field(Selectors.POSTAL_CODE, '1234567')

    @allure.step('Выполняется клик по кнопке Continue')
    def click_continue_button(self):
        self.get_element(Selectors.CONTINUE_BUTTON).click()

    @allure.step('Выполняется клик по кнопке Finish')
    def click_finish_button(self):
        self.get_element(Selectors.FINISH_BUTTON).click()

    @allure.step('Выполняется проверка  перехода на страницу товара')
    def assert_proceed_to_product_page(self):
        self.assert_equals(
            'Sauce Labs Backpack',
            self.get_element(Selectors.PRODUCT_PAGE_TITLE).text
        )

    @allure.step('Выполняется проверка добавления товара в корзину')
    def assert_product_added_to_cart(self):
        self.assert_equals(
            '1',
            self.get_element(Selectors.SHOPPING_CART_BADGE).text
        )

    @allure.step('Выполняется проверка перехода в корзину')
    def assert_proceed_to_checkout(self):
        self.assert_equals(
            'Your Cart',
            self.get_element(Selectors.PAGE_TITLE).text
        )

    @allure.step('Выполняется проверка перехода на страницу данных покупателя')
    def assert_proceed_to_user_information(self):
        self.assert_equals(
            'Checkout: Your Information',
            self.get_element(Selectors.PAGE_TITLE).text
        )

    @allure.step('Выполняется проверка  перехода на страницу обзора заказа')
    def assert_proceed_to_order_overwiev(self):
        self.assert_equals(
            'Checkout: Overview',
            self.get_element(Selectors.PAGE_TITLE).text
        )

    @allure.step('Выполняется проверка успешного заказа')
    def assert_complete_purchase(self):
        self.assert_equals(
            'Checkout: Complete!',
            self.get_element(Selectors.PAGE_TITLE).text
        )
