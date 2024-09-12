from lib2to3.pgen2 import driver

import self
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from TestData import Data
import time
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class TestOrangeHRM():

    url = "https://opensource-demo.orangehrmlive.com/"

    @pytest.fixture
    def bootup(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(self.url)
        yield
        self.driver.quit()

        # Check if you're in Add Employee page
        assert self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"

        action = ActionChains(self.driver)
        toggle_login_details = self.driver.find_element(By.XPATH, Data.element.create_login_details_toggle_path)
        action.click(on_element=toggle_login_details)
        action.perform()
        self.driver.implicitly_wait(5)

        self.driver.find_element(By.XPATH, Data.element.first_name_path).send_keys(Data.credentials.first_name)
        self.driver.find_element(By.XPATH, Data.element.last_name_path).send_keys(Data.credentials.last_name)
        self.driver.find_element(By.XPATH, Data.element.last_name_path).send_keys(u'\ue007')
        # self.driver.find_element(By.XPATH, data.element.username_text_box_path).send_keys(data.credentials.user_name)
        # self.driver.find_element(By.XPATH, data.element.password_text_box_path).send_keys(data.credentials.pass_word)
        # self.driver.find_element(By.XPATH, data.element.confirm_password_path).send_keys(data.credentials.confirm_pass_word)

        self.driver.implicitly_wait(3)
        assert self.driver.find_element(By.XPATH, Data.element.personal_details).is_displayed()


    def test_select_admin_menu(driver):
    # Navigate to the login page and log in if necessary
    driver.get(url)

    # Assuming you need to log in first, add login steps here if required
    # Example:
    # driver.find_element(By.ID, "username").send_keys("your_username")
    # driver.find_element(By.ID, "password").send_keys("your_password")
    # driver.find_element(By.ID, "login-button").click()

    # Click on the admin menu
    admin_menu = driver.find_element(By.ID, admin_menu_path)
    admin_menu.click()

    # Validate that the admin menu content is displayed
    self.driver.implicitly_wait(5).until(
        EC.visibility_of_element_located((By.ID, "admin-content"))  # Replace with actual ID or locator
    )