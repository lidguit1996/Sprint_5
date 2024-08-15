from locators import SellaBurgersLocators
from helpers import Helpers
from data import Data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestRegistration:

    def test_registation_correct_password(self, driver):
        driver.find_element(*SellaBurgersLocators.ACCOUNT_BUTTON).click()
        driver.find_element(*SellaBurgersLocators.REGISTRATION_LINK).click()

        driver.find_element(*SellaBurgersLocators.REGISTRATION_NAME_FIELD).send_keys(Data.NAME)
        driver.find_element(*SellaBurgersLocators.REGISTRATION_EMAIL_FIELD).send_keys(Helpers.generate_email())
        driver.find_element(*SellaBurgersLocators.REGISTRATION_PASSWORD_FIELD).send_keys(Helpers.generate_password())

        driver.find_element(*SellaBurgersLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver,3).until(expected_conditions.element_to_be_clickable(SellaBurgersLocators.REGISTRATION_LINK))

        assert driver.find_element(*SellaBurgersLocators.REGISTRATION_LINK).is_displayed()


    def test_registration_incorrect_password(self,driver):
        driver.find_element(*SellaBurgersLocators.ACCOUNT_BUTTON).click()
        driver.find_element(*SellaBurgersLocators.REGISTRATION_LINK).click()

        driver.find_element(*SellaBurgersLocators.REGISTRATION_NAME_FIELD).send_keys(Data.NAME)
        driver.find_element(*SellaBurgersLocators.REGISTRATION_EMAIL_FIELD).send_keys(Helpers.generate_email())
        driver.find_element(*SellaBurgersLocators.REGISTRATION_PASSWORD_FIELD).send_keys(Data.INCORRECT_PASSWORD)
        driver.find_element(*SellaBurgersLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(SellaBurgersLocators.PASSWORD_ERROR))
        assert driver.find_element(*SellaBurgersLocators.PASSWORD_ERROR).is_displayed()
















