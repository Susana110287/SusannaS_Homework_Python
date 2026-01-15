import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


class TestDataTypesFormSubmission:
    def test_data_types_form_submission(self, browser):
        # Открываем главную страницу
        browser.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

        # Поиск элементов формы
        first_name_field = browser.find_element(By.NAME, "first-name")
        last_name_field = browser.find_element(By.NAME, "last-name")
        address_field = browser.find_element(By.NAME, "address")
        email_field = browser.find_element(By.NAME, "e-mail")
        phone_number_field = browser.find_element(By.NAME, "phone")
        zip_code_field = browser.find_element(By.NAME, "zip-code")  # пустое
        city_field = browser.find_element(By.NAME, "city")
        country_field = browser.find_element(By.NAME, "country")
        job_position_field = browser.find_element(By.NAME, "job-position")
        company_field = browser.find_element(By.NAME, "company")
        submit_button = browser.find_element(
            By.CSS_SELECTOR, ".btn.btn-outline-primary.mt-3"
        )

        # Заполняем поля
        first_name_field.send_keys("Иван")
        last_name_field.send_keys("Петров")
        address_field.send_keys("Ленина, 55-3")
        email_field.send_keys("test@skypro.com")
        phone_number_field.send_keys("+7985899998787")
        zip_code_field.clear()  # принудительно очищаем
        city_field.send_keys("Москва")
        country_field.send_keys("Россия")
        job_position_field.send_keys("QA")
        company_field.send_keys("SkyPro")

        # Отправляем форму
        submit_button.click()

        # Ждём завершения обработки формы и появления уведомления об успехе
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, ".alert-success"
            )))

        # Проверяем поле Zip code — должно быть красным (danger)
        zip_element = browser.find_element(By.ID, "zip-code")
        assert "danger" in zip_element.get_attribute("class"), (
            "Поле Zip code должно быть подсвечено красным (класс danger)"
        )

        # Проверяем остальные поля — должны быть зелёными (success)
        fields_to_check = [
            "first-name", "last-name", "address", "e-mail", "phone",
            "city", "country", "job-position", "company"
        ]

        for field_id in fields_to_check:
            element = browser.find_element(By.ID, field_id)
            assert "success" in element.get_attribute("class"), (
                f"Поле {field_id} должно "
                f"быть подсвечено зелёным (класс success)"
            )
