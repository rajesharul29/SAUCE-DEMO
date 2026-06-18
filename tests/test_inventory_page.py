from pageobjects.inventory_page import InventoryPage
from pageobjects.login_page import LoginPage
import json, pytest

test_data_path = "data/test_login.json"
with open(test_data_path) as f:
  test_data=json.load(f)
  test_list = test_data["valid_login_credentials"]

def test_inventory_page_loaded_successfully(browser):
  driver=browser
  
  swag_labs_login = LoginPage(driver)
  swag_labs_login.login("standard_user","secret_sauce")
  assert driver.current_url == "https://www.saucedemo.com/inventory.html"
  
  inventory_page = InventoryPage(driver)
  assert inventory_page.get_title() == "Swag Labs"
  assert inventory_page.get_page_header() == "Products"
  assert inventory_page.is_cart_logo_available()
  assert inventory_page.is_filter_available()
  assert inventory_page.is_slidebar_available()
  

@pytest.mark.parametrize("test_list_item", test_list)
def test_add_products_to_cart(browser,test_list_item):
  driver=browser
  swag_labs_login = LoginPage(driver)
  swag_labs_login.login(test_list_item["user_name"], test_list_item["password"])
  
  add_products_to_cart = InventoryPage(driver)
  
  assert add_products_to_cart.add_all_products_to_cart() == "6"
  
@pytest.mark.parametrize("test_list_item", test_list)  
def test_sort_products_by_price(browser,test_list_item):
  driver = browser
  swag_labs_login = LoginPage(driver)
  swag_labs_login.login(test_list_item["user_name"],test_list_item["password"])
  
  sort = InventoryPage(driver)
  assert sort.sort_products_accending_by_price()
  
