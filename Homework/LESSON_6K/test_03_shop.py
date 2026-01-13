import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_purchase_flow(browser):
    # 1. Открыть сайт
    browser.get("https://www.saucedemo.com/")

    # 2. Авторизация
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()

    # 3. Ожидание загрузки товаров
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    # 4. Добавление товаров в корзину
    items_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    for item_name in items_to_add:
        # Находим элемент по названию и ищем кнопку внутри контейнера
        item_container = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 f"//div[@class='inventory_item' and "
                 f".//div[text()='{item_name}']]")
            )
        )
        add_button = item_container.find_element(
            By.CLASS_NAME, "btn_inventory"
        )
        add_button.click()

    # 5. Переход в корзину
    cart_link = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
    )
    cart_link.click()

    # 6. Checkout
    checkout_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    )
    checkout_button.click()

    # 7. Заполнение формы
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "first-name"))
    ).send_keys("Сюзанна")
    browser.find_element(By.ID, "last-name").send_keys("Савинова")
    browser.find_element(By.ID, "postal-code").send_keys("658060")

    continue_button = browser.find_element(By.ID, "continue")
    continue_button.click()

    # 8. Проверка итоговой суммы
    total_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    total_text = total_element.text
    total_amount = float(total_text.split("$")[1])

    assert total_amount == 58.29, (
        f"Ожидаемая сумма $58.29, но получено ${total_amount}"
    )
