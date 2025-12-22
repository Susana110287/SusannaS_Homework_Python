from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    # 1. Открываем страницу
    driver.get("http://uitestingplayground.com/textinput")

    # 2. Ждём поле ввода (id="newButtonName") и вводим текст
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#newButtonName"))
    )
    input_field.clear()
    input_field.send_keys("SkyPro")

    # 3. Ждём кнопку (id="updatingButton") и кликаем
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#updatingButton"))
    )
    button.click()

    # 4. Получаем актуальный текст кнопки и выводим в консоль
    button_text = button.text.strip()
    print(f'"{button_text}"')

finally:
    driver.quit()
