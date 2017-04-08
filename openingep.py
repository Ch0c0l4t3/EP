import unittest
from selenium import webdriver

class ExactproStartPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"D:\webdrivers\chromedriver.exe")

    def test(self):
        driver = self.driver
        driver.get("https://www.exactprosystems.com/")
        self.assertIn("Exactpro Systems - trading software testing company | Part of the LSEG", driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()