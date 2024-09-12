from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Test_data import Data
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



    # Test Case ID: TC_PM_03
    def test_create_new_employee(self, bootup):
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, Data.element.username_input_box_path).send_keys(Data.credentials.username)
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, Data.element.password_input_box_path).send_keys(Data.credentials.password)
        self.driver.find_element(By.XPATH, Data.element.login_button_path).click()
        self.driver.implicitly_wait(3)

        self.driver.find_element(By.XPATH, Data.element.pim_menu_path).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, Data.element.add_button_path).click()
        self.driver.implicitly_wait(3)

        # Check if you're in Add Employee page
        assert self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee"

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