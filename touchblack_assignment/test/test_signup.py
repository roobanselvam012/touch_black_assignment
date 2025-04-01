from pages.signup_page import SignupPage
from utils.logger import log

def test_existing_signup(driver):
    log.info("executing existing user signup")
    signup_page = SignupPage(driver)
    signup_script = """
    document.getElementById('sign-username').value = 'roobanselvam012@gmail.com';
    document.getElementById('sign-password').value = 'rooban012S#';
    document.querySelector("button[onclick='register()']").click();"""
    signup_page.signup(signup_script)

    alert = signup_page.get_alert()
    assert alert == "This user already exist.", "SignUp existing user execution failed"

    log.info("SignUp Existing User Executed Successfully")