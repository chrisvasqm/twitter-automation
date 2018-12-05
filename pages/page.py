class Page(object):

    def __init__(self, browser):
        self._browser = browser
        self._browser.implicitly_wait(10)
