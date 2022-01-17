import logging

from selenium.webdriver.chrome import webdriver as chrome
from selenium.webdriver.firefox import webdriver as firefox

from consts.base_consts import BaseConst


def create_driver(browser):
    """Create driver according to browser"""
    if browser == BaseConst.CHROME:
        driver = chrome.WebDriver()
        driver.maximize_window()
    elif browser == BaseConst.FIREFOX:
        driver = firefox.WebDriver()
        driver.maximize_window()
    else:
        raise RuntimeError(f"Unknown browser, name: {browser}")

    return driver


def log_decor(func):
    """Creates logs"""

    def wrapper(*args, **kwargs):
        log = logging.getLogger("[NewLogger]")
        result = func(*args, **kwargs)
        log.info("%s", func.__doc__)
        return result

    return wrapper
