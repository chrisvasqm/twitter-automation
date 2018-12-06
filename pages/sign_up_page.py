from selenium.webdriver.common.by import By

from libraries.pagefactory_support import callable_find_by as find_by
from pages.page import Page


class SignUpPage(Page):
    _toggle_sign_up_type = find_by(how=By.XPATH, using="//div[contains(text(), 'Use ')]")
    _input_name = find_by(how=By.NAME, using="name")
    _input_email = find_by(how=By.NAME, using="email")
    _error_email_already_taken = find_by(how=By.XPATH, using="//div[text()='Email has already been taken.']")

    def __init__(self, driver):
        super(SignUpPage, self).__init__(driver)

    def sign_up_by_email(self, name, email):
        self._toggle_sign_up_type().click()
        self._input_name().send_keys(name)
        self._input_email().send_keys(email)

    def is_email_already_taken(self):
        return self._error_email_already_taken().is_displayed()
