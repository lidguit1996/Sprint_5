from locators import SellaBurgersLocators
from data import Data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestLogaut:

    def test_logaut_from_account(self, driver):
        driver.find_element(*SellaBurgersLocators.ACCOUNT_BUTTON).click()

        driver.find_element(*SellaBurgersLocators.LOGIN_EMAIL_FIELD).send_keys(Data.LOGIN)
        driver.find_element(*SellaBurgersLocators.LOGIN_PASSWORD_FIELD).send_keys(Data.PASSWORD)
        driver.find_element(*SellaBurgersLocators.LOGIN_SUBMIT_BUTTON).click()

        driver.find_element(*SellaBurgersLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(SellaBurgersLocators.LOGAUT_BUTTON))

        driver.find_element(*SellaBurgersLocators.LOGAUT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(SellaBurgersLocators.REGISTRATION_LINK))

        assert driver.find_element(*SellaBurgersLocators.REGISTRATION_LINK).is_displayed()





