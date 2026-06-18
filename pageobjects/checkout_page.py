from selenium.webdriver.common.by import By

class CheckoutPage():
  def __init__(self,driver):
    self.driver = driver 
    self.firstname_locator = (By.CSS_SELECTOR,"#first-name")
    self.lastname_locator = (By.CSS_SELECTOR,"#last-name")
    self.postalcode_locator = (By.CSS_SELECTOR,"#postal-code")
    self.continue_button_locator = (By.CSS_SELECTOR,"#continue")
    self.page_header_locator = (By.CSS_SELECTOR,".title")
    self.cancel_button_locator = (By.CSS_SELECTOR,"#cancel")
    
  def get_page_header(self):
    return self.driver.find_element(*self.page_header_locator).text
  
  def get_page_title(self):
    return self.driver.title
  
  def is_continue_button_available(self):
    return self.driver.find_element(*self.continue_button_locator).is_enabled()
  
  def is_cancel_button_available(self):
    return self.driver.find_element(*self.cancel_button_locator).is_enabled()
  
  def enter_user_details(self,firstname,lastname,pincode):
    self.driver.find_element(*self.firstname_locator).send_keys(firstname)
    self.driver.find_element(*self.lastname_locator).send_keys(lastname)
    self.driver.find_element(*self.postalcode_locator).send_keys(pincode)
    self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
    self.driver.find_element(*self.continue_button_locator).click()
  
  def click_continue_button(self):
    self.driver.find_element(*self.continue_button_locator).click()