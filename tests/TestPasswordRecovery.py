from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Loсators
from helpers import get_sign_up_data

class TestLogInPasswordRecovery():
    def test_log_in_password_recovery(self, driver):
        email_data, password_data = get_sign_up_data()

        driver.find_element(*Loсators.LOGIN_BUTTON).click()
        driver.find_element(*Loсators.RECOVERY_PASSWORD).click()
        driver.find_element(*Loсators.TEXT_LINK_TO_LOG_IN).click()

        driver.find_element(*Loсators.EMAIL_FIELD).send_keys(email_data)
        driver.find_element(*Loсators.PASSWORD_FIELD).send_keys(password_data)

        driver.find_element(*Loсators.SIGN_BUTTON_REGISTRATION_FORM).click()
        place_on_order_button = WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located((Loсators.PLACE_ON_ORDER_BUTTON)))
        assert place_on_order_button.is_displayed()


