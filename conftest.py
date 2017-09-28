import os

import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from application import Application
from work_dir import driver, environment


def pytest_addoption(parser):
    parser.addoption('--url', action='store', default='https://www.gosuslugi.ru', help='server url')
    parser.addoption('--browser', action='store', default='chrome', help='browser type')
    parser.addoption("--work_dir", action="store",
                     default=os.path.abspath(os.path.join(os.path.dirname(__file__), 'work_dir')),
                     help="path to dir with input data")

@pytest.fixture(scope="session")
def optns(request):
    ops = {}
    ops['browser'] = request.config.getoption("--browser")
    ops['base_url'] = request.config.getoption("--url")
    ops['work_dir'] = request.config.getoption("--work_dir")
    return ops


@pytest.fixture(scope="session", autouse=True)
def test_session(optns, request):
    if optns['browser'] == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--start-maximized")
        if os.name != 'nt':
            chrome_options.add_argument("--start-fullscreen")

        # enable browser logging and unexpectedAlertBehaviour
        dc = DesiredCapabilities.CHROME
        dc["unexpectedAlertBehaviour"] = "accept"  # "accept", "dismiss","ignore"
        driver.driver = create_drive(chrome_options, dc)

    def close_testing_session():
        print("resource_teardown")
        driver.driver.quit()

    request.addfinalizer(close_testing_session)


@pytest.fixture(scope="session")
def app(optns, request):
    return Application()

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        driver.driver.quit()


@pytest.fixture(scope="session")
def env(optns, request):
    environment.Server.url = optns['base_url']
    return environment

def create_drive(co, dc):
    return webdriver.Chrome(chrome_options=co, desired_capabilities=dc)