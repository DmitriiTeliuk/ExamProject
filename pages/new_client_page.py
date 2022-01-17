from consts.new_client_page import NewClientPageConsts
from pages.base_page import BasePage
from pages.client_page import ClientPage
from utils import log_decor


class NewClientPage(BasePage):
    def __init__(self, driver):
        from pages.header import Header
        super().__init__(driver)
        self.constance = NewClientPageConsts()
        self.header = Header(self.driver)

    @log_decor
    def create_new_client(self, client_info):
        """Fill name and descr about client.-> Create client"""
        self.fill_field(self.constance.CLIENT_NAME_FIELD_XPATH, client_info.client_name)
        iframe_locator = self.constance.CLIENT_DESCR_IFRAME_XPATH
        field_locator = self.constance.CLIENT_DESCRIPTION_FIELD_XPATH
        self.fill_field_in_iframe(iframe_locator, field_locator, client_info.client_description)
        self.wait_until_element_visible(self.constance.SAVE_CLIENT_BUTTON).click()
        return ClientPage(self.driver)
