from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Инициализация драйвера Chrome (автоматическая установка ChromeDriver)
driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))

try:
    # Разворачиваем окно на весь экран
    driver.maximize_window()

    # Переход на целевую страницу
    driver.get("http://uitestingplayground.com/dynamicid")

    # Ожидание загрузки страницы (2 секунды)
    sleep(2)

    # Поиск кнопки по тексту (так как id динамический)
    button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")

    # Клик по кнопке
    button.click()

    # Пауза для визуального подтверждения клика
    sleep(2)

    print("Скрипт выполнен успешно: кнопка нажата!")

finally:
    # Корректное закрытие браузера
    driver.quit()
