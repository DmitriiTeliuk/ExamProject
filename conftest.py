import logging
import os

import pytest

from consts.base_consts import BaseConst
from data_for_tests import User, Candidate, Client, Vacancy, NewTag
from pages.start_page import StartPage
from utils import create_driver


def pytest_runtest_setup(item):
    item.cls.log = logging.getLogger(".".join((item.module.__name__, item.cls.__name__, item.name)))


def pytest_sessionstart(session):
    os.environ["PATH"] = os.environ["PATH"] + f":{os.path.abspath(BaseConst.DRIVER_PATH)}"
    print(os.environ["PATH"])


class BaseTest:
    """Set some fields to provide autocomplete for dynamically added fields"""
    log = logging.getLogger(__name__)

    @pytest.fixture(scope="function")
    def driver(self, browser):
        """Create driver and close after tests"""
        driver = create_driver(browser=browser)
        # driver.implicitly_wait(1)
        yield driver
        driver.close()

    @pytest.fixture(scope="function")
    def open_start_page(self, driver):
        """Return start page"""
        driver.get(BaseConst.URL)
        return StartPage(driver)

    @pytest.fixture(scope="function")
    def user_credentials(self):
        """Return registered user credentials"""
        user = User()
        user.fill_user_data()
        return user

    @pytest.fixture(scope="function")
    def new_candidate(self):
        """Generate info about  new candidate"""
        new_candidate = Candidate()
        new_candidate.generate_required_candidate_data()
        return new_candidate

    @pytest.fixture(scope="function")
    def new_client(self):
        """Generate name and descr for new client"""
        new_client = Client()
        new_client.generate_client_description()
        return new_client

    @pytest.fixture(scope="function")
    def new_vacancy(self):
        """Generate min info required to create vacancy"""
        new_vacancy = Vacancy()
        new_vacancy.generate_vacancy_data()
        return new_vacancy

    @pytest.fixture(scope="function")
    def new_tag(self):
        """Generate new tag name"""
        new_tag = NewTag()
        new_tag.generate_tag_name()
        print(new_tag.tag_name_for_edit)
        return new_tag
