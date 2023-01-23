from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    buttom = browser.find_element(By.TAG_NAME,"button")
    buttom.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    time.sleep(1)

    x_element = browser.find_element(By.ID,"input_value")
    x = x_element.text
    y = calc(x)

    text_element = browser.find_element(By.CSS_SELECTOR,"#answer")
    text_element.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR,".btn")
    button.click()

finally:

    time.sleep(7)
    browser.quit()


