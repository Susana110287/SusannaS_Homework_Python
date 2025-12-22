from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Инициализация драйвера
driver = webdriver.Chrome()

try:
    # Шаг 1: Переход на страницу
    driver.get("http://uitestingplayground.com/ajax")

    # Шаг 2: Нажатие на синюю кнопку
    button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton")
    button.click()

    # Шаг 3: Ожидание появления зелёной плашки и получение текста
    wait = WebDriverWait(driver, 10)  # Максимум 10 секунд ожидания
    success_element = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success"))
    )

    # Получаем текст из элемента
    text = success_element.text

    # Шаг 4: Вывод в консоль
    print(text)  # Ожидаемый вывод: "Data loaded with AJAX get request."

except TimeoutException:
    print("Ошибка: Элемент не появился в течение 10 секунд.")

finally:
    # Корректное закрытие браузера
    driver.quit()
