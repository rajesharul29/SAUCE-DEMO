from selenium.webdriver.common.by import By
from utils.browserutils import BrowserUtils

class CheckoutOveriew(BrowserUtils):
  def __init__(self,driver):
    self.driver  = driver
    self.page_header_locator = (By.CSS_SELECTOR,".app_logo")
    self.finish_button_locator = (By.CSS_SELECTOR,"#finish")
    self.list_of_products = (By.XPATH,"//div[@class = 'cart_item']")
    self.badge_text_locator = (By.XPATH,"//span[@class='shopping_cart_badge']")
    self.product_names_list = (By.XPATH,"//div[@class = 'inventory_item_name']")
    self.product_prices_list = (By.XPATH,"//div[@class = 'inventory_item_price']")
    self.tax_locator = (By.XPATH,"//div[@class = 'summary_tax_label']")
    
  def get_page_header(self):
    return self.wait_for_visible(self.page_header_locator).text
  
  def get_page_title(self):
    return self.get_page_title()
  
  def get_count_of_products_in_cart(self):
    list= self.wait_for_all_present(self.list_of_products)
    return len(list)
  
  def get_count_from_cart_icon(self):
    badge_text = self.wait_for_text_in_element(self.badge_text_locator)
    return badge_text
  
  def get_list_of_product_names_from_checkout_overview_page(self):
    products_names=[]
    product_name_elements=self.wait_for_all_present(self.product_names_list)
    for element in product_name_elements:
      products_names.append(element.text)
    return products_names
  
  def get_sumof_prices(self):
    list_of_prices = []
    sumof_prices=0
    product_price_elements = self.wait_for_all_present(self.product_prices_list)
    for element in product_price_elements:
      list_of_prices.append(element.text)
    for i in list_of_prices:
      sumof_prices=sumof_prices+float(i[1:])
    return sumof_prices
      
  
  def get_tax(self):
    full_text=self.wait_for_visible(self.tax_locator).text
    tax=float(full_text[6:])
    return tax
    
  def get_payment_info(self):
    pass
  
  def get_shipping_info(self):
    pass
  
  def get_price_total(self):
    pass
  
  def complete_checkout(self):
    self.driver.find_element(*self.finish_button_locator).click()
    

  