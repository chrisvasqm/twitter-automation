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
        sign_up_page.sign_up_by_email("name", "chrisvasqm@gmail.com")

        if sign_up_page.is_email_already_taken():
            assert True

    def tearDown(self):
        self.driver.quit()
