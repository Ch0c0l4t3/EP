import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class ExactproMenuChecks(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"D:\webdrivers\chromedriver.exe")

    def test_menu(self):
        driver = self.driver
        self.driver.get("https://www.exactprosystems.com")

        Menu_Button_CSS               = '#showMenu'
        Menu_Dropdown_Industries_CSS = '[title="Industries"]'

        Menu_Button_Element              = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector(Menu_Button_CSS))
        Menu_Button_Element.click()
        time.sleep(1)

        Menu_Dropdown_Industries_Element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector(Menu_Dropdown_Industries_CSS))
        Menu_Dropdown_Industries_Element.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()