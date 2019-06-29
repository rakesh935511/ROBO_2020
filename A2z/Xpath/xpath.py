'''
Created on Jun 21, 2019

@author: RAKESH KUMAR
'''
class xpath():
    def __init__(self,driver):
        self.driver=driver
        public start = driver.find_element_by_xpath("(//*[text()='Login'])[1]")
        UserNumber=driver.find_element_by_id("ContentPlaceHolder1_txtMobile")
        Password=driver.find_element_by_id("ContentPlaceHolder1_txtPassword")
        Login=driver.find_element_by_id("ContentPlaceHolder1_btnSubmit")
        ViewAdsNum=driver.find_element_by_xpath("//*[text()='View Ads']")
        ViewAdsNumber=driver.find_element_by_id("ContentPlaceHolder1_lblAdsViewCount")
        ViewAds=driver.find_element_by_id("ContentPlaceHolder1_rptNews_lbkRedirect_0")
        
        