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


class Test_003_EditQuote:

    BaseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    quote = ReadConfig.getquote()
    shortquote = ReadConfig.getshortquote()
    longquote = ReadConfig.getlongquote()

    logger = LogGen.loggen()

    # @pytest.mark.sanity
    def test_editQuotePositive(self,setup):
        # Positive Test
        self.logger.info("********** Test_003_EditQuote **********")
        self.logger.info("********** Add Quote Test Started **********")
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
        time.sleep(2)
        self.p.clickProfileicon()
        time.sleep(1)
        self.p.clickProfilepage()
        time.sleep(1)
        self.p.clickEditquote()
        time.sleep(1)
        self.p.setQuote(self.quote)
        time.sleep(1)
        self.p.clickSavequote()
        # time.sleep(1)
        # self.logger.info("*********** Quote Saved **********")

        time.sleep(1)
        error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = error_msg2[0].text
        if result == "Quote updated successfully.":
            self.logger.info("Error Message Is: %s", result)
        else:
            assert False
            self.logger.info("*************** Quote Added Test Failed  *************")


        self.driver.close()
        self.logger.info("********** Add Quote Test Ended Successfully *********")


    # @pytest.mark.sanity
    def test_editQuoteNegative1(self, setup):
        # Negative Test
        self.logger.info("********** Test_003_EditQuote **********")
        self.logger.info("********** Edit is Required Test Started **********")
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
        self.p.clickProfileicon()
        time.sleep(1)
        self.p.clickProfilepage()
        time.sleep(1)
        self.p.clickEditquote()
        time.sleep(1)
        self.p.clickEditclear()
        time.sleep(1)
        self.p.clickSavequote()
        time.sleep(2)

        toast_msg = self.driver.find_elements(By.XPATH,"/html/body/div[3]/div[3]/div/div/main/section/form/p")
        result = toast_msg[0].text
        print(result)

        if result=="Quote is required.":
            assert True
            self.logger.info("********** Edit Quote Negative test 1 passed *********")
        else:
            assert False
            self.logger.info("********** Edit Quote Negative test 1 failed *********")

        self.driver.close()
        self.logger.info("********** Edit is Required Test Ended Successfully *********")

    # @pytest.mark.sanity
    def test_editQuoteNegative2(self, setup):
        # Negative Test
        self.logger.info("********** Test_003_EditQuote **********")
        self.logger.info("********** Quote is Short Test Started **********")
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
        self.p.clickProfileicon()
        time.sleep(1)
        self.p.clickProfilepage()
        time.sleep(1)
        self.p.clickEditquote()
        time.sleep(2)
        self.p.clickEditquoteshort(self.shortquote)
        time.sleep(2)
        self.p.clickSavequote()
        time.sleep(2)

        toast_msg = self.driver.find_elements(By.XPATH,"/html/body/div[3]/div[3]/div/div/main/section/form/p")
        result = toast_msg[0].text
        print(result)

        if result=="Quote is too short.":
            assert True
            self.logger.info("********** Edit Quote Negative test 2 passed *********")
        else:
            assert False
            self.logger.info("********** Edit Quote Negative test 2 failed *********")

        self.driver.close()
        self.logger.info("********** Quote is Short Test Ended Successfully *********")

    # @pytest.mark.sanity
    def test_editQuoteNegative3(self, setup):
        # Negative Test
        self.logger.info("********** Test_003_EditQuote **********")
        self.logger.info("********** Quote is Long Test Started **********")
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
        self.p.clickProfileicon()
        time.sleep(1)
        self.p.clickProfilepage()
        time.sleep(1)
        self.p.clickEditquote()
        time.sleep(2)
        self.p.clickEditquotelong(self.longquote)
        time.sleep(2)
        self.p.clickSavequote()
        time.sleep(2)

        toast_msg = self.driver.find_elements(By.XPATH,"/html/body/div[3]/div[3]/div/div/main/section/form/p")
        result = toast_msg[0].text
        print(result)

        if result=="Quote is too long.":
            assert True
            self.logger.info("********** Edit Quote Negative test 3 passed *********")
        else:
            assert False
            self.logger.info("********** Edit Quote Negative test 3 failed *********")

        self.driver.close()
        self.logger.info("********** Quote is Long Test Ended Successfully *********")