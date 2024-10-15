# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#
# driver.get("www.google.com")
# driver.implicitly_wait(10)

def uniq_find(lst):
    for i in lst:
        i = i.lower()
        new_lst = list(set(i))
        l = len(new_lst)
        x = len(i)
        if l == x:
            print(i)

lst = ["msrt","Gogle","apple"]
uniq_find(lst)









