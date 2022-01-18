from consts.vacancy_page import VacancyPageConsts
from pages.base_page import BasePage


class VacancyPage(BasePage):
    def __init__(self, driver):
        from pages.header import Header
        super().__init__(driver)
        self.constance = VacancyPageConsts()
        self.header = Header(self.driver)

    def edit_vacancy_button_is_displayed(self):
        edit_vacancy_button = self.wait_until_element_visible(self.constance.EDIT_VACANCY_PAGE_XPATH)
        assert edit_vacancy_button.is_displayed()
