import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://uct.ac.za/students/study-uct-degrees-diplomas-commerce/commerce-undergraduate'

driver = webdriver.Chrome()

driver.get(url)
new_course = []

for j in range(5, 9):
    course = []
    for br in driver.find_elements(By.XPATH, f'//*[@id="block-blip-uct-mainpagecontent"]/article/div/div/p[{j}]'):
        course.append(br.text)

    new_list = course[0].split('\n')

    for i in range(1, len(new_list)):
        module = {"Qualification": f"{new_list[0]} {new_list[i]}"}
        new_course.append(module)
    sleep(0.5)

driver.quit()

with open('commerce.json', 'w') as file:
   json.dump(new_course, file, indent=2)