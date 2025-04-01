import pytest
import yaml
from selenium import webdriver
from utils.logger import log
import os

@pytest.fixture
def driver():
    config_file = os.path.join(os.path.dirname(__file__), "config/config.yaml")

    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)

    print(config["browser"])
    
    if config["browser"] == "chrome":
        driver = webdriver.Chrome()

    else:
        raise ValurError("unsupported browser")

    driver.get(config["base_url"])
    driver.maximize_window()
    log.info("Browser launched")

    yield driver
    driver.quit()
    log.info("Browser Closed")


