from _pytest.fixtures import SubRequest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import os

from utils.base_utils import BASE_UPL


@pytest.fixture
def driver(browser, request):
    match browser:
        case "chrome":
            driver = init_chrome()
        case "firefox":
            capabilities = {
                "browserName": "firefox",
                "browserVersion": "88.0",
                "selenoid:options": {
                    "enableVNC": True,
                    "enableVideo": False
                }
            }
            driver = webdriver.Remote(
                command_executor="http://192.168.0.1",
                desired_capabilities=capabilities)
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    driver.get(BASE_UPL)
    yield driver
    driver.quit()


def init_chrome() -> WebDriver:
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=install_ad_blocker())
    wait_until_ad_blocker_installed(driver)
    return driver


def install_ad_blocker() -> Options:
    path_to_extension = 'extentions/AdBlock-—-best-ad-blocker.crx'
    full_path = os.path.join(os.path.dirname(__file__), path_to_extension)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_extension(full_path)
    return chrome_options


def wait_until_ad_blocker_installed(driver):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.installed__container"))
        )
    except Exception as e:
        print(f"Ad Blocker has not been installed: {str(e)}")
    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[1])
    driver.close()
    driver.switch_to.window(window_handles[0])


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="My options: chrome or firefox"
    )


@pytest.fixture
def browser(request) -> SubRequest:
    return request.config.getoption("--browser")
