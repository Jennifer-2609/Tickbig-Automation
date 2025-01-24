import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import Login
from pageObjects.applyproject import applyproject
from pageObjects.readProperties import ReadConfig
from pageObjects.customLogger import LogGen
import configparser

config=configparser.ConfigParser()
config.read('C:\\Users\\jenni\\PycharmProjects\\PythonFramework\\Configurations\\config.ini')
# username = config.get('settings','BaseUrl')
# print(username)

class Test_000_Login:

    BaseURL= ReadConfig.getApplicationURL()
    username= ReadConfig.getUseremail()
    password= ReadConfig.getPassword()

    logger = LogGen.loggen()

    # @pytest.mark.sanity
    def test_loginandlogout(self,setup):

        self.logger.info("********** Test_001_Login and Logout *********")
        self.logger.info("********** verifying login and logout test *********")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.l=Login(self.driver)
        self.ap = applyproject(self.driver)
        self.l.clicksignin()
        time.sleep(1)
        self.l.setUserName(self.username)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        time.sleep(1)
        # self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
        # time.sleep(1)

        error_msg8 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = error_msg8[0].text
        if result == "Logged In successfully":
            self.logger.info("Error Message Is: %s", result)
        else:
            assert False
            self.logger.info("***************  Logged In successfully Failed   *************")

        self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
        time.sleep(2)
        self.ap.clickprofilenavbardroparrow()
        time.sleep(2)
        self.l.clickLogout()
        time.sleep(2)
        self.l.clickLogoutYes()
        time.sleep(2)
        act_url = self.driver.current_url
        print(act_url)
        exp_url="https://www.tickbig.com/signin"

        if act_url == exp_url:
            assert True
            self.logger.info("***************  Logged Out successfully Passed   *************")
        else:
            assert False
            self.logger.info("***************  Logged Out successfully Failed   *************")


        self.driver.close()
        self.logger.info("************** Login and Logout Test Ended Successfully *************")

