import time
import unittest

from selenium import webdriver

from pages.home_page import HomePage


class TwitterTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        self.home_page = HomePage(self.driver)
        self.home_page.open()

    def test_create_new_account(self):
        sign_up_page = self.home_page.go_to_sign_up_page()

        time.sleep(5)

    def tearDown(self):
        pass
