from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Loсators


class TestGoToSaucesSection():
    def test_Go_To_Sauces_Section(self, driver):

        driver.find_element(*Loсators.SAUCES_SECTION).click()
        sauces = WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located((Loсators.SELECTED_SECTION)))
        assert sauces.is_displayed()



