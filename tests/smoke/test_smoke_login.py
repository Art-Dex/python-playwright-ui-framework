import pytest

@pytest.mark.smoke
def test_open_login_page(page):
    page.goto("https://www.saucedemo.com/")
    assert page.title() == "Swag Labs"