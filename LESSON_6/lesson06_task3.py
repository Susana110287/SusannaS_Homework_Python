from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Инициализация драйвера
driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))

try:
    # 1. Переход на сайт
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )

    # 2. Ждём все изображения
    WebDriverWait(driver, 15).until(
        EC.visibility_of_all_elements_located((By.TAG_NAME, "img"))
    )

    # 3. Ищем именно 3‑ю картинку
    third_image = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "award"))
    )

    # 4. Получаем значение атрибута src
    src = third_image.get_attribute("src")

    # 5. Выводим в консоль
    print(src)

except TimeoutException:
    print("Элемент не найден за отведённое время (15 сек)")

finally:
    # 6. Закрываем браузер
    driver.quit()
