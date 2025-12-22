from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# Инициализация драйвера Firefox (автоматическая установка GeckoDriver)
driver = webdriver.Firefox(service=FirefoxService
                           (GeckoDriverManager().install()))

try:
    # Разворачиваем окно на весь экран
    driver.maximize_window()

    # Переход на целевую страницу
    driver.get("http://the-internet.herokuapp.com/inputs")

    # Ожидание загрузки страницы (2 секунды)
    sleep(2)

    # Находим текстовое поле (на странице оно единственное)
    input_field = driver.find_element(By.TAG_NAME, "input")

    # Вводим текст "Sky"
    input_field.send_keys("Sky")
    print('Введено: "Sky"')
    sleep(1)  # Пауза для визуального контроля

    # Очищаем поле
    input_field.clear()
    print("Поле очищено")
    sleep(1)

    # Вводим текст "Pro"
    input_field.send_keys("Pro")
    print('Введено: "Pro"')
    sleep(1)

    print("Скрипт выполнен успешно!")

finally:
    # Корректное закрытие браузера
    driver.quit()
