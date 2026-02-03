import pytest
import allure
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture(scope="function")
def browser():
    """
    Фикстура для инициализации браузера перед каждым тестом.

    Возвращаемое значение:
    webdriver: экземпляр WebDriver
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.feature("Калькулятор с задержкой")
class TestSlowCalculator:
    """
    Тестовый класс для проверки работы калькулятора с задержкой.
    """

    @allure.title("Проверка результата вычисления 7 + 8")
    @allure.description(
        "Тест проверяет, что калькулятор корректно " +
        "вычисляет сумму 7 + 8 с задержкой 45 секунд"
        )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_calculator_result(self, browser):
        """
        Тест для проверки результата " +
        "вычисления 7 + 8 в калькуляторе с задержкой.

        Параметры:
        browser (webdriver): экземпляр WebDriver, предоставляемый фикстурой

        Возвращаемое значение:
        None
        """
        with allure.step("Открытие страницы калькулятора"):
            browser.get((
                "https://bonigarcia.dev/selenium-webdriver-java/"
                "slow-calculator.html"
                        ))

        with allure.step("Создание объекта страницы калькулятора"):
            page = CalculatorPage(browser)

        with allure.step("Установка задержки на 45 секунд"):
            page.set_delay(45)

        with allure.step("Нажатие кнопок: 7, +, 8, ="):
            page.click_digit_or_operator('7')
            page.click_digit_or_operator('+')
            page.click_digit_or_operator('8')
            page.click_digit_or_operator('=')

        with allure.step("Получение результата вычисления"):
            result = page.get_result()

        with allure.step(
            f"Проверка результата: ожидаемое '15', полученное '{result}'"
        ):
            assert result == "15", (
                f"Результат не совпадает с ожидаемым. Получено: {result}"
            )
