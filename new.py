from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)

num_1 = browser.find_element(By.ID,'num1')

num_2 = browser.find_element(By.ID,'num2')

sigma=(int(num_1.text)+int(num_2.text))

print(sigma)

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(f"{str(sigma)}")

#submit_button = browser.find_element(By.XPATH, "/html/body/div/form/button")
#submit_button.click()

browser.execute_script("document.title='Script executing';alert('Robots at work');")

time.sleep(10)