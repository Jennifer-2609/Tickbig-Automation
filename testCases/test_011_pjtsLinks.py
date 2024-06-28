import configparser

import pytest
import time

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import Login
from pageObjects.Profile import profile
from pageObjects.ProfileA import profileA
from pageObjects.ProfileB import profileB
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


config=configparser.ConfigParser()
config.read('C:\\Users\\jenni\\PycharmProjects\\PythonFramework\\Configurations\\config.ini')


class Test_011_PjtsLinks:

    BaseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    projectname = ReadConfig.getprojectname()
    projectcompanyname = ReadConfig.getprojectcompanyname()
    projectlinks = ReadConfig.getprojectlinks()
    projectresponsibility = ReadConfig.getprojectresponsibility()
    projectdescription = ReadConfig.getprojectdescription()
    projectdescriptionmax = ReadConfig.getprojectdescriptionmax()
    projectdescriptionmin = ReadConfig.getprojectdescriptionmin()

    @pytest.mark.sanity
    def test_addPjtsLinksPositive(self,setup):
        # Positive Test
        self.logger.info("********** Test_011 Pjts & Links - Positive **********")
        self.driver=setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l=Login(self.driver)
        self.p = profile(self.driver)
        self.pA = profileA(self.driver)
        self.pB = profileB(self.driver)
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
        # self.pB.scrollPjtslinks()
        self.pA.scrollEduExp()
        time.sleep(3)
        self.pB.clickPjtslinks()
        time.sleep(1)
        self.pB.textPjtName(self.projectname)
        time.sleep(1)
        self.pB.textPjtCompName(self.projectcompanyname)
        time.sleep(1)
        # self.pB.textPjtlinks(self.projectlinks)
        # time.sleep(1)
        self.pB.textPjtresponsibility(self.projectresponsibility)
        time.sleep(3)
        self.pB.scrollSavepjtslinks()
        time.sleep(3)
        self.pB.textPjtdescription(self.projectdescription)
        time.sleep(1)
        self.pB.clickSavePjtslinks()
        time.sleep(2)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        if toast_msg:
            result = toast_msg[0].text
            self.logger.info("Toast Message: %s", result)
        else:
            self.logger.info("No toast message found")

        if result == "Profile Projects updated successfully.":
            assert True
            self.logger.info("********** Profile Projects Added successfully Test passed *********")
        else:
            assert False
            self.logger.info("********** Profile Projects Added successfully Test failed *********")

        time.sleep(2)
        self.pB.mousehoverpjtlinkcardEdit()
        # self.pB.clickeditPjtslinks()
        time.sleep(1)
        self.pB.textPjtlinks(self.projectlinks)
        time.sleep(1)
        self.pB.clickeditSavePjtslinks()
        time.sleep(2)

        toast_msgA = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        if toast_msgA:
            resultA = toast_msgA[0].text
            self.logger.info("Toast Message: %s", resultA)
        else:
            self.logger.info("No toast message found")

        if resultA == "Profile Project edited successfully.":
            assert True
            self.logger.info("********** Profile Project edited successfully Test passed *********")
        else:
            assert False
            self.logger.info("********** Profile Project edited successfully Test failed *********")

        time.sleep(2)
        self.pB.clickpjtweblink()
        time.sleep(1)
        self.logger.info("********** Project Weblink clicked successfully **********")
        time.sleep(2)
        self.pB.mousehoverpjtlinkcardDel()
        time.sleep(2)

        toast_msgB = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        if toast_msgB:
            resultB = toast_msgB[0].text
            self.logger.info("Toast Message: %s", resultB)
        else:
            self.logger.info("No toast message found")

        if resultB == "Profile Projects deleted successfully.":
            assert True
            self.logger.info("********** Profile Projects deleted successfully Test passed *********")
        else:
            assert False
            self.logger.info("********** Profile Projects deleted successfully Test failed *********")

        self.driver.close()
        self.logger.info("********** Ending Edit Pjts & Links Positive Test *********")

    @pytest.mark.sanity
    def test_addPjtsLinksNegative(self, setup):
            # Negative Test
            self.logger.info("********** Test_011 Pjts & Links - Positive **********")
            self.driver = setup
            self.driver.get(self.BaseURL)
            self.driver.maximize_window()
            self.l = Login(self.driver)
            self.p = profile(self.driver)
            self.pA = profileA(self.driver)
            self.pB = profileB(self.driver)
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
            # self.pB.scrollPjtslinks()
            self.pA.scrollEduExp()
            time.sleep(3)
            self.pB.clickPjtslinks()
            time.sleep(3)
            self.pB.scrollSavepjtslinks()
            time.sleep(3)
            self.pB.clickSavePjtslinks()
            time.sleep(2)

            toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/main/section/div[2]/form/div[1]/div[1]/p")
            if toast_msg:
                result = toast_msg[0].text
                self.logger.info("Toast Message: %s", result)
            else:
                self.logger.info("No toast message found")

            if result == "Project Name is required.":
                assert True
                self.logger.info("********** Project Name is required Negative Test passed *********")
            else:
                assert False
                self.logger.info("********** Project Name is required Negative Test failed *********")

            time.sleep(2)

            toast_msgA = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/main/section/div[2]/form/div[1]/div[2]/p")
            if toast_msgA:
                resultA = toast_msgA[0].text
                self.logger.info("Toast Message: %s", resultA)
            else:
                self.logger.info("No toast message found")

            if resultA == "Company Name is required.":
                assert True
                self.logger.info("********** Company Name is required Negative Test passed *********")
            else:
                assert False
                self.logger.info("********** Company Name is required Negative Test failed *********")

            time.sleep(2)

            toast_msgB = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/main/section/div[2]/form/div[1]/div[5]/p")
            if toast_msgB:
                resultB = toast_msgB[0].text
                self.logger.info("Toast Message: %s", resultB)
            else:
                self.logger.info("No toast message found")

            if resultB == "Description is required.":
                assert True
                self.logger.info("********** Description is required Negative Test passed *********")
            else:
                assert False
                self.logger.info("********** Description is required Negative Test failed *********")

            time.sleep(2)
            self.pB.textPjtdescriptionmin(self.projectdescriptionmin)
            time.sleep(2)

            toast_msgC = self.driver.find_elements(By.XPATH,"/html/body/div[3]/div[3]/main/section/div[2]/form/div[1]/div[5]/p")
            if toast_msgC:
                resultC = toast_msgC[0].text
                self.logger.info("Toast Message: %s", resultC)
            else:
                self.logger.info("No toast message found")

            if resultC == "Minimum 180 characters allowed.":
                assert True
                self.logger.info("********** Minimum 180 characters allowed Negative Test passed *********")
            else:
                assert False
                self.logger.info("********** Minimum 180 characters allowed Negative Test failed *********")

            time.sleep(2)
            self.pB.textPjtdescriptionmax(self.projectdescriptionmax)
            time.sleep(2)

            toast_msgD = self.driver.find_elements(By.XPATH,"/html/body/div[3]/div[3]/main/section/div[2]/form/div[1]/div[5]/p")
            if toast_msgD:
                resultD = toast_msgD[0].text
                self.logger.info("Toast Message: %s", resultD)
            else:
                self.logger.info("No toast message found")

            if resultD == "Maximum 360 characters allowed.":
                assert True
                self.logger.info("********** Maximum 360 characters allowed Negative Test passed *********")
            else:
                assert False
                self.logger.info("********** Maximum 360 characters allowed Negative Test failed *********")



            self.driver.close()
            self.logger.info("********** Ending Edit Pjts & Links Positive Test *********")