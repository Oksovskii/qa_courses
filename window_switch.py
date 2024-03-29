from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = browser.find_element(By.ID, "book")
price = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

button.click()

value = browser.find_element(By.ID, "input_value")
input = browser.find_element(By.ID, "answer")
input.send_keys(calc(value.text))

submin_button = browser.find_element(By.ID, "solve")
submin_button.click()


time.sleep(20)