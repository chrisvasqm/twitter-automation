import unittest

from selenium import webdriver

import config
import strings
from pages.landing_page import LandingPage
from pages.new_tweet_dialog import NewTweetModal


class TwitterTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        self.landing_page = LandingPage(self.driver)
        self.landing_page.open()

    def test_create_new_account(self):
        sign_up_page = self.landing_page.go_to_sign_up_page()
        sign_up_page.sign_up_by_email(config.username, config.email)

        if sign_up_page.is_email_already_taken():
            assert True

        # TODO: continue the sign up process

    def test_write_a_tweet(self):
        home_page = self.landing_page.login(config.email, config.password)
        home_page.open_new_tweet_dialog()

        NewTweetModal(self.driver) \
            .add_message(strings.tweet_plain_text) \
            .submit()

        assert home_page.is_tweet_sent() is True

    def test_write_a_tweet_with_a_photo(self):
        home_page = self.landing_page.login(config.email, config.password)
        home_page.open_new_tweet_dialog()

        NewTweetModal(self.driver) \
            .add_message(strings.tweet_plain_text_and_photo) \
            .add_attachment('/resources/images/much-selenium.jpg') \
            .submit()

        assert home_page.is_tweet_sent() is True

    def test_write_a_tweet_with_a_link(self):
        home_page = self.landing_page.login(config.email, config.password)
        home_page.open_new_tweet_dialog()

        NewTweetModal(self.driver) \
            .add_message(strings.tweet_plain_text_and_link) \
            .add_link(strings.external_link) \
            .submit()

        assert home_page.is_tweet_sent() is True

        home_page.see_new_tweet()

        assert home_page.has_link_preview() is True


def tearDown(self):
    self.driver.quit()
