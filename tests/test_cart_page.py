import pytest
import json

test_data_path = "data/test_login.json"
with open(test_data_path) as f:
    test_data = json.load(f)
    test_item = test_data["valid_login_credentials"]


# Test1
@pytest.mark.parametrize("test_data_item", test_item)
def test_cart_page_loaded_successfully(logged_in_cart_with_all_products, test_data_item):
    cart_page = logged_in_cart_with_all_products(test_data_item["user_name"], test_data_item["password"])
    assert cart_page  # cart URL assertion is inside the fixture


# Test2
@pytest.mark.parametrize("test_data_item", test_item)
def test_cart_page_title(logged_in_cart, test_data_item):
    cart_page = logged_in_cart(test_data_item["user_name"], test_data_item["password"])
    assert cart_page.get_page_title() == "Swag Labs"


# Test3
@pytest.mark.parametrize("test_data_item", test_item)
def test_cart_page_header(logged_in_cart, test_data_item):
    cart_page = logged_in_cart(test_data_item["user_name"], test_data_item["password"])
    assert cart_page.get_page_header() == "Your Cart"


# Test4
@pytest.mark.parametrize("test_data_item", test_item)
def test_checkout_button_enabled(logged_in_cart, test_data_item):
    cart_page = logged_in_cart(test_data_item["user_name"], test_data_item["password"])
    assert cart_page.is_checkout_button_enabled()


# Test5
@pytest.mark.parametrize("test_data_item", test_item)
def test_continue_shopping_button_enabled(logged_in_cart, test_data_item):
    cart_page = logged_in_cart(test_data_item["user_name"], test_data_item["password"])
    assert cart_page.is_continue_shopping_button_available()


# Test6
@pytest.mark.parametrize("test_data_item", test_item)
def test_remove_button_displayed(logged_in_cart_with_all_products, test_data_item):
    cart_page = logged_in_cart_with_all_products(test_data_item["user_name"], test_data_item["password"])
    assert cart_page.get_remove_buttons_count() == cart_page.get_cart_item_count()


# Test7
@pytest.mark.parametrize("test_data_item", test_item)
def test_remove_first_cart_item(logged_in_cart_with_all_products, test_data_item):
    cart_page = logged_in_cart_with_all_products(test_data_item["user_name"], test_data_item["password"])
    initial_cart_count = cart_page.get_cart_item_count()
    cart_page.remove_first_cart_item()
    assert cart_page.get_cart_item_count() == initial_cart_count - 1


# Test8
@pytest.mark.parametrize("test_data_item", test_item)
def test_products_availability_in_cart(logged_in_cart_with_all_products, test_data_item):
    cart_page = logged_in_cart_with_all_products(test_data_item["user_name"], test_data_item["password"])
    assert cart_page.all_products_available_cart() == cart_page.get_cart_item_count()
