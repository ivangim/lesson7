import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.calculator_page import CalculatorPage

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_calculator_7_plus_8_equals_15(driver):
    page = CalculatorPage(driver)
    page.open() 
    result = page.perform_calculation_7_plus_8(delay_seconds=1)
    assert result == "15"