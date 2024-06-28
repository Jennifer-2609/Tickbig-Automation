import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
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

    @pytest.mark.sanity
    def test_login(self,setup):

        self.logger.info("********** Test_001_Login *********")
        self.logger.info("********** verifying login test *********")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.l=Login(self.driver)
        self.l.clicksignin()
        time.sleep(1)
        self.l.setUserName(self.username)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        time.sleep(1)
        self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
        act_url=self.driver.current_url

        if act_url=="http://localhost:3000/home":
            assert True
            self.logger.info("********** Login test is passed *********")
        else:
            assert False
            self.logger.info("********** Login test is failed *********")

        self.driver.close()


