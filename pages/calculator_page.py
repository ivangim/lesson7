from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    BUTTON_7 = (By.XPATH, "//span[contains(text(), '7')]")
    BUTTON_PLUS = (By.XPATH, "//span[contains(text(), '+')]")
    BUTTON_8 = (By.XPATH, "//span[contains(text(), '8')]")
    BUTTON_EQUALS = (By.XPATH, "//span[contains(text(), '=')]")
    SCREEN_ELEMENT = (By.CLASS_NAME, "screen")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 45)

    def open(self, url="https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"):
        self.driver.get(url)

    def set_delay(self, seconds: int):
        element = self.wait.until(EC.element_to_be_clickable(self.DELAY_INPUT))
        element.clear()
        element.send_keys(str(seconds))

    def click_7(self):
        element = self.wait.until(EC.element_to_be_clickable(self.BUTTON_7))
        element.click()

    def click_plus(self):
        element = self.wait.until(EC.element_to_be_clickable(self.BUTTON_PLUS))
        element.click()

    def click_8(self):
        element = self.wait.until(EC.element_to_be_clickable(self.BUTTON_8))
        element.click()

    def click_equals(self):
        element = self.wait.until(EC.element_to_be_clickable(self.BUTTON_EQUALS))
        element.click()

    def wait_for_result(self, expected_text: str):
        self.wait.until(
            EC.text_to_be_present_in_element(self.SCREEN_ELEMENT, expected_text)
        )
        return self.driver.find_element(*self.SCREEN_ELEMENT).text

    def perform_calculation_7_plus_8(self, delay_seconds: int = 1):
        self.set_delay(delay_seconds)
        self.click_7()
        self.click_plus()
        self.click_8()
        self.click_equals()
        return self.wait_for_result("15")
