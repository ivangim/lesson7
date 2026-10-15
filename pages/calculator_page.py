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
        self.wait = WebDriverWait(driver, 20)

    def open_calculator_page(self):
        url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        self.driver.get(url)

    def wait_for_result(self, expected_text):
        self.wait.until(
            EC.text_to_be_present_in_element(self.SCREEN_ELEMENT, expected_text)
        )
        
        screen_element = self.driver.find_element(*self.SCREEN_ELEMENT)
        return screen_element.text

    def perform_calculation(self):
        try:
            delay_input = self.driver.find_element(*self.DELAY_INPUT)
            delay_input.clear()
            delay_input.send_keys("1")  # 1 секунда задержки
        except Exception:
            pass  # Если поля нет, просто идём дальше

        self.driver.find_element(*self.BUTTON_7).click()
        self.driver.find_element(*self.BUTTON_PLUS).click()
        self.driver.find_element(*self.BUTTON_8).click()
        self.driver.find_element(*self.BUTTON_EQUALS).click()

        result_text = self.wait_for_result("15")
        return result_text

