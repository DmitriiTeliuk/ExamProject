from consts.tags_page import TagsPageConsts
from pages.base_page import BasePage
from utils import log_decor


class TagsPage(BasePage):
    def __init__(self, driver):
        from pages.header import Header
        super().__init__(driver)
        self.constance = TagsPageConsts()
        self.header = Header(self.driver)

    @log_decor
    def add_tag(self, new_tag_name):
        """Add new tag on Tags Page"""
        self.wait_until_element_clickable(self.constance.ADD_TAG_BUTTON_XPATH).click()
        tag_name_field = self.constance.TAG_NAME_FIELD_XPATH
        self.wait_until_element_visible(tag_name_field)
        self.fill_field(tag_name_field, some_value=new_tag_name)
        self.wait_until_element_clickable(self.constance.SAVE_TAG_BUTTON_XPATH).click()
        return TagsPage(self.driver)

    @log_decor
    def is_tag_saved(self):
        """Check that 'Tag added' message appears"""
        message = self.wait_until_element_visible(self.constance.TAG_ADDED_SUCCESSFUL_MESSAGE_XPATH)
        assert message.is_displayed()

    @log_decor
    def edit_tag(self, tag_name, tag_new_name):
        """Edit tag that was created before"""
        self.wait_until_element_clickable(self.constance.EDIT_TAG_BUTTON_ON_TAG_XPATH.format(tag_name=tag_name)).click()
        tag_name_field = self.constance.TAG_NAME_FIELD_XPATH
        self.wait_until_element_visible(tag_name_field)
        self.fill_field(tag_name_field, some_value=tag_new_name)
        self.wait_until_element_clickable(self.constance.SAVE_NEW_NAME_FOR_TAG_BUTTON_XPATH).click()
        return TagsPage(self.driver)

    @log_decor
    def is_tag_edited(self):
        """Check that 'Tag new name saved' message appears"""
        message = self.wait_until_element_visible(self.constance.TAG_EDITED_SUCCESSFUL_MESSAGE_XPATH)
        assert message.is_displayed()
