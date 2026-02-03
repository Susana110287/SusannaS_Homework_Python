from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """
    Класс, представляющий страницу калькулятора.
    Содержит методы для взаимодействия с элементами калькулятора.
    """

    def __init__(self, driver):
        """
        Инициализирует объект страницы калькулятора.

        Параметры:
        driver (webdriver): экземпляр WebDriver для управления браузером
        """
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.digit_buttons = {
            "7": (By.XPATH, "//span[contains(text(), '7')]"),
            "+": (By.XPATH, "//span[contains(text(), '+')]"),
            "8": (By.XPATH, "//span[contains(text(), '8')]"),
            "=": (By.XPATH, "//span[contains(text(), '=')]")
        }
        self.result_display = (By.CLASS_NAME, "screen")

    def set_delay(self, seconds: int):
        """
        Устанавливает задержку в калькуляторе.

        Параметры:
        seconds (int): количество секунд задержки

        Возвращаемое значение:
        None
        """
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    def click_digit_or_operator(self, value: str):
        """
        Нажимает кнопку с указанной цифрой или оператором.

        Параметры:
        value (str): символ кнопки (например, '7', '+', '8', '=')

        Возвращаемое значение:
        None

        Исключения:
        KeyError: если указанный символ отсутствует в словаре digit_buttons
        NoSuchElementException: если элемент не найден на странице
        """
        button = self.driver.find_element(*self.digit_buttons[value])
        button.click()

    def get_result(self) -> str:
        """
        Получает результат вычисления из дисплея калькулятора.
        Ожидает появления элемента и проверки текста "15".

        Возвращаемое значение:
        str: текст результата (в данном случае ожидается "15")

        Исключения:
        TimeoutException: если элемент не виден в течение 60 секунд
                       или текст не становится равным "15" в течение 60 секунд
        """
        # Ждём появления элемента, затем проверяем его текст
        result_element = WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located(self.result_display)
        )
        # Теперь ждём, пока текст станет "15"
        WebDriverWait(self.driver, 60).until(
            lambda driver: result_element.text.strip() == "15"
        )
        return result_element.text.strip()
