from selenium.webdriver.common.by import By

class CheckoutComplete():
  def __init__(self,driver):
    self.driver = driver
    self.order_message = (By.CSS_SELECTOR,".complete-text")
  
  def get_page_header(self):
    self
    
  def get_current_url(self):
    pass
  
  def get_order_message(self):
    return self.driver.find_element(*self.order_message).text
  
  def is_back_home_button_enabled(self):
    pass
  