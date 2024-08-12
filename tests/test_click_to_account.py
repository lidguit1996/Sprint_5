from locators import SellaBurgersLocators
from data import Data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestClickAccount:

    def test_click_account_button(self, driver):
        driver.find_element(*SellaBurgersLocators.ACCOUNT_BUTTON).click()

        driver.find_element(*SellaBurgersLocators.LOGIN_EMAIL_FIELD).send_keys(Data.LOGIN)
        driver.find_element(*SellaBurgersLocators.LOGIN_PASSWORD_FIELD).send_keys(Data.PASSWORD)
        driver.find_element(*SellaBurgersLocators.LOGIN_SUBMIT_BUTTON).click()

        driver.find_element(*SellaBurgersLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(SellaBurgersLocators.LOGAUT_BUTTON))

        assert driver.find_element(*SellaBurgersLocators.LOGAUT_BUTTON).is_displayed()




