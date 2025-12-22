from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

# Инициализация драйвера Firefox (автоматическая установка GeckoDriver)
driver = webdriver.Firefox(service=FirefoxService
                           (GeckoDriverManager().install()))

try:
    # Разворачиваем окно на весь экран
    driver.maximize_window()

    # Переход на страницу логина
    driver.get("http://the-internet.herokuapp.com/login")

    # Ожидание загрузки страницы
    sleep(2)

    # Ввод логина
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")
    print("Логин введён: tomsmith")

    # Ввод пароля
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")
    print("Пароль введён: SuperSecretPassword!")

    # Нажатие кнопки Login
    LOGIN_BUTTON_SELECTOR = "button[type='submit']"
    login_button = driver.find_element(By.CSS_SELECTOR, LOGIN_BUTTON_SELECTOR)
    login_button.click()
    print("Кнопка Login нажата")

    # Ожидание появления зелёного уведомления (успешный вход)
    wait = WebDriverWait(driver, 10)
    success_alert = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".flash.success"))
    )

    # Получение текста из уведомления
    alert_text = success_alert.text.strip()
    print("Текст из зелёной плашки:")
    print(alert_text)

finally:
    # Корректное закрытие браузера
    driver.quit()
