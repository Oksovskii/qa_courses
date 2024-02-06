from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/execute_script.html"
browser.get(link)
value = browser.find_element(By.ID, "input_value")
print(value.text)

input_field = browser.find_element(By.ID, "answer")
input_field.send_keys(calc(value.text))

button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

robot_check = browser.find_element(By.ID, "robotCheckbox")
robot_check.click()

robot_check = browser.find_element(By.ID, "robotsRule")
robot_check.click()


#browser.execute_script()

button.click()
time.sleep(10)