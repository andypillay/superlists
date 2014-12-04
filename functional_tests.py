from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Jeff hears about a online to-do app and goes to
		# check the homepage
		self.browser.get('http://localhost:8000')

		# He notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

# He is invited to enter a to-do item straight away

# He types "Buy shin pads" into a text box (His hobby is football)

# When he hits enter, the page updates, and now the page lists
# "1: Buy peacock feathers" as an item in a to-do lists

# There is still a text box inviting her to add another item. He
# enters "Buy food for gym"

# The page updates again, and now shows both items on his lists

# Jeff wonders whether the site will remember his list. The he sees
# that the site has a generated a unique URL for him -- There is some
# explantory text to that effect.

# He visits that URL - His to do list is still there.

# Happy, Jeff goes to sleep

if __name__ == '__main__':
	unittest.main(warnings='ignore')

browser.quit()