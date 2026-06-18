import json
from pageobjects.login_page import LoginPage
import pytest

test_data_path = "data/test_login.json"
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list=test_data["invalid_login_credentials"]
    
@pytest.mark.usefixtures("browser","data_load")
class TestLogin:
    @pytest.mark.smoke
    def test_login_valid_credentials(self,browser,data_load):
        # Test valid login
        driver = browser
        loginpage = LoginPage(driver)
        loginpage.login(data_load[0],data_load[1])
        
        assert driver.current_url == "https://www.saucedemo.com/inventory.html"
        
    @pytest.mark.parametrize("test_list_item", test_list)
    def test_login_invalid_credentials(self,browser,test_list_item):
        driver=browser
        loginpage = LoginPage(driver)
        error_msg=loginpage.invalid_login(test_list_item["user_name"], test_list_item["password"])
        assert "Username and password do not match any user in this service" in error_msg
            

    