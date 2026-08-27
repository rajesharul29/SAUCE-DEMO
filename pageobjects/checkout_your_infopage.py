from selenium.webdriver.common.by import By
from utils.browserutils import BrowserUtils

class CheckoutYourInfo(BrowserUtils):
  def __init__(self,driver):
    super().__init__(driver)
    self.driver = driver 
    self.firstname_locator = (By.CSS_SELECTOR,"#first-name")
    self.lastname_locator = (By.CSS_SELECTOR,"#last-name")
    self.postalcode_locator = (By.CSS_SELECTOR,"#postal-code")
    self.continue_button_locator = (By.CSS_SELECTOR,"#continue")
    self.page_header_locator = (By.CSS_SELECTOR,".title")
    self.cancel_button_locator = (By.CSS_SELECTOR,"#cancel")
    self.error_message_locator = (By.CSS_SELECTOR,"[data-test='error']")

  def get_page_header(self):
    return self.wait_for_visible(self.page_header_locator).text
  
  def get_page_title(self):
    return self.get_title()
  
  def is_continue_button_available(self):
    return self.wait_for_visible(self.continue_button_locator).is_enabled()
  
  def is_cancel_button_available(self):
    return self.wait_for_visible(self.cancel_button_locator).is_enabled()
  
  def enter_user_details(self,firstname,lastname,pincode):
    self.fill_user_details(firstname,lastname,pincode)
    self.click_continue_button()

  def fill_user_details(self,firstname,lastname,pincode):
    self.wait_for_clickable(self.firstname_locator).send_keys(firstname)
    self.wait_for_clickable(self.lastname_locator).send_keys(lastname)
    self.wait_for_clickable(self.postalcode_locator).send_keys(pincode)

  def get_error_message(self):
    return self.wait_for_visible(self.error_message_locator).text

  def click_continue_button(self):
    self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
    self.wait_for_clickable(self.continue_button_locator).click()
    
  def click_cancel_button(self):
    self.wait_for_clickable(self.cancel_button_locator).click()
    
  def verify_placeholder_text(self):
    first_name_placeholder = self.wait_for_visible(self.firstname_locator).get_attribute("placeholder")
    last_name_placeholder = self.wait_for_visible(self.lastname_locator).get_attribute("placeholder")
    postalcode_placeholder = self.wait_for_visible(self.postalcode_locator).get_attribute("placeholder")
    return [first_name_placeholder, last_name_placeholder, postalcode_placeholder]