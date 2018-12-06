from selenium.webdriver.common.by import By

from libraries.pagefactory_support import callable_find_by as find_by
from pages.pageobject import PageObject


class NewTweetModal(PageObject):
    _button_submit = find_by(how=By.XPATH, using="(//span[@class='buttons'])[1]/button/span[text()='Tweet']")
    _input_body = find_by(
        how=By.XPATH,
        using="//*[@id='Tweetstorm-tweet-box-0']/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]"
    )

    def __init__(self, driver):
        super(NewTweetModal, self).__init__(driver)

    def add_message(self, message: str):
        self._input_body().send_keys(message)
        return self

    def submit(self):
        self._button_submit().click()
