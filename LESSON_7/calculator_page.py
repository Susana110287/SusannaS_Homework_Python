from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.digit_buttons = {
            "7": (By.XPATH, "//span[contains(text(), '7')]"),
            "+": (By.XPATH, "//span[contains(text(), '+')]"),
            "8": (By.XPATH, "//span[contains(text(), '8')]"),
            "=": (By.XPATH, "//span[contains(text(), '=')]")
        }
        self.result_display = (By.CLASS_NAME, "screen")

    def set_delay(self, seconds):
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    def click_digit_or_operator(self, value):
        button = self.driver.find_element(*self.digit_buttons[value])
        button.click()

    def get_result(self):
        # Ждём появления элемента, затем проверяем его текст
        result_element = WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located(self.result_display)
        )
        # Теперь ждём, пока текст станет "15"
        WebDriverWait(self.driver, 60).until(
            lambda driver: result_element.text.strip() == "15"
        )
        return result_element.text.strip()
