from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.browserutils import BrowserUtils

class YourCartPage(BrowserUtils):
  def __init__(self,driver):
    super().__init__(driver)
    self.driver=driver
    self.page_header_locator = (By.CSS_SELECTOR,".title")
    self.continue_shopping_button_locator = (By.CSS_SELECTOR,"#continue-shopping")
    self.checkout_button_locator = (By.CSS_SELECTOR,"#checkout")
    self.products_in_cart = (By.CSS_SELECTOR,"div [class='cart_item']")
    self.cart_count = (By.XPATH,"//span[@class='shopping_cart_badge']")
    self.in_cart_items = (By.XPATH,"//div[@class='cart_item']")
    self.remove_button_list = (By.XPATH,"//div[@class='item_pricebar']/button")
    
  def get_page_header(self):
    return self.driver.find_element(*self.page_header_locator).text
  
  def get_page_title(self):
    return self.get_title()
    
  
  def is_continue_shopping_button_available(self):
    self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
    return self.wait_for_visible(self.continue_shopping_button_locator).is_displayed()
  
  def is_checkout_button_enabled(self):
    self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
    return self.wait_for_visible(self.checkout_button_locator).is_displayed()
  
  def all_products_available_cart(self):
    return len(self.wait_for_all_present(self.products_in_cart))
  
  def get_cart_item_count(self):
    return int(self.driver.find_element(*self.cart_count).text)
  
  def click_checkout_button(self):
    self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
    self.driver.find_element(*self.checkout_button_locator).click()
    
  def get_product_names_from_your_cart_page(self):
    self.wait_for_all_present(self.products_in_cart)
    cart_items = self.driver.find_elements(*self.products_in_cart)
    products_list = []
    for item in cart_items:
      product = item.find_element(By.CSS_SELECTOR,".inventory_item_name").text
      products_list.append(product)
    return products_list
  
  def get_remove_buttons_count(self):
    return len(self.wait_for_all_present(self.remove_button_list))
    
  
  def remove_first_cart_item(self):
    buttons_list = self.wait_for_all_present(self.remove_button_list)
    buttons_list[0].click()
    
    
  
    