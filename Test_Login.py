from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver

from TestData import Data
import time
import pytest

class TestOrangeHRM():

    url = "https://opensource-demo.orangehrmlive.com/"

    @pytest.fixture
    def bootup(self):
        self.driver = webdriver.Firefox()
        yield
        self.driver.quit()

    def driver(self, bootup):
        # Initialize WebDriver (for example, using Chrome)
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)  # Set implicit wait time to 10 seconds
        yield driver
        driver.quit()

    def test_forgot_password(self, bootup):
        # Navigate to the login page
        driver.get(url)

        # Click on the "Forgot Password" link
        forgot_password_link = driver.find_element(By.LINK_TEXT, FORGOT_PASSWORD_LINK_TEXT)
        forgot_password_link.click()

        # Optionally, verify that you are redirected to the correct page or see the expected elements
        self.driver.implicitly_wait(5).until(
            EC.presence_of_element_located((By.ID, "forgot-password-page"))  # Replace with actual ID or locator
        )

    # Test Case ID: TC_Login_01 (Succesful Login)
    def test_login(self, bootup):
        self.driver.get(self.url)

        ## To check if correct webpage is displayed
        assert self.driver.title == "OrangeHRM"

        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, Data.element.username_input_box_path).send_keys(Data.credentials.username)
        self.driver.find_element(By.XPATH, Data.element.password_input_box_path).send_keys(Data.credentials.password)
        self.driver.find_element(By.XPATH, Data.element.login_button_path).click()
        self.driver.implicitly_wait(3)

        ## To check if the login was successful
        assert self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"
        print("Login Successful!")

    def get(self, url):
        pass

    def find_element(self, LINK_TEXT, FORGOT_PASSWORD_LINK_TEXT):
        pass