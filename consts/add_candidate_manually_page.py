class AddCandidateManuallyPageConsts:
    LAST_NAME_FIELD_XPATH = "//input[@id='candidate-last-name']"
    FIRST_NAME_FIELD_XPATH = "//input[@id='candidate-first-name']"
    DESIRED_POSITION_LABLE_XPATH = "//div[@class='flex-item desired-position-item']//a//span"
    DESIRED_POSITION_AUTOCOMPLETE_FIELD_XPATH = "//input[@id='s2id_autogen2_search']"
    DESIRED_POSITION_AUTOCOMPLETE_PLUS_IMG_XPATH = "//img[@id='plusIcon']"
    ADD_CANDIDATE_BUTTON_XPATH = "//div[@class='candidate-add__header']//a[@ng-click='saveCandidate()']"
    ADD_TAG_FIELD_XPATH = "//div[@class='tags-dropdown']//input[@id='mainInput']"
    ADD_TAG_LIST_OF_TAGS_XPATH = "//div[text()='TAG_NAME']"
