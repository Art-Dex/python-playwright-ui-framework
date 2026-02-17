import pytest
from pages.login_page import LoginPage


@pytest.mark.smoke
def test_open_login_page(page):
    login_page = LoginPage(page)
    login_page.open("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    assert page.url.endswith("inventory.html")
