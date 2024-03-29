from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from removeMonths import months
import time

list = ["OpenAI", "Deepmind", "Cohere"] #, "EleutherAI", "Mistral", "META", "Microsoft", "IBM", "Google", "Tesla"]
driver = webdriver.Chrome()



possible_hackathons = []
for i in range(3):
    driver.get('https://www.google.com')

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
    )

    input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
    input_element.clear()
    for month in months:
        try:
            input_element.send_keys(f"{list[i]} Hackathon 2024 14+ {month}" + Keys.ENTER)
            link = driver.find_element(By.PARTIAL_LINK_TEXT)
            link.click()
            possible_hackathons.append(driver.current_url)
            break
        except:
            continue    
    time.sleep(5)
driver.quit()
print(possible_hackathons)
