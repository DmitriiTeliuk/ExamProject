class TagsPageConsts:
    EXISTING_TAG_BUTTON_XPATH = "//div[@class='tags-main']//div[@title='{tag_name}']"
    EDIT_TAG_BUTTON_ON_TAG_XPATH = "//div[@title='{tag_name}']//div[@role='button']"
    TAG_NAME_FIELD_XPATH = "//input[@type='text']"
    SAVE_TAG_BUTTON_XPATH = "//button[@translate='add']"
    SAVE_NEW_NAME_FOR_TAG_BUTTON_XPATH = "//button[@translate='Edit']"
    ADD_TAG_BUTTON_XPATH = "//button[@ng-click='vm.addTag(vm)']"
    TAG_ADDED_SUCCESSFUL_MESSAGE_XPATH = "//div[@role='alert']//div[text()='Tag added']"
    TAG_EDITED_SUCCESSFUL_MESSAGE_XPATH = "//div[@role='alert']//div[text()='Tag name saved']"
