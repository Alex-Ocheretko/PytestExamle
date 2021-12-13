import pytest
from selenium import webdriver


@pytest.fixture
def driver(browser, request):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
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
    driver.implicitly_wait(7)
    request.cls.driver = driver
    driver.get("https://demoqa.com/")
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="My options: chrome or firefox"
    )


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")
