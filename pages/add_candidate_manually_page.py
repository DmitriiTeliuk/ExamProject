from consts.add_candidate_manually_page import AddCandidateManuallyPageConsts
from pages.base_page import BasePage
from utils import log_decor


class AddCandidateManuallyPage(BasePage):
    def __init__(self, driver):
        from pages.header import Header
        super().__init__(driver)
        self.constance = AddCandidateManuallyPageConsts()
        self.header = Header(self.driver)

    @log_decor
    def create_candidate(self, candidate):
        """Fill new candidate info at new candidate page and click Add button"""
        from pages.candidate_page import CandidatePage
        self.fill_field(self.constance.LAST_NAME_FIELD_XPATH, some_value=candidate.first_name)
        self.fill_field(self.constance.FIRST_NAME_FIELD_XPATH, some_value=candidate.last_name)
        self.wait_until_find_element(self.constance.DESIRED_POSITION_LABLE_XPATH).click()
        self.wait_until_element_visible(self.constance.DESIRED_POSITION_AUTOCOMPLETE_FIELD_XPATH)
        self.fill_field(self.constance.DESIRED_POSITION_AUTOCOMPLETE_FIELD_XPATH, some_value=candidate.desired_position)
        self.wait_until_element_visible(self.constance.DESIRED_POSITION_AUTOCOMPLETE_PLUS_IMG_XPATH).click()
        self.wait_until_find_element(self.constance.ADD_CANDIDATE_BUTTON_XPATH).click()
        return CandidatePage(self.driver)
