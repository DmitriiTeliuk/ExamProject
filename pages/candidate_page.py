from consts.candidate_page import CandidatePageConsts
from pages.base_page import BasePage
from pages.header import Header


class CandidatePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.constance = CandidatePageConsts()
        self.header = Header(self.driver)

    def check_candidate_is_saved(self):
        """Check that 'Candidate is saved' message appears"""
        message = self.wait_until_element_visible(self.constance.CANDIDATE_IS_SAVED_SUCCESSFULL_MESSAGE)
        assert message.is_displayed()
