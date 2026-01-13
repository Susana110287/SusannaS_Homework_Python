import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


class TestSlowCalculator:
    def test_calculator_result(self, browser: WebDriver):
        # Открываем страницу
        browser.get(
         "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
            )

        # Установка задержки на 45 секунд
        delay_input = browser.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys("45")

        # Локаторы кнопок калькулятора
        xpath_buttons = {
            "7": "//span[contains(text(), '7')]",
            "+": "//span[contains(text(), '+')]",
            "8": "//span[contains(text(), '8')]",
            "=": "//span[contains(text(), '=')]",
        }

        # Номиналы кнопок и соответствующие им запросы
        buttons = {}
        for key, xpath in xpath_buttons.items():
            buttons[key] = browser.find_element(By.XPATH, xpath)

        # Последовательное нажатие кнопок
        buttons["7"].click()
        buttons["+"].click()
        buttons["8"].click()
        buttons["="].click()

        # Ждём, пока результат станет равным 15
        wait = WebDriverWait(browser, 50)
        # даём запас в 5 секунд на случай задержек
        wait.until(EC.text_to_be_present_in_element
                   ((By.CLASS_NAME, "screen"), "15"))
        # Проверяем результат
        result = browser.find_element(By.CLASS_NAME, "screen").text
        err_msg = f"Результат не совпадает с ожидаемым. Получено: {result}"
        assert result == "15", err_msg
