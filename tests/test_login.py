from locators import SellaBurgersLocators
from data import Data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestLogin:

    def test_login_for_button_login_in_main_page(self, driver):
        driver.find_element(*SellaBurgersLocators.LOGIN_BUTTON_IN_MAIN_PAGE).click()

        driver.find_element(*SellaBurgersLocators.LOGIN_EMAIL_FIELD).send_keys(Data.LOGIN)
        driver.find_element(*SellaBurgersLocators.LOGIN_PASSWORD_FIELD).send_keys(Data.PASSWORD)

        driver.find_element(*SellaBurgersLocators.LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(SellaBurgersLocators.PLACE_AN_ORDER_BUTTON))

        assert driver.find_element(*SellaBurgersLocators.PLACE_AN_ORDER_BUTTON).is_displayed()


    def test_login_for_account_button(self, driver):
        driver.find_element(*SellaBurgersLocators.ACCOUNT_BUTTON).click()

        driver.find_element(*SellaBurgersLocators.LOGIN_EMAIL_FIELD).send_keys(Data.LOGIN)
        driver.find_element(*SellaBurgersLocators.LOGIN_PASSWORD_FIELD).send_keys(Data.PASSWORD)

        driver.find_element(*SellaBurgersLocators.LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(SellaBurgersLocators.PLACE_AN_ORDER_BUTTON))

        assert driver.find_element(*SellaBurgersLocators.PLACE_AN_ORDER_BUTTON).is_displayed()


    def test_login_in_registration_window(self, driver):
        driver.find_element(*SellaBurgersLocators.ACCOUNT_BUTTON).click()
        driver.find_element(*SellaBurgersLocators.REGISTRATION_LINK).click()
        driver.find_element(*SellaBurgersLocators.LOGIN_LINK_IN_REGISTRATION_WINDOW).click()

        driver.find_element(*SellaBurgersLocators.LOGIN_EMAIL_FIELD).send_keys(Data.LOGIN)
        driver.find_element(*SellaBurgersLocators.LOGIN_PASSWORD_FIELD).send_keys(Data.PASSWORD)

        driver.find_element(*SellaBurgersLocators.LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(SellaBurgersLocators.PLACE_AN_ORDER_BUTTON))

        assert driver.find_element(*SellaBurgersLocators.PLACE_AN_ORDER_BUTTON).is_displayed()



    def test_login_in_forgot_password_window(self, driver):
        driver.find_element(*SellaBurgersLocators.ACCOUNT_BUTTON).click()
        driver.find_element(*SellaBurgersLocators.FORGOT_PASSWORD_LINK).click()
        driver.find_element(*SellaBurgersLocators.LOGIN_LINK_IN_FORGOT_PASSWORD_WINDOW).click()

        driver.find_element(*SellaBurgersLocators.LOGIN_EMAIL_FIELD).send_keys(Data.LOGIN)
        driver.find_element(*SellaBurgersLocators.LOGIN_PASSWORD_FIELD).send_keys(Data.PASSWORD)

        driver.find_element(*SellaBurgersLocators.LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(SellaBurgersLocators.PLACE_AN_ORDER_BUTTON))

        assert driver.find_element(*SellaBurgersLocators.PLACE_AN_ORDER_BUTTON).is_displayed()









