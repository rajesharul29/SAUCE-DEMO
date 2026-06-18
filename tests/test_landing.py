from pageobjects.login_page import LoginPage

def test_landing(browser):
  driver  = browser
  
  landing_page = LoginPage(driver)
  
  header_text = landing_page.landing()
  assert header_text == "Swag Labs"
  
  assert driver.current_url == "https://www.saucedemo.com/"
  
  
  login_form = LoginPage(driver)
  assert login_form.username_placeholder() == "Username"
  assert login_form.password_placeholder() == "Password"
  assert login_form.login_button() == "Login"
  
  
  
