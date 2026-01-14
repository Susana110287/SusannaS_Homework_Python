import pytest
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


class TestSlowCalculator:
    def test_calculator_result(self, browser):
        # Открываем страницу
        browser.get(
         "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
            )

        # Создаем объект страницы
        page = CalculatorPage(browser)

        # Устанавливаем задержку на 45 секунд
        page.set_delay(45)

        # Нажимаем кнопки
        page.click_digit_or_operator('7')
        page.click_digit_or_operator('+')
        page.click_digit_or_operator('8')
        page.click_digit_or_operator('=')

        # Получаем результат
        result = page.get_result()

        # Проверяем результат
        assert result == "15", (
            f"Результат не совпадает с ожидаемым. Получено: {result}"
            )
