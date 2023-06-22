from pages.header import Header
from pages.main_page import MainPage
from pages.search_result_page import SearchResultsPage
from pages.signin_page import SigninPage


class Application:

    def __init__(self, driver):
        self.header = Header
        self.driver = driver
        self.header = Header(self.header)
        self.main_page = MainPage(self.driver)
        self.search_result_page = SearchResultsPage(self.driver)
        self.sign_in_page = SigninPage(self.driver)

