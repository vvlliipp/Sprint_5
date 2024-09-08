from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Loсators
from helpers import get_sign_up_data
class TestSuccessfulRegistration():
    def test_successful_registration(self, driver):
        name_data, email_data, password_data = get_sign_up_data()
        driver.find_element(*Loсators.LOGIN_BUTTON).click()
        driver.find_element(*Loсators.REGISTRATION_BUTTON).click()

        driver.find_element(*Loсators.NAME_FIELD).send_keys(name_data)
        driver.find_element(*Loсators.EMAIL_FIELD).send_keys(email_data)
        driver.find_element(*Loсators.PASSWORD_FIELD).send_keys(password_data)

        driver.find_element(*Loсators.REGISTR_BUTTON).click()
        sign_button_registration_form = WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located((Loсators.SIGN_BUTTON_REGISTRATION_FORM)))
        assert sign_button_registration_form.is_displayed()


