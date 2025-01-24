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


class Test_006_EditBC:

    BaseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    designation = ReadConfig.getdesdignation()
    tagline = ReadConfig.gettagline()
    summary = ReadConfig.getsummary()
    address1 = ReadConfig.getaddress1()
    address2 = ReadConfig.getaddress2()
    city = ReadConfig.getcity()
    state = ReadConfig.getstate()
    country = ReadConfig.getcountry()
    pincode = ReadConfig.getpincode()

    # @pytest.mark.sanity
    def test_editBCPositive(self,setup):
        # Positive Test
        self.logger.info("********** Test_006_EditBC - Positive **********")
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
        self.p.clickProfileicon()
        time.sleep(1)
        self.p.clickProfilepage()
        time.sleep(1)
        self.p.clickeditcard()
        time.sleep(1)
        # self.p.clickFN()
        # time.sleep(1)
        # self.p.clickLN()
        # time.sleep(1)
        self.p.setDesignation(self.designation)
        time.sleep(1)
        self.p.settagline(self.tagline)
        time.sleep(1)
        self.p.setsummary(self.summary)
        time.sleep(1)
        self.p.setaddress1(self.address1)
        time.sleep(1)
        self.p.setaddress2(self.address2)
        time.sleep(1)
        self.p.setcity(self.city)
        time.sleep(1)
        self.p.setcountry(self.country)
        time.sleep(1)
        self.p.setstate(self.state)
        time.sleep(1)
        self.p.setpincode(self.pincode)
        time.sleep(1)
        self.p.clickmob()
        time.sleep(1)
        self.p.clicksaveBC()
        time.sleep(1)

        toast_msg = self.driver.find_elements(By.XPATH,"/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = toast_msg[0].text
        print(result)

        if result=="Business Card details updated Successfully.":
            assert True
            self.logger.info("********** Edit BC Positive Test passed *********")
        else:
            assert False
            self.logger.info("********** Edit BC Positive Test failed *********")


        self.driver.close()
        self.logger.info("********** Ending Edit Business Card Positive Test *********")

    # @pytest.mark.sanity
    def test_editBCNegative(self,setup):
        # Negative Test
        self.logger.info("********** Test_006_EditBC - Negative **********")
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
        self.p.clickProfileicon()
        time.sleep(1)
        self.p.clickProfilepage()
        time.sleep(1)
        self.p.clickeditcard()
        time.sleep(1)
        self.p.clearDesignation()
        time.sleep(1)
        self.p.cleartagline()
        time.sleep(1)
        self.p.clearsummary()
        time.sleep(1)
        self.p.clearaddress1()
        time.sleep(1)
        self.p.clearaddress2()
        time.sleep(1)
        self.p.clearcity()
        time.sleep(1)
        self.p.clearcountry()
        time.sleep(1)
        self.p.clearstate()
        time.sleep(1)
        self.p.clearpincode()
        time.sleep(1)
        self.p.clicksaveBC()
        time.sleep(5)

        # designation
        toast_msgA = self.driver.find_elements(By.XPATH,"/html/body/div[3]/div[3]/div/div/form/p[1]")
        resultA = toast_msgA[0].text
        print(resultA)

        if resultA=="Designation is required.":
            assert True
            self.logger.info("********** Designation Negative Test passed *********")
        else:
            assert False
            self.logger.info("********** Designation Negative Test failed *********")

        time.sleep(5)

        # tagline
        toast_msgB = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/form/p[2]")
        resultB = toast_msgB[0].text
        print(resultB)

        if resultB == "TagLine is required.":
            assert True
            self.logger.info("********** Tagline Negative Test passed *********")
        else:
            assert False
            self.logger.info("********** Tagline Negative Test failed *********")

        time.sleep(5)

        # Summary
        toast_msgC = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/form/p[3]")
        resultC = toast_msgC[0].text
        print(resultC)

        if resultC == "Summary is required.":
            assert True
            self.logger.info("********** Summary Negative Test passed *********")
        else:
            assert False
            self.logger.info("********** Summary Negative Test failed *********")

        time.sleep(5)

        # Address1
        toast_msgD = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/form/p[4]")
        resultD = toast_msgD[0].text
        print(resultD)

        if resultD == "Address Line 1 is required.":
            assert True
            self.logger.info("********** Address Line 1 Negative Test passed *********")
        else:
            assert False
            self.logger.info("********** Address Line 1 Negative Test failed *********")

        time.sleep(5)

        # Address2
        toast_msgE = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/form/p[5]")
        resultE = toast_msgE[0].text
        print(resultE)

        if resultE == "Address Line 2 is required.":
            assert True
            self.logger.info("********** Address Line 2 Negative Test passed *********")
        else:
            assert False
            self.logger.info("********** Address Line 2 Negative Test failed *********")

        time.sleep(5)

        # City
        toast_msgF = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/form/div[11]/div[1]/p")
        resultF = toast_msgF[0].text
        print(resultF)

        if resultF == "City is required.":
            assert True
            self.logger.info("********** City Negative Test passed *********")
        else:
            assert False
            self.logger.info("********** City Negative Test failed *********")

        time.sleep(5)

        # State
        toast_msgG = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/form/div[11]/div[2]/p")
        resultG = toast_msgG[0].text
        print(resultG)

        if resultG == "state is required.":
            assert True
            self.logger.info("********** State Negative Test Test passed *********")
        else:
            assert False
            self.logger.info("********** State Negative Test failed *********")

        time.sleep(5)

        # Country
        toast_msgH = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/form/div[11]/div[3]/p")
        resultH = toast_msgH[0].text
        print(resultH)

        if resultH == "Country is required.":
            assert True
            self.logger.info("********** Country Negative Test passed *********")
        else:
            assert False
            self.logger.info("********** Country Negative Test failed *********")

        time.sleep(5)

        # Pincode
        toast_msgI = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/form/div[11]/div[4]/p")
        resultI = toast_msgI[0].text
        print(resultI)

        if resultI == "Pincode is required.":
            assert True
            self.logger.info("********** Pincode Negative Test passed *********")
        else:
            assert False
            self.logger.info("********** Pincode Negative Test failed *********")

        time.sleep(5)

        self.driver.close()
        self.logger.info("********** Ending Edit Business Card Negative Test *********")