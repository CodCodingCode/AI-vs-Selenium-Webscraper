from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


import time

list = "test"
driver = webdriver.Chrome()


driver.get('https://www.google.com')

input_element = driver.find_element(By.CLASS_NAME, 'gLFyf')
time.sleep(10)
driver.quit()

input_element.send_keys(f"{list}" + Keys.ENTER)