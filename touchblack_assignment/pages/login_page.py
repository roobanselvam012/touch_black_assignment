from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    login_card = (By.LINK_TEXT, "Log in")
    wait_for_element = (By.ID, "loginusername")
    dash_board_element = (By.LINK_TEXT, "Welcome roobanselvam012@gmail.com")
    
    def login(self, login_script):
        self.click_element(self.login_card)
        self.wait_for_element_visible(self.wait_for_element)
        self.execute_script(login_script)

    def get_dashboard(self):
        return self.find_element(self.dash_board_element).text

    def get_alert(self):
        return self.alert_present()
