from consts.login_page import LoginPageConsts
from pages.base_page import BasePage
from pages.header import Header
from utils import log_decor


class LoginPage(BasePage):
    """"""

    def __init__(self, driver):
        super().__init__(driver)
        self.constance = LoginPageConsts()

    @log_decor
    def successful_login_via_email(self, credentials):
        """Fill login/password and click Log in button"""
        self.fill_field(locator=self.constance.EMAIL_FIELD_XPATH, some_value=credentials.user_email)
        self.fill_field(locator=self.constance.PASSWORD_FIELD_XPATH, some_value=credentials.user_password)
        self.wait_until_find_element(self.constance.SIGN_IN_BUTTON_XPATH).click()
        return Header(self.driver)
