import datetime
import logging
import logging.handlers
import os
from logging.handlers import RotatingFileHandler
from pathlib import Path

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.webdriver import WebDriver

from pages.products_page import ProductsPage
from api_client.api_client import ApiClient

load_dotenv()


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox')
    parser.addoption('--url', action='store', default=os.getenv('LOGIN_URL'))
    parser.addoption('--log_level', action='store', default="INFO")
    parser.addoption('--executor', action='store')
    parser.addoption('--browser_version', action='store')


@pytest.fixture(scope='function')
def logger(request):
    log_dir = Path(__file__).parent / 'log'
    log_dir.mkdir(exist_ok=True)
    log_level = request.config.getoption('--log_level')
    browser_name = request.config.getoption('--browser')
    logger = logging.getLogger(request.node.name)
    file_handler = RotatingFileHandler(
        str(log_dir / f'{request.node.name}({browser_name}).log'),
        maxBytes=30000000,
        backupCount=3)
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info('===> Test %s started at %s' % (request.node.name, datetime.datetime.now()))

    yield logger

    logger.info('===> Test %s finished at %s' % (request.node.name, datetime.datetime.now()))

    for handler in logger.handlers:
        handler.close()
    logger.handlers.clear()


@pytest.fixture()
def browser(request, logger) -> WebDriver:
    browser_name = request.config.getoption('--browser')
    browser_version = request.config.getoption('--browser_version')
    executor = request.config.getoption('--executor')
    url = request.config.getoption('--url')

    if executor:
        if browser_name == 'chrome':
            options = ChromeOptions()
        elif browser_name == 'firefox':
            options = FirefoxOptions()
        elif browser_name == 'edge':
            options = EdgeOptions()
        else:
            raise ValueError(
                'Browser name must be "chrome", "firefox" or "edge"'
            )
        options.headless = False
        capabilities = {
            'browserName': browser_name,
            'browserVersion': browser_version,
        }
        for key, value in capabilities.items():
            options.set_capability(key, value)

        driver = webdriver.Remote(
            command_executor=f'http://{executor}:4444/wd/hub',
            options=options
        )
        driver.maximize_window()
    else:
        if browser_name == 'chrome':
            options = webdriver.ChromeOptions()
            # options.add_argument("--headless=new")
            driver = webdriver.Chrome(options=options)
        elif browser_name == 'firefox':
            options = webdriver.FirefoxOptions()
            # options.add_argument("--headless")
            driver = webdriver.Firefox(options=options)
            # driver.fullscreen_window()
        elif browser_name == 'edge':
            options = webdriver.EdgeOptions()
            options.use_chromium = True
            # options.add_argument("--headless=new")
            driver = webdriver.Edge(options=options)
        else:
            raise ValueError(
                'Browser name must be "chrome", "firefox" or "edge"'
            )
    driver.get(url)
    driver.url = url
    driver.logger = logger
    driver.test_name = request.node.name

    yield driver
    driver.quit()


@pytest.fixture()
def login_as_user(browser) -> ProductsPage:
    page = ProductsPage(browser)
    page.fill_login_field()
    page.fill_password_field()
    page.click_login_button()
    return page


@pytest.fixture()
def create_test_repository(logger) -> ApiClient:
    api_client = ApiClient('https://api.github.com', logger)
    api_client.logger.info('* (SETUP) Create new repository for test"')
    api_client.create_repository(name='my737373')


@pytest.fixture()
def delete_test_repository(logger) -> ApiClient:
    yield
    api_client = ApiClient('https://api.github.com', logger)
    api_client.logger.info('* (TEARDOWN) Delete new repository for test"')
    api_client.delete_repository(name='my737373')
