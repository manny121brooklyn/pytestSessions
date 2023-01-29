from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

driver = None
@pytest.fixture(scope='module')
def init_driver():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get('https://www.google.com')

    yield
    driver.quit()

# we have two test cases
# 1
def test_google_title(init_driver):
    assert driver.title == 'Google'

# 2

def test_google_url(init_driver):
    assert driver.current_url == 'https://www.google.com/'

