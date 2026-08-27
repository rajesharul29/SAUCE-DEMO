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
    # Wait for page header to be visible before reading its text
    return self.wait_for_visible(self.page_header_locator).text

  def is_filter_available(self):
    return self.wait_for_visible(self.filter_locator).is_displayed()

  def is_cart_logo_available(self):
    return self.wait_for_visible(self.cart_logo_locator).is_displayed()

  def is_slidebar_available(self):
    return self.wait_for_visible(self.slidebar_logo_locator).is_displayed()

  def add_all_products_to_cart(self):
    # Wait for all buttons to be in DOM before iterating
    buttons = self.wait_for_all_present(self.add_to_cart_buttons_locator)
    for button in buttons:
      # Each click updates the DOM — wait for each button to be clickable
      self.wait_for_clickable(self.add_to_cart_buttons_locator)
      button.click()
    # Cart badge appears after first item is added — wait for it
    return self.wait_for_visible(self.cart_count).text

  def sort_products_accending_by_price(self):
    # Wait for filter to be interactable before using Select
    options = Select(self.wait_for_clickable(self.filter_locator))
    options.select_by_index(2)
    # After sort, wait for price list to re-render
    price_elements = self.wait_for_all_present(self.price_of_listed_products_locator)
    actual_prices = [float(p.text.replace("$", "")) for p in price_elements]
    return actual_prices == sorted(actual_prices)

  def click_cart_logo(self):
    self.driver.execute_script("window.scrollBy(0,-700);")
    # Wait for cart logo to be clickable before clicking
    self.wait_for_clickable(self.cart_logo_locator).click()
    # Wait for URL to transition to cart page
    self.wait_for_url_contains("cart")
    return self.driver.current_url
    
    