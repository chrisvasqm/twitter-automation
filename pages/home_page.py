from selenium.webdriver.common.by import By

import strings
from libraries.pagefactory_support import callable_find_by as find_by
from pages.page import Page
from pages.sign_up_page import SignUpPage


class HomePage(Page):
    _button_sign_up = find_by(how=By.XPATH, using="//a[contains(text(), 'Sign Up')]")

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def open(self):
        self._driver.get(strings.base_url)

    def go_to_sign_up_page(self):
        self._button_sign_up().click()

        return SignUpPage(self._driver)
