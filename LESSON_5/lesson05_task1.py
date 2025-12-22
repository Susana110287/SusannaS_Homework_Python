from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))

try:
    driver.maximize_window()
    driver.get("http://uitestingplayground.com/classattr")
    sleep(2)

    button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    button.click()
    sleep(2)

    print("Скрипт выполнен успешно: кнопка нажата!")

finally:
    driver.quit()
