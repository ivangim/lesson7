import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import FirefoxDriverManager
from pages.saucedemo_page import SaucedemoPage

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