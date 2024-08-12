from locators import SellaBurgersLocators
from data import Data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestConstructor:

    def test_constructor_sauces(self, driver):
        driver.find_element(*SellaBurgersLocators.ACCOUNT_BUTTON).click()

        driver.find_element(*SellaBurgersLocators.LOGIN_EMAIL_FIELD).send_keys(Data.LOGIN)
        driver.find_element(*SellaBurgersLocators.LOGIN_PASSWORD_FIELD).send_keys(Data.PASSWORD)

        driver.find_element(*SellaBurgersLocators.LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(SellaBurgersLocators.SAUCES_LIST))

        sauces_list = driver.find_element(*SellaBurgersLocators.SAUCES_LIST)
        driver.execute_script("arguments[0].scrollIntoView();", sauces_list)
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(SellaBurgersLocators.GALACTIC_SAUCE))

        assert driver.find_element(*SellaBurgersLocators.GALACTIC_SAUCE).is_displayed()


    def test_constructor_toppings(selfs, driver):
        driver.find_element(*SellaBurgersLocators.ACCOUNT_BUTTON).click()

        driver.find_element(*SellaBurgersLocators.LOGIN_EMAIL_FIELD).send_keys(Data.LOGIN)
        driver.find_element(*SellaBurgersLocators.LOGIN_PASSWORD_FIELD).send_keys(Data.PASSWORD)

        driver.find_element(*SellaBurgersLocators.LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(SellaBurgersLocators.SAUCES_LIST))

        toppings_list = driver.find_element(*SellaBurgersLocators.TOPPINGS_LIST)
        driver.execute_script("arguments[0].scrollIntoView();", toppings_list)
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(SellaBurgersLocators.BEAF_METEOR))

        assert driver.find_element(*SellaBurgersLocators.BEAF_METEOR).is_displayed()

    def test_constructor_bread(selfs, driver):
        driver.find_element(*SellaBurgersLocators.ACCOUNT_BUTTON).click()

        driver.find_element(*SellaBurgersLocators.LOGIN_EMAIL_FIELD).send_keys(Data.LOGIN)
        driver.find_element(*SellaBurgersLocators.LOGIN_PASSWORD_FIELD).send_keys(Data.PASSWORD)

        driver.find_element(*SellaBurgersLocators.LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(SellaBurgersLocators.SAUCES_LIST))

        toppings_list = driver.find_element(*SellaBurgersLocators.TOPPINGS_LIST)
        driver.execute_script("arguments[0].scrollIntoView();", toppings_list)
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(SellaBurgersLocators.BEAF_METEOR))

        bread_list = driver.find_element(*SellaBurgersLocators.BREAD_LIST)
        driver.execute_script("arguments[0].scrollIntoView();", bread_list)
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(SellaBurgersLocators.CRATER_BREAD))

        assert driver.find_element(*SellaBurgersLocators.CRATER_BREAD).is_displayed()













