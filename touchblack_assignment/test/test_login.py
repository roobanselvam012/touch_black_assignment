from pages.login_page import LoginPage
from utils.logger import log

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# CONFIG_PATH = os.path.join(BASE_DIR, "..", "config", "config.yaml")

# CONFIG_PATH = os.path.abspath(CONFIG_PATH)

# with open(CONFIG_PATH, 'r') as file:
#     config = yaml.safe_load(file)

def test_login(driver):
    log.info("Executing Login test")
    login_page = LoginPage(driver)
    login_script = """
    document.getElementById('loginusername').value = 'roobanselvam012@gmail.com';
    document.getElementById('loginpassword').value = 'rooban012S#';
    document.querySelector("button[onclick='logIn()']").click();"""
    login_page.login(login_script)


    alert = login_page.get_dashboard()
    assert alert == "Welcome roobanselvam012@gmail.com", "login failed"

    log.info("Login Test Passed")


def test_failed_login(driver):
    log.info("Executing invalid login test")
    login_page = LoginPage(driver)
    login_script = """
    document.getElementById('loginusername').value = 'invalid@gmail.com';
    document.getElementById('loginpassword').value = 'rooban012S#';
    document.querySelector("button[onclick='logIn()']").click();"""
    login_page.login(login_script)
    alert = login_page.get_alert()
    assert alert == 'Wrong password.', "Invalid login failed"

    log.info("Invalid login test Passed")