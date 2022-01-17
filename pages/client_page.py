from consts.client_page import ClientPageConsts
from pages.base_page import BasePage

from utils import log_decor


class ClientPage(BasePage):
    def __init__(self, driver):
        from pages.header import Header
        super().__init__(driver)
        self.constance = ClientPageConsts()
        self.header = Header(self.driver)

    @log_decor
    def check_client_is_saved(self, client_name):
        """Check that 'Client {client_name} is saved' message appears"""
        locator = self.constance.CLIENT_SUCCESSFULLY_SAVED_MESSAGE
        message_box = self.wait_until_element_visible(locator)
        assert message_box.text == f"Client {client_name} saved"
