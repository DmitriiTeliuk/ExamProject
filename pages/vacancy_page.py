from consts.vacancy_page import VacancyPageConsts
from pages.base_page import BasePage


class VacancyPage(BasePage):
    def __init__(self, driver):
        from pages.header import Header
        super().__init__(driver)
        self.constance = VacancyPageConsts()
        self.header = Header(self.driver)
