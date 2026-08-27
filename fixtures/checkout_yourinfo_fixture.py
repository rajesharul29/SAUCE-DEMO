import pytest
from pageobjects.login_page import LoginPage
from pageobjects.inventory_page import InventoryPage
from pageobjects.yourcart_page import YourCartPage
from pageobjects.checkout_your_infopage import CheckoutYourInfo


@pytest.fixture
def checkout_your_info_page(browser):
    """Factory fixture: login, add an item to cart, and land on the checkout info page. Call with (username, password)."""
    def _navigate(username, password):
        LoginPage(browser).login(username, password)
        inv = InventoryPage(browser)
        inv.add_all_products_to_cart()
        inv.click_cart_logo()
        YourCartPage(browser).click_checkout_button()
        return CheckoutYourInfo(browser)
    return _navigate
