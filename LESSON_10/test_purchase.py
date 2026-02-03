import pytest
import allure
from selenium import webdriver
from page_objects import (
    LoginPage,
    InventoryPage,
    CartPage,
    CheckoutInfoPage,
    CheckoutOverviewPage,
)


@pytest.fixture
def browser():
    """
    Фикстура для инициализации браузера.

    Возвращаемое значение:
    webdriver: экземпляр WebDriver
    """
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@allure.feature("Оформление заказа")
class TestPurchaseFlow:
    """
    Тестовый класс для проверки процесса покупки.
    """

    @allure.title("Проверка полного цикла покупки")
    @allure.description("Проверяет процесс покупки: " +
                        "авторизация, добавление товаров,"
                        "оформление заказа и проверка суммы.")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_purchase_flow(self, browser):
        """
        Тест полного цикла покупки.

        Параметры:
        browser (webdriver): экземпляр браузера

        Возвращаемое значение:
        None
        """
        with allure.step("1. Открытие страницы авторизации"):
            login_page = LoginPage(browser)
            login_page.open()

        with allure.step("2. Выполнение входа в систему"):
            login_page.login("standard_user", "secret_sauce")

        with allure.step("3. Проверка загрузки страницы товаров"):
            inventory_page = InventoryPage(browser)
            assert inventory_page.is_loaded(), " +"
            "Страница товаров не загрузилась"

        with allure.step("4. Добавление товаров в корзину"):
            items_to_add = [
                "Sauce Labs Backpack",
                "Sauce Labs Bolt T-Shirt",
                "Sauce Labs Onesie"
            ]
            for item in items_to_add:
                inventory_page.add_item_to_cart(item)

        with allure.step("5. Переход в корзину"):
            inventory_page.go_to_cart()

        with allure.step("6. Переход к оформлению заказа"):
            cart_page = CartPage(browser)
            cart_page.proceed_to_checkout()

        with allure.step("7. Заполнение информации о покупателе"):
            checkout_info_page = CheckoutInfoPage(browser)
            checkout_info_page.fill_info("Сюзанна", "Савинова", "658060")

        with allure.step("8. Получение итоговой суммы заказа"):
            checkout_overview_page = CheckoutOverviewPage(browser)
            total_amount = checkout_overview_page.get_total_amount()

        with allure.step("9. Проверка итоговой суммы заказа"):
            expected_amount = 58.29
        assert total_amount == expected_amount, (
            f"Ожидаемая сумма: ${expected_amount}, "
            f"фактическая: ${total_amount}"
            )
