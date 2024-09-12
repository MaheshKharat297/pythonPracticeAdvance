from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time

browser_name = "chrome"

if browser_name == "chrome":
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
elif browser_name == "firefox":
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
else:
    print("Invalid value in browser name !")

driver.implicitly_wait(5)
driver.get("https://www.google.com/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.ID, 'APjFqb').send_keys("Mahesh Kharat")
time.sleep(5)
driver.find_element(By.XPATH, "//input[@aria-label='Google Search']").click()
time.sleep(5)
title = driver.title
print("The title is : ", title)

driver.quit()