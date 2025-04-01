from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SignupPage(BasePage):
    signup_card = (By.LINK_TEXT, "Sign up")
    wait_for_element = (By.ID, "sign-username")

    def signup(self, signup_script):
        self.click_element(self.signup_card)
        self.wait_for_element_visible(self.wait_for_element)
        self.execute_script(signup_script)

    def get_alert(self):
        return self.alert_present()
