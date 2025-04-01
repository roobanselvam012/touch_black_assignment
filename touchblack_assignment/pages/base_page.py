# import yaml
# import os

# config_path = os.path.join(os.path.dirname(__file__), "..", "config", "config.yaml")

# print(config_path)
# with open(config_path ,'r') as file:
#         config = yaml.safe_load(file)

# base_dir = config["base_dir"]

# print(base_dir)

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator)).click()

    def wait_for_element_visible(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.find_element(locator).click()

    def enter_text(self, locator, text):
        self.driver.find_element(locator).send_keys(text)

    def execute_script(self, script):
        self.driver.execute_script(script)

    def alert_present(self):
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        return alert.text

    def get_current_url(self):
        return self.driver.current_url

