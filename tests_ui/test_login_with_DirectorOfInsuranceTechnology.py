import os

import pytest

import utils.secert_config
from pom.login_page import LoginPage

@pytest.mark.regression
def test_login_director(set_up):
    page = set_up
    login_page = LoginPage(page)
    page.wait_for_load_state("networkidle")
    login_page.login("DirectorOfInsuranceTechnology", os.environ["PASSWORD"])

