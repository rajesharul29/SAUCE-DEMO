from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utils.browserutils import BrowserUtils

class InventoryPage(BrowserUtils):
  def __init__(self,driver):
    super().__init__(driver)
    self.driver=driver
    self.filter_locator=(By.CSS_SELECTOR,"select[data-test='product-sort-container']")
    self.cart_logo_locator = (By.CSS_SELECTOR,".shopping_cart_link")
    self.slidebar_logo_locator = (By.CSS_SELECTOR,"#react-burger-menu-btn")
    self.page_header_locator = (By.CSS_SELECTOR,".title")
    self.add_to_cart_buttons_locator = (By.XPATH,"//div[@class = 'inventory_list']/div/div/div[2]/button")
    self.cart_count = (By.XPATH,"//span[@class='shopping_cart_badge']")
    self.price_of_listed_products_locator = (By.XPATH,"//div[@class='inventory_item_price']")
    
  def get_page_header(self):
    return self.driver.find_element(*self.page_header_locator).text
  
  # def get_page_title(self):
  #   return self.driver.title
  
  def is_filter_available(self):
    return self.driver.find_element(*self.filter_locator).is_displayed()
  
  def is_cart_logo_available(self):
    return self.driver.find_element(*self.cart_logo_locator).is_displayed()
  
  def is_slidebar_available(self):
    return self.driver.find_element(*self.slidebar_logo_locator).is_displayed()
  
  def add_all_products_to_cart(self):
    buttons = self.driver.find_elements(*self.add_to_cart_buttons_locator)
    for button in range(len(buttons)):
      buttons[button].click()
    return self.driver.find_element(*self.cart_count).text
  
  def sort_products_accending_by_price(self):
    options=Select(self.driver.find_element(*self.filter_locator))
    options.select_by_index(2)
    price_elements = self.driver.find_elements(*self.price_of_listed_products_locator)
    
    actual_prices =[]
    for price in price_elements:
      actual_prices.append(float(price.text.replace("$","")))
      
    expected_prices = sorted(actual_prices)
    return actual_prices == expected_prices
  
  def click_cart_logo(self):
    self.driver.execute_script("window.scrollBy(0,-700);")
    self.driver.find_element(*self.cart_logo_locator).click()
    return self.driver.current_url
    
    