import pytest
from pageobjects.login_page import LoginPage
from pageobjects.inventory_page import InventoryPage
from pageobjects.yourcart_page import YourCartPage


@pytest.fixture
def logged_in_cart(browser):
    """Factory fixture: login and navigate to cart. Call with (username, password)."""
    def _navigate(username, password):
        LoginPage(browser).login(username, password)
        InventoryPage(browser).click_cart_logo()
        return YourCartPage(browser)
    return _navigate


@pytest.fixture
def logged_in_cart_with_all_products(browser):
    """Factory fixture: login, add all products, navigate to cart. Call with (username, password)."""
    def _navigate(username, password):
        LoginPage(browser).login(username, password)
        inv = InventoryPage(browser)
        inv.add_all_products_to_cart()
        inv.click_cart_logo()
        return YourCartPage(browser)
    return _navigate
