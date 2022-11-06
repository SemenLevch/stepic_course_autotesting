from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)

    book_but = browser.find_element(By.ID, "book")

    opt_price = WebDriverWait(browser, 12).until(
        expected_conditions.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    book_but.click()

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