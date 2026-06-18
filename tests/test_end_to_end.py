from pageobjects.Checkout_complete_page import CheckoutComplete
from pageobjects.checkout_overview_page import CheckoutOveriew
from pageobjects.checkout_page import CheckoutPage
from pageobjects.login_page import LoginPage
from pageobjects.inventory_page import InventoryPage
from pageobjects.cart_page import CartPage
import pytest

@pytest.mark.usefixtures("browser","data_load")
class TestE2E:
  def test_end_to_end(self,browser,data_load):
    driver = browser
    
    login = LoginPage(driver)
    login.login(data_load[0],data_load[1])
    
    inventory_page = InventoryPage(driver)
    inventory_page.add_all_products_to_cart()
    your_cart_url = inventory_page.click_cart_logo()
    assert your_cart_url == "https://www.saucedemo.com/cart.html"
    
    cart_page=CartPage(driver)
    
    # this assert passes only if list contains products fails if no products are in list
    assert cart_page.get_cart_item_count() == cart_page.all_products_available_cart() 
    expected_product_list = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt","Sauce Labs Fleece Jacket", "Sauce Labs Onesie", "Test.allTheThings() T-Shirt (Red)"]
    assert cart_page.get_product_names_from_list() == expected_product_list
    cart_page.click_checkout_button()
    
    checkout = CheckoutPage(driver)
    checkout.enter_user_details("Arul", "Rajeesh", "123456")
    assert driver.current_url == "https://www.saucedemo.com/checkout-step-two.html"
    
    checkout_overview = CheckoutOveriew(driver)
    checkout_overview.complete_checkout()
    assert driver.current_url == "https://www.saucedemo.com/checkout-complete.html"
    
    checkout_complete = CheckoutComplete(driver)
    assert checkout_complete.get_order_message() == "Your order has been dispatched, and will arrive just as fast as the pony can get there!"

    
    

