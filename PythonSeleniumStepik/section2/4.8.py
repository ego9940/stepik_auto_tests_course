from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    b = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element(By.ID, "book").click()

    x_element = browser.find_element(By.ID,"input_value")
    x = x_element.text
    y = calc(x)

    text_element = browser.find_element(By.CSS_SELECTOR,"#answer")
    text_element.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR,"#solve")
    button.click()

finally:
    time.sleep(7)
    browser.quit()





