import pytest
from selene.support.shared import browser
from utils.base_session import demoshop


@pytest.fixture(scope='session')
def register():
    browser.config.base_url = "https://demowebshop.tricentis.com/"
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    response = demoshop.post('/login', data={'Email': 'neeiraaa@gmail.com', 'Password': 'neeiraaa'}, allow_redirects=False)
    authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    browser.open("Themes/DefaultClean/Content/images/logo.png")

    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": authorization_cookie})

    return browser
