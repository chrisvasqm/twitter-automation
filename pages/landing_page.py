from selenium.webdriver.common.by import By

import strings
from libraries.pagefactory_support import callable_find_by as find_by
from pages.home_page import HomePage
from pages.page import Page
from pages.sign_up_page import SignUpPage


class LandingPage(Page):
    _button_sign_up = find_by(how=By.XPATH, using="//a[contains(text(), 'Sign Up')]")
    _input_email = find_by(how=By.XPATH, using="(//input[@autocomplete='username'])[1]")
    _input_password = find_by(how=By.XPATH, using="(//input[@autocomplete='current-password'])[1]")
    _button_login = find_by(how=By.XPATH, using="(//input[@value='Log in'])[1]")

    def __init__(self, driver):
        super(LandingPage, self).__init__(driver)

    def open(self):
        self._driver.get(strings.twitter_url)

    def go_to_sign_up_page(self):
        self._button_sign_up().click()

        return SignUpPage(self._driver)

    def login(self, email, password):
        self._input_email().send_keys(email)
        self._input_password().send_keys(password)
        self._button_login().click()

        return HomePage(self._driver)
