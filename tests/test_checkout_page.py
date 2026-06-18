from pageobjects.checkout_page import CheckoutPage
from pageobjects.login_page import LoginPage
from pageobjects.inventory_page import InventoryPage
from pageobjects.cart_page import CartPage
import pytest
import json


test_data_path = "data/test_login.json"
with open(test_data_path) as f:
    test_data = json.load(f)
    test_item=test_data["valid_login_credentials"]
    
@pytest.mark.parametrize("test_list_item",test_item)
def test_checkout_page_loaded_successfully(browser,test_list_item):
    driver=browser
    login_page = LoginPage(driver)
    login_page.login(test_list_item["user_name"],test_list_item["password"])
    
    inv = InventoryPage(driver)
    inv.add_all_products_to_cart()
    inv.click_cart_logo()
    
    cart_page = CartPage(driver)
    cart_page.all_products_available_cart()
    cart_page.click_checkout_button()
    
    checkout_page = CheckoutPage(driver)
    # checkout_page.enter_user_details("Arul", "Rajeesh", "1234")
    # checkout_page.click_continue_button()
    assert checkout_page.is_continue_button_available()
    
    
    