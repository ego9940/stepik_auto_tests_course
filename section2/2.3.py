from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects2.html")
    
    x = str(int(browser.find_element(By.ID,"num1").text) + int(browser.find_element(By.ID,"num2").text)) ## Сумма 2 элементов 
    print(x)

    select = Select(browser.find_element(By.ID,"dropdown"))
    select.select_by_value(x)

    button = browser.find_element(By.CSS_SELECTOR,".btn")
    button.click()

finally:
    time.sleep(7)
    browser.quit()

