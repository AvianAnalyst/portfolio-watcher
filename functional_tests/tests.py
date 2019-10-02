import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

MAX_WAIT = 10


class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_view_homepage(self):

        title = 'Portfolio Watcher'
        header = 'Welcome to Portfolio Watcher'

        # A new user visits the home page
        self.browser.get('http://localhost:8000')

        # He sees the title "Investment Tracker", a header welcoming him, and a brief message with an intro to
        # what the product is, and  links to continue
        self.assertIn(title, self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn(header, header_text)
        links = self.browser.find_elements_by_tag_name('a')
        self.assertEqual(len(links), 2)

    def test_can_view_report(self):

        # A user navigates to the home page, and clicks 'view portfolio'
        self.browser.get('http://localhost:8000')
        self.browser.find_element_by_link_text('View Portfolio').click()

        # The user gets redirected to a page with a table with headings for Company Cost and Shares
        table_header = self.browser.find_elements_by_tag_name('table')[0].text.split()[:3]
        self.assertIn('Company', table_header)
        self.assertIn('Cost', table_header)
        self.assertIn('Shares', table_header)

    def test_report_changes_with_date_change(self):

        # A user adds an investment for the current day
        self.browser.get('http://localhost:8000')
        self.browser.find_element_by_link_text('New Investment').click()

        # He asserts that 'Carta' is in the company list, if not, he adds it
        companies = self.browser.find_element_by_id('id_company').text
        if not 'Carta' in companies:
            self.browser.find_element_by_link_text('Add company!').click()
            input_field = self.browser.find_element_by_id('id_name')
            input_field.send_keys('Carta')
            self.browser.find_element_by_tag_name('button').click()

        # He creates an entry
        company = self.browser.find_element_by_id('id_company')
        company.click()
        company.send_keys('c')
        self.browser.find_element_by_id('id_cost').send_keys('123')
        self.browser.find_element_by_id('id_num_of_shares').send_keys('321')
        self.browser.find_element_by_tag_name('button').click()

        # he then goes to the reports page
        self.browser.find_element_by_link_text('Generate report!').click()

        # He takes note of the current table
        report = self.browser.find_element_by_tag_name('table').text

        # he then updates the report to a prior date than today, and sees the report has changed
        date = self.browser.find_element_by_tag_name('input')
        date.send_keys('2000-03-31')
        new_report = self.browser.find_element_by_tag_name('table').text
        self.assertNotEqual(report, new_report)
