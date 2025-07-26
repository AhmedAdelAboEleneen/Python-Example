import os

import pytest
from playwright.sync_api import sync_playwright

PASSWORD = os.environ['PASSWORD']

# try:
#     PASSWORD = os.environ['PASSWORD']
# except KeyError:
#     import utils.secret_config
#     PASSWORD = utils.secret_config.PASSWORD

@pytest.fixture
def set_up():
    """Fixture to launch the browser and navigate to the login page"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("http://yxdemo.eastus.cloudapp.azure.com/CHECK/Demo/IA/Site/login")
        page.wait_for_load_state("networkidle")
        yield page
        browser.close()


# This method to user it in case need login every time to the browser just need to add login to test case you run
# def login_set_up(set_up):
#     page = set_up
#
#     username
#     password