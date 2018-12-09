import time

from selenium.webdriver.common.by import By

from libraries.pagefactory_support import callable_find_by as find_by
from pages.pageobject import PageObject


class HomePage(PageObject):
    _button_tweet = find_by(how=By.ID, using="global-new-tweet-button")
    _message_tweet_sent = find_by(how=By.XPATH, using="//span[text()='Your Tweet was sent.']")
    _message_tweet_already_sent = find_by(how=By.XPATH, using="//span[text()='You have already sent this Tweet.']")
    _button_see_new_tweet = find_by(how=By.XPATH, using="//button[contains(text(), 'See 1 new Tweet')]")
    _tweet_link_preview = find_by(how=By.XPATH, using="//h2[contains(text(), 'Just Syntactic Sugar')]")
    _iframe = find_by(how=By.XPATH, using="//iframe[contains(@id, 'xdm_default')]")

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def open_new_tweet_dialog(self):
        self._button_tweet().click()

    def is_tweet_sent(self):
        return self._message_tweet_sent().is_displayed()

    def see_new_tweet(self):
        new_tweet = self._button_see_new_tweet()
        # To wait for the button animation to finish
        time.sleep(2)
        new_tweet.click()

    def has_link_preview(self):
        self._driver.switch_to.frame(self._iframe())
        preview = self._tweet_link_preview()
        has_link = preview.is_displayed()
        self._driver.switch_to.default_content()
        return has_link
