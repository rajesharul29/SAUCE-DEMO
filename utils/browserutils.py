from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BrowserUtils:
  def __init__(self, driver, timeout=10):
    self.driver = driver
    self.wait = WebDriverWait(driver, timeout)

  def get_title(self):
    return self.driver.title

  # ── Explicit wait helpers ─────────────────────────────────────────────────

  def wait_for_visible(self, locator):
    """Wait until element is visible, return it.
       I need to read text /attribute"""
    return self.wait.until(EC.visibility_of_element_located(locator))

  def wait_for_clickable(self, locator):
    """Wait until element is visible AND enabled, return it."""
    """i need t0 click/type into it"""
    return self.wait.until(EC.element_to_be_clickable(locator))

  def wait_for_present(self, locator):
    """Wait until element exists in DOM (may be invisible), return it."""
    """i just need to check if element is there, e.g. a checkbox, a dropdown, a table"""
    return self.wait.until(EC.presence_of_element_located(locator))

  def wait_for_all_present(self, locator):
    """Wait until at least one element matching locator is in DOM, return list."""
    """iam itereting over list of elements, e.g. table rows, dropdown options"""
    return self.wait.until(EC.presence_of_all_elements_located(locator))

  def wait_for_invisible(self, locator):
    """Wait until element disappears (e.g. a loading spinner)."""
    return self.wait.until(EC.invisibility_of_element_located(locator))

  def wait_for_url_contains(self, partial_url):
    """Wait until the current URL contains the given string."""
    """I want to verify that we navigated to the correct page, e.g. after login or clicking a link"""
    self.wait.until(EC.url_contains(partial_url))

  def wait_for_text_in_element(self, locator, text):
    """Wait until element contains specific text."""
    return self.wait.until(EC.text_to_be_present_in_element(locator, text))