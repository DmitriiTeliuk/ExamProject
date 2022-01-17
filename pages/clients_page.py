from consts.clients_page import ClientsPageConsts
from pages.base_page import BasePage

from utils import log_decor


class ClientsPage(BasePage):
    def __init__(self, driver):
        from pages.header import Header
        super().__init__(driver)
        self.constance = ClientsPageConsts()
        self.header = Header(self.driver)

    @log_decor
    def click_new_client_tab(self):
        """Click edit client tab on ClientsPage"""
        from pages.new_client_page import NewClientPage
        self.wait_until_find_element(self.constance.CREATE_NEW_CLIENT_TAB_XPATH).click()
        return NewClientPage(self.driver)
