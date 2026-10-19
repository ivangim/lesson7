from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class SaucedemoPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_saucedemo_page(self):
        self.driver.get("https://www.saucedemo.com")
        return self

    def enter_username(self, username):
        field = self.wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
        field.clear()
        field.send_keys(username)
        return self

    def enter_password(self, password):
        field = self.wait.until(EC.visibility_of_element_located((By.ID, "password")))
        field.clear()
        field.send_keys(password)
        return self

    def click_login(self):
        btn = self.wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
        btn.click()
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
        return self

    def add_product_by_id(self, product_id):
        locator = (By.ID, product_id)
        remove_locator = (By.ID, f"remove-{product_id.replace('add-to-cart-', '')}")

        btn = self.wait.until(EC.element_to_be_clickable(locator))
        btn.click()

        try:
            self.wait.until(
                EC.visibility_of_element_located(remove_locator)
            )
        except Exception as e:
            self.driver.save_screenshot("failed_add_to_cart.png")
            raise e
            
        return self

    def go_to_cart(self):
        cart_icon = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
        cart_icon.click()
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart_item")))
        return self

    def click_checkout(self):
        checkout_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_btn.click()
        return self

    def fill_checkout_form(self, first_name, last_name, postal_code):
        fname_field = self.wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
        lname_field = self.driver.find_element(By.ID, "last-name")
        pcode_field = self.driver.find_element(By.ID, "postal-code")
        
        fname_field.clear()
        fname_field.send_keys(first_name)
        
        lname_field.clear()
        lname_field.send_keys(last_name)
        
        pcode_field.clear()
        pcode_field.send_keys(postal_code)
        return self

    def click_continue(self):
        cont_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "continue")))
        cont_btn.click()
        return self

    def get_total_price(self) -> str:
        total_elem = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label")))
        text = total_elem.text
        return text.replace("Total: $", "").strip()
