import pytest
from selenium import webdriver
from data import Data

@pytest.fixture(scope='function')
def driver():
    chromedriver = webdriver.Chrome()
    chromedriver.get(Data.SBURGERS_URL)
    yield chromedriver
    chromedriver.quit()

