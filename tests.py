import pytest

from conftest import BaseTest
from consts.base_consts import BaseConst


@pytest.mark.parametrize("browser", [BaseConst.CHROME])
class TestEntitiesCreation(BaseTest):
    """Tests"""

    @pytest.fixture(scope="function")
    def header(self, open_start_page, user_credentials):
        """Log in to the system"""
        open_start_page.click_agree_cookies()
        login_page = open_start_page.click_login_button()
        header = login_page.successful_login_via_email(user_credentials)
        return header

    @pytest.fixture(scope="function")
    def navigate_to_candidates(self, header):
        """Navigate to Candidates page"""
        candidates_page = header.navigate_to_candidates_tab()
        return candidates_page

    @pytest.fixture(scope="function")
    def navigate_to_clients(self, header):
        """Navigate to Clients page"""
        clients_page = header.navigate_to_clients_tab()
        return clients_page

    @pytest.fixture(scope="function")
    def navigate_to_vacancies(self, header):
        """Navigate to Vacancies page"""
        vacancies_page = header.navigate_to_vacancies_tab()
        return vacancies_page

    @pytest.fixture(scope="function")
    def navigate_to_account(self, header):
        """Navigate to Account page"""
        account_page = header.navigate_to_account_tab()
        return account_page

    @pytest.fixture(scope="function")
    def create_client_and_get_client_info(self, navigate_to_clients, new_client):
        """Creates new client and returns new client name and description"""
        new_client_page = navigate_to_clients.click_new_client_tab()
        new_client_page.create_new_client(new_client)
        yield new_client

    @pytest.fixture(scope="function")
    def create_tag(self, navigate_to_account, new_tag):
        """ Creates tag and returns tag info"""
        tags_tab = navigate_to_account.click_tags_tab()
        created_tag = tags_tab.add_tag(new_tag_name=new_tag.tag_name)
        return created_tag

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

    def test_create_new_vacancy_via_vacancies_tab(self, create_client_and_get_client_info, navigate_to_vacancies,
                                                  new_vacancy):
        """
        Pre-conditions:
            1. Create new Client
        Steps:
            2.Go to new vacancy tab
            3.Create new vacancy for new client
            4.Verify that vacancy is created
        Expected:
            Edit vacancy page button appears
        """
        new_vacancy_page = navigate_to_vacancies.click_new_vacancy()
        vacancy_page = new_vacancy_page.create_vacancy(new_vacancy,
                                                       client_name=create_client_and_get_client_info.client_name)
        vacancy_page.edit_vacancy_button_is_displayed()

    def test_create_tag(self, navigate_to_account, new_tag):
        """
        Pre-conditions:
            1. Log in and go to Account page
        Steps:
            2.Go to Tags tab
            3.Create new tag
            4.Verify that new tag is created
        Expected:
            Message "New tag is saved" appears
        """
        tags_tab = navigate_to_account.click_tags_tab()
        created_tag = tags_tab.add_tag(new_tag_name=new_tag.tag_name)
        created_tag.is_tag_saved()

    def test_edit_tag(self, create_tag, new_tag):
        """
        Pre-conditions:
            1. Log in
            2. Create new tag
        Steps:
            3.Edit tag
            4.Verify that new tag name  is saved
        Expected:
            Message "New tag is saved" appears
            """
        tag_is_edited = create_tag.edit_tag(tag_name=new_tag.tag_name, tag_new_name=new_tag.tag_name_for_edit)
        tag_is_edited.is_tag_edited()
