from consts.candidates_page import CandidatesPageConsts
from pages.base_page import BasePage
from pages.header import Header
from utils import log_decor


class CandidatesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.constance = CandidatesPageConsts()
        self.header = Header(self.driver)

    @log_decor
    def is_displayed_new_candidate_tab(self):
        """"Check is new candidate tab displayed"""
        new_cadidate_tab = self.wait_until_find_element(self.constance.NEW_CANDIDATE_TAB_XPATH)
        assert new_cadidate_tab.is_displayed()

    @log_decor
    def click_add_candidate_manually(self):
        """Click add candidate manually button on Candidates page"""
        from pages.add_candidate_manually_page import AddCandidateManuallyPage
        self.wait_until_find_element(self.constance.NEW_CANDIDATE_TAB_XPATH).click()
        return AddCandidateManuallyPage(self.driver)
