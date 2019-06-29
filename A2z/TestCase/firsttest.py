import unittest
from selenium import webdriver
from PageObject.Loginpage import Loginpage
class firsttest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path="C:\\Users\\RAKESH KUMAR\\Downloads\\chromedriver_win32\\chromedriver.exe")
        cls.driver.maximize_window()
    def test_01(self):
        driver=self.driver
        driver.get("https://www.a2zadwords.com") 
        callfunction=Loginpage(driver)
        
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()  