from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    subm = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    subm.click()

    browser.switch_to.alert.accept()

    x_value = browser.find_element(By.ID, "input_value").text
    x = int(x_value)
    y = calc(x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)


    subm = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    subm.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()