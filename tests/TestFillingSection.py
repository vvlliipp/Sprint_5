from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Loсators
from helpers import get_sign_up_data

class TestGoToFillingSection():
    def test_Go_To_Filling_Section(self, driver):

        driver.find_element(*Loсators.FILLING_SECTION).click()
        filling = WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located((Loсators.SELECTED_SECTION)))
        assert filling.is_displayed()



