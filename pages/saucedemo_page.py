from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import FirefoxDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class SaucedemoPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_saucedemo_page(self):
        self.driver.get("https://saucedemo.com")

    def perform_saucedemo(self):
        username_field = self.wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
        username_field.clear()
        username_field.send_keys("standard_user")

        password_field = self.driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys("secret_sauce")

        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))

        # Добавляем товар (Sauce Labs Backpack)
        product_locator = (By.ID, "item_4_title_link")
        product_element = self.wait.until(EC.element_to_be_clickable(product_locator))
        product_element.click()

        cart_icon = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_container")))
        return cart_icon.text

@pytest.fixture
def driver():
    service = Service(FirefoxDriverManager().install())
    driver = webdriver.Firefox(service=service)
    yield driver
    driver.quit()

def test_change_calculator(driver):
    saucedemo = SaucedemoPage(driver)
    saucedemo.open_saucedemo_page()
    result = saucedemo.perform_saucedemo()
    assert "1" in result
