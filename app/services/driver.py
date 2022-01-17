import os
from selenium import webdriver
import chromedriver_autoinstaller

from app.logger import log
from app.utils import HEADLESS_OPTIONS

# TODO: move to config.py
PATH_TO_CHROME_DRIVER = os.environ.get("PATH_TO_CHROME_DRIVER")
assert PATH_TO_CHROME_DRIVER

# chromedriver_autoinstaller.install()
# Check if the current version of chromedriver exists
# and if it doesn't exist, download it automatically,
# then add chromedriver to path


class DriverService:
    def __init__(self, driver_type):
        self.driver = None
        self.initialize_driver(driver_type)
        assert self.driver

    def initialize_driver(self, driver_type):
        if driver_type == "Chrome":
            self.driver = webdriver.Chrome(
                executable_path=PATH_TO_CHROME_DRIVER,
                # options=HEADLESS_OPTIONS,
            )  # allow to access webpages from the chrome browser
            # self.driver = webdriver.Chrome()
        else:
            pass  # TODO: add Firefox

    def get_driver(self):
        return self.driver

    def close_driver_session(self):
        log(log.INFO, "Close driver session")
        self.driver.close()

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        self.close_driver_session()
