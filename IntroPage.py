import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class ExactproStartPageBasicChecks(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"D:\webdrivers\chromedriver.exe")

    def test_intro(self):
        driver = self.driver
        self.driver.get("https://www.exactprosystems.com")
        self.assertIn("Exactpro Systems - trading software testing company | Part of the LSEG", driver.title)

        EP_Button_Xpath       = "//img[contains(@alt, 'Home')]"
        EP_Slogan_Xpath       = "//*[@id='block-expro-theme-branding']/div"
        EP_Search_Xpath       = "//*[@id='showSearch']/span"
        EP_ContactUs_Xpath    = "//*[@id='block-contact-us-modal']/a/span"
        EP_Menu_Xpath         = "//*[@id='showMenu']"
        EP_WDWD_Xpath         = "//*[@id='block-exactpro-what-we-do']/div/h2"
        EP_FT_Xpath           = "//*[@id='block-exactpro-what-we-do']/div/div/div[1]/a/img[1]"
        EP_FTText_Xpath       = "//*[@id='block-exactpro-what-we-do']/div/div/div[1]/a/p"
        EP_TT_Xpath           = "//*[@id='block-exactpro-what-we-do']/div/div/div[2]/a/img[1]"
        EP_TTText_Xpath       = "//*[@id='block-exactpro-what-we-do']/div/div/div[2]/a/p"
        EP_S_Xpath            = "//*[@id='block-exactpro-what-we-do']/div/div/div[3]/a/img[1]"
        EP_SText_Xpath        = "//*[@id='block-exactpro-what-we-do']/div/div/div[3]/a/p"
        EP_ES_Xpath           = "//*[@id='block-exactpro-what-we-do']/div/div/div[4]/a/img[1]"
        EP_ESText_Xpath       = "//*[@id='block-exactpro-what-we-do']/div/div/div[4]/a/p"
        EP_NFT_Xpath          = "//*[@id='block-exactpro-what-we-do']/div/div/div[5]/a/img[1]"
        EP_NFTText_Xpath      = "//*[@id='block-exactpro-what-we-do']/div/div/div[5]/a/p"
        EP_AT_Xpath           = "//*[@id='block-exactpro-what-we-do']/div/div/div[6]/a/img[1]"
        EP_ATText_Xpath       = "//*[@id='block-exactpro-what-we-do']/div/div/div[6]/a/p"

        EP_Button_Element    = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(EP_Button_Xpath))
        EP_Slogan_Element    = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(EP_Slogan_Xpath))
        EP_Search_Element    = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(EP_Search_Xpath))
        EP_ContactUs_Element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(EP_ContactUs_Xpath))
        EP_Menu_Element      = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(EP_Menu_Xpath))
        EP_WDWD_Element      = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(EP_WDWD_Xpath))
        EP_FT_Element        = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(EP_FT_Xpath))
        EP_FTText_Element    = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(EP_FTText_Xpath))
        EP_TT_Element        = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(EP_TT_Xpath))
        EP_TTText_Element    = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(EP_TTText_Xpath))
        EP_S_Element         = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(EP_S_Xpath))
        EP_SText_Element     = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(EP_SText_Xpath))
        EP_ES_Element        = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(EP_ES_Xpath))
        EP_ESText_Element    = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(EP_ESText_Xpath))
        EP_NFT_Element       = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(EP_NFT_Xpath))
        EP_NFTText_Element   = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(EP_NFTText_Xpath))
        EP_AT_Element        = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(EP_AT_Xpath))
        EP_ATText_Element    = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(EP_ATText_Xpath))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()