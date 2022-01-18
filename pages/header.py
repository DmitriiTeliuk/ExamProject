from consts.header import HeaderConsts
from pages.account_page import AccountPage
from pages.base_page import BasePage
from pages.clients_page import ClientsPage
from pages.vacancies_page import VacanciesPage
from utils import log_decor


class Header(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constance = HeaderConsts()

    @log_decor
    def is_main_bar_visible(self):
        """check if main bar is visible"""
        main_bar = self.wait_until_element_visible(self.constance.MAIN_NAVIGATION_BAR_XPATH)
        assert main_bar.is_displayed()

    @log_decor
    def navigate_to_candidates_tab(self):
        """Go to Candidates Page"""
        from pages.candidates_page import CandidatesPage
        # try:
        self.wait_until_element_visible(self.constance.CANDIDATES_TAB_XPATH).click()
        # except Exception :
        #
        #     self.wait_until_element_visible(self.constance.CANDIDATES_TAB_IN_BURGER_MENU_XPATH).click()
        return CandidatesPage(self.driver)

    @log_decor
    def navigate_to_clients_tab(self):
        """Go to Clients Page"""
        self.wait_until_element_visible(self.constance.CLIENTS_TAB_XPATH).click()
        return ClientsPage(self.driver)

    @log_decor
    def navigate_to_vacancies_tab(self):
        """Go to Vacancies Page"""
        self.wait_until_element_clickable(self.constance.VACANCIES_TAB_XPATH).click()
        return VacanciesPage(self.driver)

    @log_decor
    def navigate_to_account_tab(self):
        """Go to Account Page"""
        self.wait_until_element_clickable(self.constance.ACCOUNT_TAB_XPATH).click()
        return AccountPage(self.driver)
