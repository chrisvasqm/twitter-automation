import unittest

from selenium import webdriver

import config
from pages.landing_page import LandingPage


class TwitterTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        self.landing_page = LandingPage(self.driver)
        self.landing_page.open()

    def test_create_new_account(self):
        sign_up_page = self.landing_page.go_to_sign_up_page()
        sign_up_page.sign_up_by_email("name", "chrisvasqm@gmail.com")

        if sign_up_page.is_email_already_taken():
            assert True

        # TODO: continue the sign up process

    def test_write_a_tweet(self):
        self.landing_page.login(config.email, config.password)

    def tearDown(self):
        self.driver.quit()
