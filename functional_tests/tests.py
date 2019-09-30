import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

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

        TITLE = 'Portfolio Watcher'
        HEADER = 'Welcome to Portfolio Watcher'
        INVEST_MESSAGE = 'Investments allows you to select what date to include investments up to (inclusive). If ' \
                         'unselected, it will default to today.'
        CORRECT_MESSAGE = 'Corrections allows you to select what date to include corrections up to (inclusive). If ' \
                          'unselected, it will default to today.'

        # Investor John has just made his first purchase, he wants to use
        # our product to track this. He goes to the homepage.
        self.browser.get('http://localhost:8000')

        # He sees the title "Investment Tracker", a header welcoming him,
        # and a brief message with an intro to what the product is, and
        # instructions on how to continue.
        self.assertIn(TITLE, self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn(HEADER, header_text)
        invest_text = self.browser.find_element_by_id('id_invest_msg')
        correct_text = self.browser.find_element_by_id('id_correct_msg')
        self.assertIn(INVEST_MESSAGE, invest_text)
        self.assertIn(CORRECT_MESSAGE, correct_text)

        # He then sees two fields, each selects a date. One is labeled investments, the other corrections.
        invest_input = self.browser.find_element_by_id('id_invest_date')
        correct_input = self.browser.find_element_by_id('id_correct_date')

        # He selects


    # def test_new_user_can_create_account(self):
    #     pass

