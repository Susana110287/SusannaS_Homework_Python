import pytest
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
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_purchase_flow(browser):
    # 1. Страница авторизации
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # 2. Страница товаров
    inventory_page = InventoryPage(browser)
    assert inventory_page.is_loaded()

    items_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]
    for item in items_to_add:
        inventory_page.add_item_to_cart(item)

    inventory_page.go_to_cart()

    # 3. Страница корзины
    cart_page = CartPage(browser)
    cart_page.proceed_to_checkout()

    # 4. Страница заполнения данных
    checkout_info_page = CheckoutInfoPage(browser)
    checkout_info_page.fill_info("Сюзанна", "Савинова", "658060")

    # 5. Страница подтверждения заказа
    checkout_overview_page = CheckoutOverviewPage(browser)
    total_amount = checkout_overview_page.get_total_amount()

    assert total_amount == 58.29, (
        f"Ожидаемая сумма $58.29, но получено ${total_amount}"
    )
