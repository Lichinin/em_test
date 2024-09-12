import os

import allure
from dotenv import load_dotenv
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators import Selectors

load_dotenv()


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger

    @allure.step('Поиск элемента на странице')
    def get_element(self, locator: tuple, timeout=3):
        try:
            self.browser.logger.info(f'* Get element "{repr(locator)}"')
            return WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except Exception:
            self.logger.exception('Error: element not found!')
            raise

    @allure.step('Ввожу в поле "{locator}" текст "{text}"')
    def fill_the_field(self, locator, text):
        field = self.get_element(locator)
        field.click()
        field.send_keys(text)
        return field

    @allure.step('Проверка assert_equals')
    def assert_equals(self, expected, actual):
        self.logger.info(
            f'* Check assertion between expected '
            f'({expected}) and actual ({actual})'
        )
        try:
            assert expected == actual, f"Expected: '{expected}', Actual: '{actual}'"
            self.logger.info('*** Test completed successful ***')
        except AssertionError:
            self.logger.exception('!!! Test failed !!!')
            raise

    @allure.step('Вводится логин пользователя')
    def fill_login_field(self):
        self.fill_the_field(Selectors.LOGIN_FIELD, os.getenv('LOGIN'))

    @allure.step('Вводится пароль пользователя')
    def fill_password_field(self):
        self.fill_the_field(Selectors.PASSWORD_FIELD, os.getenv('PASSWORD'))

    @allure.step('Нажимается кнопка Login')
    def click_login_button(self):
        self.get_element(Selectors.LOGIN_BUTTON).click()

    @allure.step('Выполняется проверка перехода на страницу товаров')
    def assert_proceed_to_products_page(self):
        self.assert_equals(
            'Products',
            self.get_element(Selectors.PRODUCTS_PAGE_TITLE).text.strip()
        )
