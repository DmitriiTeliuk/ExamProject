import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.log = logging.getLogger(__name__)
        self.wait = WebDriverWait(driver, timeout=5)

    def fill_field(self, locator, some_value):
        """Filling field"""
        user_field = self.wait_until_find_element(locator=locator)
        user_field.clear()
        user_field.send_keys(some_value)

    def fill_field_in_iframe(self, iframe_locator, field_locator, some_value):
        """Switch to iframe, find element in iframe and fill it"""
        self.driver.switch_to.frame(self.wait_until_find_element(iframe_locator))
        field = self.wait_until_find_element(field_locator)
        field.clear()
        field.send_keys(some_value)
        self.driver.switch_to.default_content()

    def wait_until_find_element(self, locator):
        """Wait unlit element is found"""
        return self.wait.until(EC.presence_of_element_located(locator=(By.XPATH, locator)))

    def wait_until_element_clickable(self, locator):
        """Wait unlit element is clickable"""
        return self.wait.until(EC.element_to_be_clickable(mark=(By.XPATH, locator)))

    def wait_until_element_visible(self, locator):
        """Wait unlit element is visible"""
        return self.wait.until(EC.visibility_of_element_located(locator=(By.XPATH, locator)))
