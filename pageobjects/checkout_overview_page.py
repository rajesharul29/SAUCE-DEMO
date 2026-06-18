from selenium.webdriver.common.by import By

class CheckoutOveriew:
  def __init__(self,driver):
    self.driver  = driver
    self.page_header_locator = (By.CSS_SELECTOR,".app_logo")
    self.finish_button_locator = (By.CSS_SELECTOR,"#finish")
    
  def get_page_header(self):
    return self.driver.find_element(*self.page_header_locator).text
  
  def get_page_title(self):
    return self.driver.title
  
  def get_order_summary(self):
    pass
  
  def get_payment_info(self):
    pass
  
  def get_shipping_info(self):
    pass
  
  def get_price_total(self):
    pass
  
  def complete_checkout(self):
    self.driver.find_element(*self.finish_button_locator).click()
  