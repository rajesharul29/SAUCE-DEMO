from selenium.webdriver.common.by import By
from utils.browserutils import BrowserUtils


class LoginPage(BrowserUtils):
  def __init__(self, driver):
    super().__init__(driver)
    self.driver = driver
    self.user_name = (By.XPATH, "//input[@id='user-name']")
    self.user_password = (By.XPATH, "//input[@id='password']")
    self.login_button_locator = (By.XPATH, "//input[@id='login-button']")
    self.page_header = (By.CLASS_NAME, "login_logo")
    self.error_message_locator = (By.XPATH, "//form/div[3]")

  def landing(self):
    return self.wait_for_visible(self.page_header).text

  def login(self, user_name, user_password):
    self.wait_for_clickable(self.user_name).send_keys(user_name)
    self.wait_for_clickable(self.user_password).send_keys(user_password)
    self.wait_for_clickable(self.login_button_locator).click()
    # After login, wait for URL to move away from the login page
    self.wait_for_url_contains("inventory")

  def username_placeholder(self):
    return self.wait_for_visible(self.user_name).get_attribute("placeholder")

  def password_placeholder(self):
    return self.wait_for_visible(self.user_password).get_attribute("placeholder")

  def login_button(self):
    return self.wait_for_visible(self.login_button_locator).get_attribute("value")

  def invalid_login(self, user_name, user_password):
    self.wait_for_clickable(self.user_name).send_keys(user_name)
    self.wait_for_clickable(self.user_password).send_keys(user_password)
    self.wait_for_clickable(self.login_button_locator).click()
    # Error message is injected into DOM after failed login — wait for it
    return self.wait_for_visible(self.error_message_locator).text
    
    