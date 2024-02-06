from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
button.click()

alert = browser.switch_to.alert
alert.accept()

value = browser.find_element(By.ID, "input_value")
print(value.text)

input = browser.find_element(By.ID, "answer")
input.send_keys(calc(value.text))

button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
button.click()

time.sleep(10)