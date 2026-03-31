from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username: str, password: str):
        username_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        username_field.send_keys(username)

        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(password)

        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_loaded(self) -> bool:
        return self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
        ) is not None

    def add_item_to_cart(self, item_name: str):
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
        cart_link = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        )
        cart_link.click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def proceed_to_checkout(self):
        checkout_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_button.click()


class CheckoutInfoPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_info(self, first_name: str, last_name: str, postal_code: str):
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
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_total_amount(self) -> float:
        total_element = self.wait.until(
         EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        total_text = total_element.text
        return float(total_text.split("$")[1])
