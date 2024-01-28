# pages.py
from utils.plywright_utils import PlaywrightUtils


class LoginPage(PlaywrightUtils):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

    def navigate_to_login(self):
        self.page.goto("https://example.com/login")

    def login(self, username, password):
        self.take_screenshot("screenshots/screenshot_after_login.png")

    # Add other methods as needed