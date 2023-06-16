from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')

username_form = driver.find_element(By.CSS_SELECTOR, '#user-name')
password_form = driver.find_element(By.CSS_SELECTOR, '#password')
log_button = driver.find_element(By.CSS_SELECTOR, '#login-button')
if username_form is not None and password_form is not None and log_button is not None:
    print('Элементы найдены')
