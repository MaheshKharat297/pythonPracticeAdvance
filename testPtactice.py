# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#
# driver.get("www.google.com")
# driver.implicitly_wait(10)

# def uniq_find(lst):
#     for i in lst:
#         i = i.lower()
#         new_lst = list(set(i))
#         l = len(new_lst)
#         x = len(i)
#         if l == x:
#             print(i)
#
# lst = ["msrt","Gogle","apple"]
# uniq_find(lst)

def max_find(lst):
    count = 0
    max_3 = []
    lst = list(set(lst))
    for i in range(len(lst)):
        max = 0
        for j in lst:
            if j > max:
                max = j
        if count < 3 and max not in max_3:
            lst.remove(max)
            max_3.append(max)
            count += 1
        elif max in max_3:
            count += 0

    print(max_3[2])

lst = [4,5,4,2,3,1,0,5,3,10]
max_find(lst)








