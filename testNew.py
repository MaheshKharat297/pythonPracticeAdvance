import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time


@pytest.fixture(scope="function")
def launch_chrome_browser():
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    time.sleep(5)
    driver.maximize_window()
    yield
    driver.close()


@pytest.fixture(scope="function")
def launch_firefox_browser():
    global driver
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    time.sleep(5)
    driver.maximize_window()
    yield
    driver.close()


def test_get_url(launch_firefox_browser):
    driver.get("https://www.google.com/")
    time.sleep(5)


@pytest.mark.parametrize("num, output", [(1, 11), (2, 24), (3, 33)])
def test_number_multiplication(num, output):
    assert num * 11 == output


@pytest.fixture(params=[("mahesh", "kharat"), ("Rihansh", "kharat"), ("Rohini", "kharat")])
def input_data(request):
    return request.param


def test_input_data(input_data):
    print(input_data[0])
    print(input_data[1])
