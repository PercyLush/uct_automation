import json
import re
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://uct.ac.za/students/study-uct-degrees-diplomas-science/science-undergraduate'

driver = webdriver.Chrome()

driver.get(url)
data = []
courses = driver.find_elements(By.XPATH, '//*[@id="block-blip-uct-mainpagecontent"]/article/div/div/p[2]')

for Text in courses:
    data.append(Text.text)

driver.quit()

pattern = r'(Bachelor\s*of\s*Science\n)'

DATA = []

for item in data:
    final_data = re.sub(pattern, r'', item)
    DATA.append(final_data)

with open('science.json', 'w') as file:
   json.dump(DATA, file, indent=2)