from selenium.webdriver.common.by import By
from utils.browserutils import BrowserUtils
class CheckoutComplete(BrowserUtils):
  def __init__(self,driver):
    super().__init__(driver)
    self.driver = driver
    self.order_message = (By.CSS_SELECTOR,".complete-text")
  
  def get_page_header(browser):
    driver=browser
    self.driver
    
  def get_current_url(self):
    pass
  
  def get_order_message(self):
    return self.driver.find_element(*self.order_message).text
  
  def is_back_home_button_enabled(self):
    pass
  