import time
import unittest

from selenium import webdriver

from pages.home_page import HomePage


class TwitterTests(unittest.TestCase):

    def setUp(self):
        self._browser = webdriver.Chrome()
        self._browser.maximize_window()

        self._home_page = HomePage(self._browser)
        self._home_page.open()

    def test_create_new_account(self):
        sign_up_page = self._home_page.go_to_sign_up_page()

        time.sleep(5)

    def tearDown(self):
        pass
