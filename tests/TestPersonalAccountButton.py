from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Loсators
from helpers import get_sign_up_data

class TestLoginPersonalAccountButton():
    def test_login_personal_account_button(self, driver):
        email_data, password_data = get_sign_up_data()

        driver.find_element(*Loсators.PERSONAL_ACCOUNT).click()
        driver.find_element(*Loсators.EMAIL_FIELD).send_keys(email_data)
        driver.find_element(*Loсators.PASSWORD_FIELD).send_keys(password_data)
        driver.find_element(*Loсators.SIGN_BUTTON_REGISTRATION_FORM)
        place_on_order_button = WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located((Loсators.PLACE_ON_ORDER_BUTTON)))
        assert place_on_order_button.is_displayed()