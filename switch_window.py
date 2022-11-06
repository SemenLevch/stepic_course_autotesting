from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)

    subm = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    subm.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

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