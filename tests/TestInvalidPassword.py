from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Loсators

class TestInvalidPassword:
    def test_invalid_password(self, driver):
        driver.find_element(*Loсators.LOGIN_BUTTON).click()
        driver.find_element(*Loсators.PASSWORD_FIELD).send_keys('12345')
        driver.find_element(*Loсators.SIGN_BUTTON_REGISTRATION_FORM).click()
        invalid_password = WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located((Loсators.INVALID_PASSWORD)))
        assert invalid_password.is_displayed()
