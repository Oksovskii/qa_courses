from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "https://vk.com/im?sel=63858042"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, '//*[@id="index_email"]')
    input1.send_keys("89535101988")
    button = browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/form/button')
    button.click()
    time.sleep(0.5)
    button = browser.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/div/div/div/div/form/div[3]/button')
    button.click()
    

    #input4 = browser.find_element(By.ID, "country")
    #input4.send_keys("Russia")
    #button = browser.find_element(By.XPATH, "/html/body/div/form/div[6]/button[3]")
    #button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла