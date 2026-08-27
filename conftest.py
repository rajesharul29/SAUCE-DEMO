import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import json
import sys

pytest_plugins = [
    "fixtures.cart_fixtures",
    "fixtures.checkout_yourinfo_fixture",
]


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="function")
def data_load():
    with open("data/test_login.json") as f:
        test_data = json.load(f)
        credentials = test_data["valid_login_credentials"][0]
        return [credentials["user_name"], credentials["password"]]


@pytest.fixture(scope="function")
def browser():
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    })
    chrome_options.add_argument("--disable-save-password-bubble")
    chrome_options.add_argument("--disable-features=PasswordLeakDetection")
    chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")
    # chrome_options.add_argument("--incognito")

    try:
        # Use WebDriver Manager to auto-download correct ChromeDriver
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get("https://www.saucedemo.com/")
        # driver.implicitly_wait(10)
        yield driver
    except Exception as e:
        print(f"\n❌ Chrome initialization failed: {e}", file=sys.stderr)
        raise
    finally:
        try:
            driver.quit()
        except:
            pass


@pytest.fixture(autouse=True)
def screenshot_on_fail(request, browser):
    yield
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        os.makedirs("screenshots", exist_ok=True)
        browser.save_screenshot(f"screenshots/{request.node.name}.png")
        print(f"\nScreenshot saved: screenshots/{request.node.name}.png")
