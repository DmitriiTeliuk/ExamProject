import datetime
import logging
from time import sleep

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


def wait_until_ok(timeout, period):
    logger = logging.getLogger("[WaitUntilOk]")

    def decorator(original_function):

        def wrapper(*args, **kwargs):
            end_time = datetime.datetime.now() + datetime.timedelta(seconds=timeout)
            while True:
                try:
                    return original_function(*args, **kwargs)
                except Exception as err:
                    if datetime.datetime.now() > end_time:
                        logger.warning(f"Catch: {err}")
                        raise err
                    else:
                        sleep(period)

        return wrapper

    return decorator
