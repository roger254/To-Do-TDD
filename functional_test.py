import time

from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # {USER} has heard about a cool new online to-do app.
        # {USER} goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # {USER} notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)

        # User is invited to enter a to-do item straight away
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # User types 'Buy a book' into a text box
        input_box.send_keys('The Buy a book')

        # when user hits enter, the page updates, and now the page lists
        # '1: Buy a book; as an item in a to-do list
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy a book' for row in rows),
            'New to-do item did not appear in table'
        )
        # There is still a text box inviting her to add another item
        # user enters 'Read book 2 hours a day'
        self.fail('Finish the test!')
        # The page updates again and now shows both items on her list

        # user wonders whether the site will remember the list. The user
        # sees that the site has generated a unique URL for them -- there is some
        # explanatory text to that effect

        # user visits that url - their to-do list is still there


if __name__ == '__main__':
    unittest.main(warnings='ignore')
