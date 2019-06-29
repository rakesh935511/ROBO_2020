

class Loginpage():
    def __init__(self,driver):
        self.driver=driver
        self.signin_button_id="a-autoid-0-announce"
        self.start_button="(//*[text()='Login'])[1]"
        self.UserNumber_id="ContentPlaceHolder1_txtMobile"
        self.password="ContentPlaceHolder1_txtPassword"
        self.log="ContentPlaceHolder1_btnSubmit"
        self.ViewAdsNum="//*[text()='View Ads']"
        self.ViewAdsNumber="ContentPlaceHolder1_lblAdsViewCount"
        self.ViewAds="ContentPlaceHolder1_rptNews_lbkRedirect_0"
    def LoginUser(self): 
        self.driver.find_element_by_xpath(signin_button_id).click()
        self.driver.find_element_by_id(UserNumber_id).click()
        