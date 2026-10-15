import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.calculator_page import CalculatorPage

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_change_calculator(driver):
    calculator = CalculatorPage(driver)
    
    calculator.open_calculator_page()
    
    result = calculator.perform_calculation()
    
    assert result == "15", f"Ожидалось 15, но получилось: {result}"
