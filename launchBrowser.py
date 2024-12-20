from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.google.com/")

driver.implicitly_wait(10)
time.sleep(5)

driver.close()

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("https://www.google.com/")
time.sleep(5)

driver.close()




