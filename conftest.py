import os

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.webdriver import WebDriver

load_dotenv()


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox')
    parser.addoption('--url', action='store', default=os.getenv('LOGIN_URL'))
    parser.addoption('--executor', action='store')
    parser.addoption('--browser_version', action='store')


@pytest.fixture()
def browser(request) -> WebDriver:
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
    driver.test_name = request.node.name

    yield driver
    driver.quit()
