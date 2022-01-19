from selenium.webdriver import Keys

from consts.new_vacancy_page import NewVacancyPageConsts
from pages.base_page import BasePage
from pages.vacancy_page import VacancyPage
from utils import log_decor


class NewVacancyPage(BasePage):
    def __init__(self, driver):
        from pages.header import Header
        super().__init__(driver)
        self.constance = NewVacancyPageConsts()
        self.header = Header(self.driver)

    @log_decor
    def create_vacancy(self, vacancy_info, client_name):
        """Create vacancy. Add title, client, location, employment type, descr(must be at least 800 symbols)"""
        self.wait_until_element_clickable(self.constance.NOT_IT_RADIO_BUTTON).click()
        self.fill_field(self.constance.JOB_TITLE_XPATH, vacancy_info.vacancy_title)
        self.wait_until_element_visible(self.constance.CLIENT_FIELD_XPATH).click()
        self.wait_until_element_visible(self.constance.CLIENT_ITEM_IN_LIST_XPATH.format(client=client_name)).click()
        self.wait_until_element_visible(self.constance.EMPLOYMENT_TYPE_FIELD_XPATH).click()
        self.wait_until_element_clickable(
            self.constance.EMPLOYMENT_TYPE_OPTION_XPATH.format(type=vacancy_info.employment_type)).click()
        self.wait_until_element_visible(self.constance.COUNTRY_FIELD_XPATH).click()
        self.wait_until_element_clickable(
            self.constance.COUNTRY_ITEM_IN_LIST_XPATH.format(country=vacancy_info.country)).click()
        self.wait_until_element_visible(self.constance.CITY_FIELD_XPATH).click()
        self.wait_until_element_visible(self.constance.CITY_ITEM_IN_LIST_XPATH.format(city=vacancy_info.city)).click()
        iframe = self.constance.DESCRIPTION_FIELD_IFRAME_XPATH
        locator = self.constance.BODY_IN_IFRAME_XPATH
        self.fill_field_in_iframe(iframe, locator, some_value=vacancy_info.vacancy_description)
        self.wait_until_find_element(self.header.constance.VACANCIES_TAB_XPATH).send_keys(Keys.HOME)
        self.wait_until_element_clickable(self.constance.VACANCY_SAVE_BUTTON_XPATH).click()
        return VacancyPage(self.driver)

