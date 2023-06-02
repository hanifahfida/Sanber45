import select
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_a_failed_login(self): #test case 1
        driver = self.browser
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("haitest")
        driver.find_element(By.CSS_SELECTOR, "[data-test='password']").send_keys("xxxx")
        driver.find_element(By.NAME,"login-button").click()
        error_message = driver.find_element(By.CSS_SELECTOR, "[data-test=error]").text
        self.assertIn("Epic sadface: Username and password do not match any user in this service", error_message)

    def test_a_success_login(self): #test case 2
        driver = self.browser
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.CSS_SELECTOR, "[data-test='password']").send_keys("secret_sauce")
        driver.find_element(By.NAME,"login-button").click()
        response_data = driver.find_element(By.CLASS_NAME, "title").text
        self.assertIn("Products", response_data)

    def test_a_failed_login_blank(self): #test case 3
        driver = self.browser
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("")
        driver.find_element(By.CSS_SELECTOR, "[data-test='password']").send_keys("")
        driver.find_element(By.NAME,"login-button").click()
        error_message = driver.find_element(By.CSS_SELECTOR, "[data-test=error]").text
        self.assertIn("Epic sadface: Username is required", error_message)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()