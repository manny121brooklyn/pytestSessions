from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


def test_google():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://www.google.com')
    assert driver.title == 'Google'
    driver.quit()

def test_python():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://www.python.org')
    assert driver.title == 'Welcome to Python.org'
    driver.quit()

def test_facebook():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://www.fb.com')
    assert driver.title == 'Facebook - log in or sign up'
    driver.quit()

def test_instagram():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://www.instagram.com')
    assert driver.title == 'Instagram'
    driver.quit()

def test_gmail():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://www.gmail.com')
    assert driver.title == 'Gmail'
    driver.quit()
