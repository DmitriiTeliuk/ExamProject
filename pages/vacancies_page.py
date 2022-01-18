from consts.vacancies_page import VacanciesPageConsts
from pages.base_page import BasePage
from pages.new_vacancy_page import NewVacancyPage
from utils import wait_until_ok


class VacanciesPage(BasePage):
    def __init__(self, driver):
        from pages.header import Header
        super().__init__(driver)
        self.constance = VacanciesPageConsts()
        self.header = Header(self.driver)

    @wait_until_ok(1, 5)
    # @log_decor
    def click_new_vacancy(self):
        """GO to New Vacancy tab"""
        self.wait_until_element_visible(self.constance.NEW_VACANCY_TAB_XPATH).click()
        return NewVacancyPage(self.driver)
