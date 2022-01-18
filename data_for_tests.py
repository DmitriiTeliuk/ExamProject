import random

users_lst = [
    ("d.teliuk@gmail.com", "goldenmask3421L"),
    ("worab68164@huekieu.com", "Qwerty123"),
    ("hurzocurku@vusra.com", "qwertY123"),
    ("gekkiromli@vusra.com", "qatest234"),
    ("mostutarze@vusra.com", "qatest678")
]

first_name_lst = ["Anna", "Olga", "Dmitrii", "Denis", "Bogdan"]
last_name_lst = ["Tester", "Senior", "Junior", "Middle", "Teamlead"]
position_lst = ["QA", "Team Lead", "TechRighter", "Project Manager", "Sys admin"]

employment_status_lst = [
    "Full time",
    "Part Time",
    "Remote",
    "Internship, Practice",
    "Temporary",
    "Relocate"
]

country_lst = ["Algeria"]
city_lst = ["Algiers Province"]

base_text = """Welcome to the weather forecast. 
        Now, let’s see what the weather is like today. 
        In the north of the country, it’s very windy and cold. 
        There is a chance of some rain too, so don’t leave home without your umbrella! 
        The temperature is around 10 degrees centigrade. In the east it’s rainy all day today, 
        I’m afraid. There may be a thunderstorm in the afternoon. 
        The temperature is a bit higher, at around 13 degrees.
        In the west and middle of the country, the weather is dry but cloudy. 
        So no rain for you, but it is quite windy and the temperature is just 10 degrees. 
        The south of the country has the best weather today. 
        It’s cloudy most of the time but sunny this afternoon."""


def generate_text(word_count):
    """Generate some string"""

    text_lst = base_text.replace("\n", " ").replace(",", " ").replace(".", " ").split(" ")
    lst_without_none = []
    generate_text_lst = []
    # Delete all '' in the list
    for elem in text_lst:
        if elem != '':
            lst_without_none.append(elem)
    # Randomly select {word_count} number of items from list
    for _ in range(word_count):
        generate_text_lst.append(random.choice(lst_without_none))
    #  make final sentence
    final_generated_text = " ".join(generate_text_lst)
    return final_generated_text


class User:

    def __init__(self, user_creds=(), user_email="", user_password="", test_name=""):
        self.user_creds = user_creds
        self.user_email = user_email
        self.user_password = user_password
        self.test_name = test_name

    def fill_user_data(self):
        """ Set it up as users login and user password pare from list according to test name"""
        if self.test_name == "test_create_candidate":
            self.user_creds = users_lst[4]
            self.user_email = self.user_creds[0]
            self.user_password = self.user_creds[1]
        elif self.test_name == "test_create_client":
            self.user_creds = users_lst[3]
            self.user_email = self.user_creds[0]
            self.user_password = self.user_creds[1]
        elif self.test_name == "test_create_new_vacancy_via_vacancies_tab":
            self.user_creds = users_lst[2]
            self.user_email = self.user_creds[0]
            self.user_password = self.user_creds[1]
        elif self.test_name == "test_create_tag":
            self.user_creds = users_lst[1]
            self.user_email = self.user_creds[0]
            self.user_password = self.user_creds[1]
        else:
            self.user_creds = users_lst[0]
            self.user_email = self.user_creds[0]
            self.user_password = self.user_creds[1]


class Candidate:

    def __init__(self, candidate_first_name="", candidate_last_name="", candidate_desired_position=""):
        self.first_name = candidate_first_name
        self.last_name = candidate_last_name
        self.desired_position = candidate_desired_position

    def generate_required_candidate_data(self):
        """Generates candidate with required data for candidate profile creation: First name, Last name, Position"""
        self.first_name = first_name_lst[random.randrange(len(first_name_lst))]
        self.last_name = last_name_lst[random.randrange(len(last_name_lst))]
        self.desired_position = position_lst[random.randrange(len(position_lst))]


class Client:

    def __init__(self, client_name="", client_description=""):
        self.client_name = client_name
        self.client_description = client_description

    def generate_client_description(self):
        """Generate Client name and description for test"""
        self.client_name = generate_text(5)
        self.client_description = generate_text(15)


class Vacancy:
    def __init__(self, title="", employment_type="", country="", city="", description=""):
        self.vacancy_title = title
        self.employment_type = employment_type
        self.country = country
        self.city = city
        self.vacancy_description = description

    def generate_vacancy_data(self):
        """Generate Vacancy title, description, employment type,country and city for test"""
        self.vacancy_title = generate_text(5)
        self.employment_type = employment_status_lst[random.randrange(len(employment_status_lst))]
        self.country = country_lst[random.randrange(len(country_lst))]
        self.city = city_lst[random.randrange(len(city_lst))]
        self.vacancy_description = base_text * 5
        print(self.employment_type)
        print(self.country)
        print(self.city)


class NewTag:
    """Class contains tag name and name that will be used as new name for same tag during Tag editing process"""

    def __init__(self, name="", tag_name_for_edit=""):
        self.tag_name = name
        self.tag_name_for_edit = tag_name_for_edit

    def random_num(self):
        return str(random.choice(range(111111, 999999)))

    def generate_tag_name(self):
        self.tag_name = f"TagNumber{self.random_num()}"
        self.tag_name_for_edit = f"TagEdit{self.random_num()}"
