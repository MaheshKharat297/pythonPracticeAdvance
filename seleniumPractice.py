import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager

browsers = ["Chrome", "Firefox"]

for browser in browsers:
    if browser == "Chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == "Fir efox":
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    driver.get("https://www.google.com/")
    time.sleep(5)
    driver.maximize_window()
    driver.close()