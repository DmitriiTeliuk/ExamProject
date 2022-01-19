from consts.account_page import AccountPageConsts
from pages.base_page import BasePage
from pages.tags_page import TagsPage
from utils import log_decor


class AccountPage(BasePage):
    def __init__(self, driver):
        from pages.header import Header
        super().__init__(driver)
        self.constance = AccountPageConsts()
        self.header = Header(self.driver)

    @log_decor
    def click_tags_tab(self):
        """Navigate to tags tab in Account page"""
        self.wait_until_element_visible(self.constance.TAGS_TAB_XPATH).click()
        return TagsPage(self.driver)
