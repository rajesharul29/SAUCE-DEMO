import json
import pytest

test_data_path = "data/test_login.json"
with open(test_data_path) as f:
    test_data = json.load(f)
    valid_credentials = test_data["valid_login_credentials"][0]


def test_Checkout_yourinfo_page_loaded_successfully(browser, checkout_your_info_page):
    driver = browser
    checkout_your_info_page(valid_credentials["user_name"], valid_credentials["password"])
    assert driver.current_url == "https://www.saucedemo.com/checkout-step-one.html"


def test_page_header(checkout_your_info_page):
    checkout_your_info_page = checkout_your_info_page(valid_credentials["user_name"], valid_credentials["password"])
    assert checkout_your_info_page.get_page_header() == "Checkout: Your Information"


def test_page_title(checkout_your_info_page):
    checkout_your_info_page = checkout_your_info_page(valid_credentials["user_name"], valid_credentials["password"])
    assert checkout_your_info_page.get_page_title() == "Swag Labs"


def test_form_place_holder_texts(checkout_your_info_page):
    checkout_your_info_page = checkout_your_info_page(valid_credentials["user_name"], valid_credentials["password"])
    assert checkout_your_info_page.verify_placeholder_text() == ["First Name", "Last Name", "Zip/Postal Code"]


def test_continue_with_valid_details(browser, checkout_your_info_page):
    driver = browser
    checkout_your_info_page = checkout_your_info_page(valid_credentials["user_name"], valid_credentials["password"])
    checkout_your_info_page.enter_user_details("Arul", "Rajeesh", "123456")
    assert driver.current_url == "https://www.saucedemo.com/checkout-step-two.html"


@pytest.mark.parametrize(
    "firstname, lastname, postalcode, expected_error",
    [
        ("", "Rajeesh", "123456", "Error: First Name is required"),
        ("Arul", "", "123456", "Error: Last Name is required"),
        ("Arul", "Rajeesh", "", "Error: Postal Code is required"),
    ],
)
def test_continue_with_missing_required_field(browser, checkout_your_info_page, firstname, lastname, postalcode, expected_error):
    driver = browser
    checkout_your_info_page = checkout_your_info_page(valid_credentials["user_name"], valid_credentials["password"])
    checkout_your_info_page.fill_user_details(firstname, lastname, postalcode)
    checkout_your_info_page.click_continue_button()
    assert checkout_your_info_page.get_error_message() == expected_error
    assert driver.current_url == "https://www.saucedemo.com/checkout-step-one.html"
