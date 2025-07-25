import pytest
from playwright.sync_api import Playwright

@pytest.fixture
def set_up(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto("http://yxdemo.eastus.cloudapp.azure.com/CHECK/Demo/IA/Site/login")

    yield page



# This method to user it in case need login every time to the browser just need to add login to test case you run
# def login_set_up(set_up):
#     page = set_up
#
#     username
#     password