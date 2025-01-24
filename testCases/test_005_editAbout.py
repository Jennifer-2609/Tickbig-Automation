import configparser

import pytest
import time

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import Login
from pageObjects.Profile import profile
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


config=configparser.ConfigParser()
config.read('C:\\Users\\jenni\\PycharmProjects\\PythonFramework\\Configurations\\config.ini')


class Test_005_EditAbout:

    BaseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    aboutdescriptionneg = ReadConfig.getaboutdescriptionneg()

    logger = LogGen.loggen()

    # @pytest.mark.sanity
    def test_editAboutPositive(self,setup):
        # Positive Test
        self.logger.info("********** Test_005_EditAbout **********")
        self.driver=setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l=Login(self.driver)
        self.p = profile(self.driver)
        self.l.clicksignin()
        time.sleep(1)
        self.l.setUserName(self.username)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        time.sleep(1)
        self.driver.refresh()
        time.sleep(3)
        self.p.clickProfileicon()
        time.sleep(1)
        self.p.clickProfilepage()
        time.sleep(1)
        self.p.clickEditAbout()
        time.sleep(1)
        self.p.clickOpenWork()
        time.sleep(1)
        self.p.clickRaisingFund()
        time.sleep(1)
        self.p.clickOpenInvest()
        time.sleep(5)
        self.p.clickOpenConsult()
        time.sleep(5)
        self.p.clickHiring()
        time.sleep(6)
        self.p.clickDescriptionclear()
        time.sleep(3)
        self.p.clickDescription()
        time.sleep(6)
        self.p.scrollSave()
        time.sleep(3)
        self.p.clickSave()

        # self.logger.info("*********** About Me Saved **********")

        time.sleep(1)
        toast_msg = self.driver.find_elements(By.XPATH,"/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = toast_msg[0].text
        print(result)

        if result=="About updated successfully.":
            assert True
            self.logger.info("********** Edit About Positive test passed *********")
        else:
            assert False
            self.logger.info("********** Edit About Positive test failed *********")

        self.driver.close()
        self.logger.info("********** Ending Edit About Test *********")

    # @pytest.mark.sanity
    def test_editAboutNegative(self,setup):
        # Negative Test
        self.logger.info("********** Test_005_EditAbout **********")
        self.driver=setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l=Login(self.driver)
        self.p = profile(self.driver)
        self.l.clicksignin()
        time.sleep(1)
        self.l.setUserName(self.username)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        time.sleep(1)
        self.driver.refresh()
        time.sleep(3)
        self.p.clickProfileicon()
        time.sleep(1)
        self.p.clickProfilepage()
        time.sleep(1)
        self.p.clickEditAbout()
        time.sleep(5)
        self.p.clickDescription()
        time.sleep(5)
        self.p.clickDescriptionclear()
        time.sleep(5)
        self.p.scrollSave()
        time.sleep(3)
        self.p.clickSave()

        time.sleep(2)
        toast_msg = self.driver.find_elements(By.XPATH,"/html/body/div[3]/div[3]/main/section/div[2]/form[2]/div[3]/p")
        result = toast_msg[0].text
        print(result)

        if result=="Description is required.":
            assert True
            self.logger.info("********** Edit About Negative test passed *********")
        else:
            assert False
            self.logger.info("********** Edit About Negative test failed *********")

        self.driver.close()
        self.logger.info("********** Ending Edit About Test *********")

    # @pytest.mark.sanity
    def test_editAboutPositive2(self,setup):
        # Positive Test - upload document
        self.logger.info("********** Test_005_EditAbout **********")
        self.driver=setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l=Login(self.driver)
        self.p = profile(self.driver)
        self.l.clicksignin()
        time.sleep(1)
        self.l.setUserName(self.username)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        time.sleep(1)
        self.driver.refresh()
        time.sleep(3)
        self.p.clickProfileicon()
        time.sleep(1)
        self.p.clickProfilepage()
        time.sleep(1)
        self.p.clickEditAbout()
        time.sleep(2)
        self.p.uploadResume()
        time.sleep(2)
        self.p.clickRessave()
        time.sleep(2)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = toast_msg[0].text
        print(result)

        if result == "Resume uploaded successfully.":
            assert True
            self.logger.info("********** Resume upload test passed *********")
        else:
            assert False
            self.logger.info("********** Resume upload test failed *********")

        self.logger.info("********** Resume upload Done *********")


        self.driver.close()
        self.logger.info("********** Ending Edit About - Resume Upload Test *********")

    # @pytest.mark.sanity
    def test_editAboutNegative2(self, setup):
        # Negative Test
        self.logger.info("********** Test_005_EditAbout Negative Test **********")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.p = profile(self.driver)
        self.l.clicksignin()
        time.sleep(1)
        self.l.setUserName(self.username)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        time.sleep(1)
        self.driver.refresh()
        time.sleep(3)
        self.p.clickProfileicon()
        time.sleep(1)
        self.p.clickProfilepage()
        time.sleep(1)
        self.p.clickEditAbout()
        # time.sleep(1)
        # self.p.clickOpenWork()
        # time.sleep(1)
        # self.p.clickRaisingFund()
        # time.sleep(1)
        # self.p.clickOpenInvest()
        # time.sleep(5)
        # self.p.clickOpenConsult()
        # time.sleep(5)
        # self.p.clickHiring()
        time.sleep(5)
        self.p.clickDescriptionclear()
        time.sleep(5)
        self.p.clickDescriptionneg(self.aboutdescriptionneg)
        time.sleep(5)
        self.p.scrollSave()
        time.sleep(3)
        self.p.clickSave()

        time.sleep(2)
        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/main/section/div[2]/form[2]/div[3]/p")
        result = toast_msg[0].text
        print(result)

        if result == "Maximum 500 characters allowed.":
            assert True
            self.logger.info("********** Edit About - Maximum 500 characters allowed Negative test passed *********")
        else:
            assert False
            self.logger.info("********** Edit About - Maximum 500 characters allowed Negative test failed *********")


        self.driver.close()
        self.logger.info("********** Ending Edit About Test *********")