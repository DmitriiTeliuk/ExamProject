import pytest

from conftest import BaseTest
from consts.base_consts import BaseConst


@pytest.mark.parametrize("browser", [BaseConst.CHROME])
class TestEntitiesCreation(BaseTest):
    """Tests"""

    @pytest.fixture(scope="function")
    def header(self, open_start_page, user_credentials):
        open_start_page.click_agree_cookies()
        login_page = open_start_page.click_login_button()
        header = login_page.successful_login_via_email(user_credentials)
        return header

    @pytest.fixture(scope="function")
    def navigate_to_candidates(self, header):
        candidates_page = header.navigate_to_candidates_tab()
        return candidates_page

    @pytest.fixture(scope="function")
    def navigate_to_clients(self, header):
        clients_page = header.navigate_to_clients_tab()
        return clients_page

    @pytest.fixture(scope="function")
    def navigate_to_vacancies(self, header):
        vacancies_page = header.navigate_to_vacancies_tab()
        return vacancies_page

    @pytest.fixture(scope="function")
    def create_client_and_get_client_info(self, navigate_to_clients, new_client):
        """Creates new client and returns new client name and description"""
        new_client_page = navigate_to_clients.click_new_client_tab()
        new_client_page.create_new_client(new_client)
        yield new_client

    def test_create_candidate(self, navigate_to_candidates, new_candidate):
        """
        Pre-conditions:
            1. Log in to the system
            2. Go to Candidates page
        Steps:
            3.Click create new candidate
            4. Fill candidate data and save new candidate
            5. Verify that candidate is saved
        Expected:
            6. 'Candidate is saved' message appears
        """
        add_candidate_page = navigate_to_candidates.click_add_candidate_manually()
        candidate_page = add_candidate_page.create_candidate(new_candidate)
        candidate_page.check_candidate_is_saved()

    def test_create_client(self, navigate_to_clients, new_client):
        """
        Pre-conditions:
            1. Log in to the system
            2. Go to Clients page
        Steps:
            3.Click create new client
            4. Fill client info and save new client
            5. Verify that client is created
        Expected:
            6. Client "Client name" message appears
        """
        new_client_page = navigate_to_clients.click_new_client_tab()
        client_page = new_client_page.create_new_client(new_client)
        client_page.check_client_is_saved(new_client.client_name)

    def test_create_new_vacancy_via_vacancies_tab(self, navigate_to_vacancies, new_vacancy):
        """
        Pre-conditions:
            1. Create new Client
        Steps:
            2.Go to new vacancy tab
            3.Create new vacancy for new client
            4.Verify that vacancy is created
        Expected:
            Successful message is displayed
        """
        new_vacancy_page = navigate_to_vacancies.click_new_vacancy()
        # new_vacancy_page.create_vacancy(new_vacancy, client_name="My client")
        new_vacancy_page.create_vacancy(new_vacancy, client_name="My client")
