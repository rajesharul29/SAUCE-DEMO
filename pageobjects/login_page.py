from selenium.webdriver.common.by import By

class LoginPage():
  def __init__(self,driver):
    self.driver=driver
    self.user_name = (By.XPATH,"//input[@id='user-name']")
    self.user_password = (By.XPATH,"//input[@id='password']")
    self.login_button_locator = (By.XPATH,"//input[@id='login-button']")
    self.page_header = (By.CLASS_NAME,"login_logo")
    self.error_message_locator =(By.XPATH,"//form/div[3]")
    
    
  def landing(self):
    return self.driver.find_element(*self.page_header).text
    
  def login(self,user_name,user_password):
    self.driver.find_element(*self.user_name).send_keys(user_name)
    self.driver.find_element(*self.user_password).send_keys(user_password)
    self.driver.find_element(*self.login_button_locator).click()
    
  def username_placeholder(self):
    return self.driver.find_element(*self.user_name).get_attribute("placeholder")
  
  def password_placeholder(self):
    return self.driver.find_element(*self.user_password).get_attribute("placeholder")
  
  def login_button(self):
    return self.driver.find_element(*self.login_button_locator).get_attribute("value")
  
  def invalid_login(self,user_name,user_password):
    self.driver.find_element(*self.user_name).send_keys(user_name)
    self.driver.find_element(*self.user_password).send_keys(user_password)
    self.driver.find_element(*self.login_button_locator).click()
    return self.driver.find_element(*self.error_message_locator).text
    
    