import os

from selenium.webdriver.common.by import By


class Selectors:

    LOGIN_FIELD = (By.ID, 'user-name')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    PRODUCTS_PAGE_TITLE = (By.CLASS_NAME, 'title')
    PRODUCT_NAME = (
        By.XPATH,
        '//*[@class="inventory_item_name " and '
        'contains(text(), "Sauce Labs Backpack")]'
    )
    PRODUCT_PAGE_TITLE = (By.CLASS_NAME, 'inventory_details_name')
    ADD_TO_CART_BUTTON = (By.ID, 'add-to-cart')
    SHOPPING_CART_BADGE = (By.CLASS_NAME, 'shopping_cart_badge')
    PAGE_TITLE = (By.CLASS_NAME, 'title')
    CHECKOUT_BUTTON = (By.ID, 'checkout')
    FIRST_NAME = (By.ID, 'first-name')
    LAST_NAME = (By.ID, 'last-name')
    POSTAL_CODE = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')
    FINISH_BUTTON = (By.ID, 'finish')
    ENDPOINT_REPOSITORIES = f'/{os.getenv("GIT_USER")}/repos'
