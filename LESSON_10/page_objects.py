from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """
    Класс, представляющий страницу авторизации.
    Содержит методы для открытия страницы и входа в систему.
    """

    def __init__(self, driver):
        """
        Инициализирует объект страницы авторизации.

        Параметры:
        driver (webdriver): экземпляр WebDriver для управления браузером
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """
        Открывает страницу авторизации.

        Возвращаемое значение:
        None
        """
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username: str, password: str):
        """
        Выполняет вход в систему с указанными учётными данными.

        Параметры:
        username (str): имя пользователя
        password (str): пароль пользователя

        Возвращаемое значение:
        None

        Исключения:
        TimeoutException: " +
        "если поле имени пользователя не найдено в течение 10 секунд"
        NoSuchElementException: " +
        "если другие элементы (пароль, кнопка) не найдены"
        """
        username_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        username_field.send_keys(username)

        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(password)

        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()


class InventoryPage:
    """
    Класс, представляющий страницу товаров.
    Содержит методы для проверки загрузки страницы, " +
    "добавления товаров в корзину и перехода в корзину."
    """

    def __init__(self, driver):
        """
        Инициализирует объект страницы товаров.

        Параметры:
        driver (webdriver): экземпляр WebDriver для управления браузером
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_loaded(self) -> bool:
        """
        Проверяет, загрузилась ли страница товаров.

        Возвращаемое значение:
        bool: True, если страница загрузилась, False — иначе

        Исключения:
        TimeoutException: " +
        "если элемент списка товаров не найден в течение 10 секунд"
        """
        return self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
        ) is not None

    def add_item_to_cart(self, item_name: str):
        """
        Добавляет указанный товар в корзину.

        Параметры:
        item_name (str): название товара

        Возвращаемое значение:
        None

        Исключения:
        TimeoutException: если контейнер товара не найден в течение 10 секунд
        NoSuchElementException: если кнопка добавления не найдена
        """
        item_container = self.wait.until(
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

    def go_to_cart(self):
        """
        Переходит на страницу корзины.

        Возвращаемое значение:
        None

        Исключения:
        TimeoutException: " +
        "если ссылка на корзину не кликабельна в течение 10 секунд"
        """
        cart_link = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        )
        cart_link.click()


class CartPage:
    """
    Класс, представляющий страницу корзины.
    Содержит метод для перехода к оформлению заказа.
    """

    def __init__(self, driver):
        """
        Инициализирует объект страницы корзины.

        Параметры:
        driver (webdriver): экземпляр WebDriver для управления браузером
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def proceed_to_checkout(self):
        """
        Переходит к оформлению заказа (страница ввода данных).

        Возвращаемое значение:
        None

        Исключения:
        TimeoutException: " +
        "если кнопка оформления заказа не кликабельна в течение 10 секунд"
        """
        checkout_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_button.click()


class CheckoutInfoPage:
    """
    Класс, представляющий страницу ввода данных для оформления заказа.
    Содержит метод для заполнения информации о покупателе.
    """

    def __init__(self, driver):
        """
        Инициализирует объект страницы ввода данных.

        Параметры:
        driver (webdriver): экземпляр WebDriver для управления браузером
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_info(self, first_name: str, last_name: str, postal_code: str):
        """
        Заполняет поля с информацией о покупателе.

        Параметры:
        first_name (str): имя покупателя
        last_name (str): фамилия покупателя
        postal_code (str): почтовый индекс

        Возвращаемое значение:
        None

        Исключения:
        TimeoutException: если поле имени не найдено в течение 10 секунд
        NoSuchElementException: если другие поля или кнопка не найдены
        """
        first_name_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        first_name_field.send_keys(first_name)

        last_name_field = self.driver.find_element(By.ID, "last-name")
        last_name_field.send_keys(last_name)

        postal_code_field = self.driver.find_element(By.ID, "postal-code")
        postal_code_field.send_keys(postal_code)

        continue_button = self.driver.find_element(By.ID, "continue")
        continue_button.click()


class CheckoutOverviewPage:
    """
    Класс, представляющий страницу подтверждения заказа.
    Содержит метод для получения итоговой суммы заказа.
    """

    def __init__(self, driver):
        """
        Инициализирует объект страницы подтверждения заказа.

        Параметры:
        driver (webdriver): экземпляр WebDriver для управления браузером
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_total_amount(self) -> float:
        """
        Получает итоговую сумму заказа.

        Возвращаемое значение:
        float: итоговая сумма заказа

        Исключения:
        TimeoutException: если элемент с суммой не найден в течение 10 секунд
        ValueError: если текст суммы не может быть преобразован в float
        """
        total_element = self.wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
                )
        )
        total_text = total_element.text
        return float(total_text.split("$")[1])
