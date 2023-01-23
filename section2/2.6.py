from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):

    return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser = webdriver.Chrome()
    browser.get("http://SunInJuly.github.io/execute_script.html")
    
    x_element = browser.find_element(By.ID,"input_value")
    x = x_element.text
    y = calc(x)

 

    text_element = browser.find_element(By.CSS_SELECTOR,"#answer")
    text_element.send_keys(y)

  

    check_element = browser.find_element(By.ID,"robotCheckbox")
    check_element.click()

    button = browser.find_element(By.CSS_SELECTOR,".btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    radio_element = browser.find_element(By.ID,"robotsRule")
    radio_element.click()
    
    button.click()

    

finally:

    time.sleep(7)
    browser.quit()
 

