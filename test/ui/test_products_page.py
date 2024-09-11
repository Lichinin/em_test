from pages.base_page import BasePage


def test_login(browser):
    page = BasePage(browser)
    page.fill_login_field()
    page.fill_password_field()
    page.click_login_button()
    page.assert_proceed_to_products_page()


def test_go_to_product_page(login_as_user):
    page = login_as_user
    page.click_on_product_name()
    page.assert_proceed_to_product_page()


def test_add_product_to_cart(login_as_user):
    page = login_as_user
    page.click_on_product_name()
    page.click_add_to_cart_button()
    page.assert_product_added_to_cart()


def test_shopping_cart_button(login_as_user):
    page = login_as_user
    page.click_on_product_name()
    page.click_add_to_cart_button()
    page.click_shopping_cart_button()
    page.assert_proceed_to_checkout()


def test_checkout_button(login_as_user):
    page = login_as_user
    page.click_on_product_name()
    page.click_add_to_cart_button()
    page.click_shopping_cart_button()
    page.click_checkout_button()
    page.assert_proceed_to_user_information()


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


def test_complete_purchase(login_as_user):
    page = login_as_user
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
