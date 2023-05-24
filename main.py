from selenium import webdriver
from selenium.webdriver.common.by import By
import json

with open('config.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

errors = []

for login in data['logins']:
    try:
        driver = webdriver.Chrome(executable_path='chromedriver/chromedriver')
        driver.get(url='https://iccup.com/community/')

        login_input = driver.find_element(by=By.ID, value='login')
        login_input.clear()
        login_input.send_keys(login)

        pass_input = driver.find_element(by=By.ID, value='passw')
        pass_input.clear()
        pass_input.send_keys(data['password'])

        dologin = driver.find_element(by=By.CLASS_NAME, value='auth-button').click()

        driver.get(url='https://iccup.com/settings.html')

        current_password = driver.find_element(by=By.ID, value='inp-current-password')
        current_password.clear()
        current_password.send_keys(data['password'])

        new_password = driver.find_element(by=By.ID, value='inp-new-password')
        new_password.clear()
        new_password.send_keys(data['new_password'])

        confirm_new_password = driver.find_element(by=By.ID, value='inp-confirm-new-password')
        confirm_new_password.clear()
        confirm_new_password.send_keys(data['new_password'])

        save_button = driver.find_element(by=By.ID, value='reg-btn').click()
    except Exception as e:
        errors.append(login)
    finally:
        driver.close()
        driver.quit()

with open('errors.txt', 'w') as f:
    for login in errors:
        f.write(f"{login}\n")
