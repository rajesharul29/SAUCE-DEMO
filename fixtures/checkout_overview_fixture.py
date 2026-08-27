import pytest
from pageobjects.login_page import LoginPage
from pageobjects.inventory_page import InventoryPage
from pageobjects.yourcart_page import YourCartPage
from pageobjects.checkout_your_infopage import CheckoutYourInfo
from pageobjects.checkout_overview_page import CheckoutOveriew

@pytest.fixture
def navigate_to_checkout_overview_page(browser):
    def _navigate(username, password, firstname, lastname, postalcode):
        LoginPage(browser).login(username,password)
        inv = InventoryPage(browser)
        inv.add_all_products_to_cart()
        inv.click_cart_logo()
        YourCart=YourCartPage(browser)
        YourCart.click_checkout_button()
        user_details=CheckoutYourInfo(browser)
        user_details.enter_user_details(firstname,lastname,postalcode)
        return CheckoutOveriew(browser)
    return _navigate
        
        