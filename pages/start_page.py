from consts.start_page import StartPageConsts
from pages.base_page import BasePage
from pages.login_page import LoginPage
from utils import log_decor


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constance = StartPageConsts()

    @log_decor
    def click_login_button(self):
        """Click login button on Start Page"""
        self.wait_until_element_clickable(self.constance.LOGIN_BUTTON_XPATH).click()
        return LoginPage(self.driver)

    @log_decor
    def click_agree_cookies(self):
        """Click agree cookie button on StartPage"""
        self.wait_until_element_visible(self.constance.COOKIE_AGREE_BUTTON_XPATH).click()
        return StartPage(self.driver)
