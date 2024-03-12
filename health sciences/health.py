import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://uct.ac.za/students/study-uct-degrees-diplomas-health-sciences/health-sciences-undergraduate'

driver = webdriver.Chrome()

driver.get(url)
new_course = []

for j in range(2, 7):
    course = []
    for p in driver.find_elements(By.XPATH, f'//*[@id="block-blip-uct-mainpagecontent"]/article/div/div/p[{j}]'):
        for strong in p.find_elements(By.XPATH, f'//*[@id="block-blip-uct-mainpagecontent"]/article/div/div/p[{j}]/strong'):
            course.append(strong.text)

    new_list = course[0].split('\n')

    for i in range(len(new_list)):
        module = {"Qualification": new_list[i]}
        new_course.append(module)
    sleep(0.5)

driver.quit()

with open('health.json', 'w') as file:
   json.dump(new_course, file, indent=2)