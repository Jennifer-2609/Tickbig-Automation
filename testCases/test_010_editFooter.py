import configparser

import pytest
import time

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import Login
from pageObjects.Profile import profile
from pageObjects.ProfileA import profileA
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


config=configparser.ConfigParser()
config.read('C:\\Users\\jenni\\PycharmProjects\\PythonFramework\\Configurations\\config.ini')


class Test_010_EditFooter:

    BaseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()



    # @pytest.mark.sanity
    def test_editFooterPositive(self,setup):
        # Positive Test
        self.logger.info("********** Test_009_Edit Footer - Positive **********")
        self.driver=setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l=Login(self.driver)
        self.p = profile(self.driver)
        self.pA = profileA(self.driver)
        self.l.clicksignin()
        time.sleep(1)
        self.l.setUserName(self.username)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        time.sleep(1)
        self.p.clickProfileicon()
        time.sleep(1)
        self.p.clickProfilepage()
        time.sleep(3)
        self.pA.scrollEditfooter()
        time.sleep(3)
        self.pA.clickEditfooter()
        time.sleep(1)
        self.pA.txtFB()
        time.sleep(1)
        self.pA.txtTwitter()
        time.sleep(1)
        self.pA.txtInsta()
        time.sleep(1)
        self.pA.txtLinkedIn()
        time.sleep(1)
        self.pA.txtWebsite()
        time.sleep(1)
        self.pA.clickSavefooter()
        time.sleep(1)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        if toast_msg:
            result = toast_msg[0].text
            self.logger.info("Toast Message: %s", result)
        else:
            self.logger.info("No toast message found")

        if result == "Social Media Links updated successfully.":
            assert True
            self.logger.info("********** Social Media Link Added Successfully Test passed *********")
        else:
            assert False
            self.logger.info("********** Social Media Link Added Successfully Test failed *********")



        self.driver.close()
        self.logger.info("********** Ending Edit Footer Positive Test *********")


    # @pytest.mark.sanity
    def test_editFooterCheck(self,setup):
        # Positive Test
        self.logger.info("********** Test_009_Edit Footer - Check **********")
        self.driver=setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l=Login(self.driver)
        self.p = profile(self.driver)
        self.pA = profileA(self.driver)
        self.l.clicksignin()
        time.sleep(1)
        self.l.setUserName(self.username)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        time.sleep(1)
        self.p.clickProfileicon()
        time.sleep(1)
        self.p.clickProfilepage()
        time.sleep(3)
        self.pA.scrollEditfooter()
        time.sleep(3)
        self.pA.clickTwitterlink()
        time.sleep(10)
        self.pA.clickFBlink()
        time.sleep(10)
        self.pA.clickLinkedinlink()
        time.sleep(10)
        self.pA.clickInstalink()
        time.sleep(10)
        self.pA.clickWebsitelink()
        time.sleep(10)


        self.driver.close()
        self.logger.info("********** Ending Edit Footer Check *********")