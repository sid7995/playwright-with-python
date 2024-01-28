# conftest.py
import pytest
from playwright.sync_api import sync_playwright

from config.config import BROWSER_TYPE, HEADLESS_MODE
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from utils.plywright_utils import PlaywrightUtils


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        if BROWSER_TYPE == "chromium":
            browser = p.chromium.launch(headless=HEADLESS_MODE)
        elif BROWSER_TYPE == "firefox":
            browser = p.firefox.launch(headless=HEADLESS_MODE)
        elif BROWSER_TYPE == "webkit":
            browser = p.webkit.launch(headless=HEADLESS_MODE)
        else:
            raise ValueError(f"Invalid BROWSER_TYPE: {BROWSER_TYPE}")

        yield browser
        browser.close()



@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


@pytest.fixture(scope="function")
def login_page(page):
    return LoginPage(page)


@pytest.fixture(scope="function")
def home_page(page):
    return HomePage(page)


@pytest.fixture(scope="function")
def common_actions(page):
    return PlaywrightUtils(page)
