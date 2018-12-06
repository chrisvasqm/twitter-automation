from selenium.webdriver.common.by import By

from libraries.pagefactory_support import callable_find_by as find_by
from pages.pageobject import PageObject


class HomePage(PageObject):
    _button_tweet = find_by(how=By.ID, using="global-new-tweet-button")
    _message_tweet_sent = find_by(how=By.XPATH, using="//span[text()='Your Tweet was sent.']")
    _message_tweet_already_sent = find_by(how=By.XPATH, using="//span[text()='You have already sent this Tweet.']")

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def open_new_tweet_dialog(self):
        self._button_tweet().click()

    def is_tweet_sent(self):
        return self._message_tweet_sent().is_displayed()
