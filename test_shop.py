import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from pages.saucedemo_page import SaucedemoPage

def test_shop_checkout_flow():
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    
    try:
        page = SaucedemoPage(driver)

        page.open_saucedemo_page()

        page.enter_username("standard_user") \
            .enter_password("secret_sauce") \
            .click_login()

        # ШАГ 3: Добавьте в корзину товары
        # Sauce Labs Backpack
        page.add_product_by_id("add-to-cart-sauce-labs-backpack")
        # Sauce Labs Bolt T-Shirt
        page.add_product_by_id("add-to-cart-sauce-labs-bolt-t-shirt")
        # Sauce Labs Onesie
        page.add_product_by_id("add-to-cart-sauce-labs-onesie")

        page.go_to_cart()

        page.click_checkout()

        page.fill_checkout_form("Иван", "Петров", "123456")

        page.click_continue()

        total = page.get_total_price()
        expected = "58.29"
        
        assert total == expected, f"Ошибка: ожидалось {expected}, но было {total}"
        
        print(f"✅ Тест пройден! Итоговая сумма: ${total}")

    except Exception as e:
        driver.save_screenshot("test_03_shop_error.png")
        print(f"❌ Тест упал: {e}")
        raise
    finally:
        driver.quit()


