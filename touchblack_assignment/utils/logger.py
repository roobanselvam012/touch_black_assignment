import logging
import yaml
import os

def get_logger():
    logger = logging.getLogger("Test Automation")
    logger.setLevel(logging.INFO)
    # config_file = config_path = os.path.join(os.path.dirname(__file__), "..", "config", "config.yaml")
    # with open(config_file ,'r') as file:
    #     config = yaml.safe_load(file)

    # base_dir = config["base_dir"]

    handler = logging.FileHandler("logs/test_execution.log")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger

log= get_logger()