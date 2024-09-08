from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Loсators
from helpers import get_sign_up_data

class TestGoToBreadSection():
    def test_Go_To_Bread_Section(self, driver):
        email_data, password_data = get_sign_up_data()
        driver.find_element(*Loсators.LOGIN_BUTTON).click()

        driver.find_element(*Loсators.EMAIL_FIELD).send_keys(email_data)
        driver.find_element(*Loсators.PASSWORD_FIELD).send_keys(password_data)
        driver.find_element(*Loсators.SIGN_BUTTON_REGISTRATION_FORM).click()

        driver.find_element(*Loсators.BREAD_SECTION).click()
        bread = WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located((Loсators.BREAD)))
        assert bread.is_displayed()



