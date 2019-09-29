import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

TITLE = 'Portfolio Watcher'
HEADER = 'Welcome to Portfolio Watcher'
MESSAGE = 'Here at Portfolio Watcher, we make it easy to track your investments.\n'
MESSAGE += 'Please select below to login or create an account'
MAX_WAIT = 10


class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    # TODO: revisit if necessary
    # def wait_for_row_in_list_table(self, row_text):
    #     start_time = time.time()
    #     while True:
    #         try:
    #             table = self.browser.find_element_by_id('id_list_table')
    #             rows = table.find_elements_by_tag_name('tr')
    #             self.assertIn(row_text, [row.text for row in rows])
    #             return
    #         except (AssertionError, WebDriverException) as e:
    #             if time.time() - start_time > MAX_WAIT:
    #                 raise e
    #             time.sleep(.5)

    def test_can_view_homepage(self):

        # Investor John has just made his first purchase, he wants to use
        # our product to track this. He goes to the homepage.
        self.browser.get('http://localhost:8000')

        # He sees the title "Investment Tracker", a header welcoming him,
        # and a brief message with an intro to what the product is, and
        # instructions on how to continue.
        self.assertIn(TITLE, self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn(HEADER, header_text)
        body_text = self.browser.find_element_by_tag_name('p').text
        self.assertIn(MESSAGE, body_text)

        # Below this, he sees two buttons, one offering to create an account, and the other offering to login.
        login = self.browser.find_element_by_id('id_login').text
        create = self.browser.find_element_by_id('id_create').text
        self.assertIn('Login!', login)
        self.assertIn('Create an account!', create)

    # def test_new_user_can_create_account(self):
    #     pass

