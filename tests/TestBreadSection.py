from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Loсators


class TestGoToBreadSection():
    def test_Go_To_Bread_Section(self, driver):

        driver.find_element(*Loсators.BREAD_SECTION).click()
        bread = WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located((Loсators.SELECTED_SECTION)))
        assert bread.is_displayed()



