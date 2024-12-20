Testcases
page_object
conftest.py
pytest.ini
config.ini
test_data

@pytest.mark.smoke
def test_login():
    assert True

get_screenshot_as_png
import requests
name = "mahesh"
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.get("https://dummy-json.mock.beeceptor.com/continents",
                        data=payload, headers={'Content-Type': 'application/json'}).json()
name = response.data[name][0]
assert name == name


def login():
    try:
        uname = "mahesh"
        pwd = "kharat"
        user_name = driver.find_element(By.NAME, "username")
        user_name.send_keys(uname)
        password = driver.find_element(By.NAME, "password")
        password.send_keys(pwd)
        submit_button = driver.find_element(By.NAME, "Submit")
        submit_button.click()
    catch exception as e:
        print(e)


for i in range(3):
    if drop_dwn2:
        drop_dwn2.click()
        break





