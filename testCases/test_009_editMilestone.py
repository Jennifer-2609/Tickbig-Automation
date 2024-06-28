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


class Test_009_EditMilestone:

    BaseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    MilestoneYear = ReadConfig.getMilestoneYear()
    MilestoneDescription = ReadConfig.getMilestoneDescription()
    MSDescriptionAtLeast = ReadConfig.getMSDescriptionAtLeast()
    MSDescriptionMaxChar = ReadConfig.getMSDescriptionMaxChar()
    InvalidYear = ReadConfig.getInvalidYear()

    @pytest.mark.sanity
    def test_editMilestonePositive(self,setup):
        # Positive Test
        self.logger.info("********** Test_009_Edit Milestone - Positive **********")
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
        self.pA.scrollEditMilestone()
        time.sleep(3)
        self.pA.clickEditMilestone()
        time.sleep(1)
        self.pA.clickAddMilestone()
        time.sleep(1)
        self.pA.textyearMilestone(self.MilestoneYear)
        time.sleep(1)
        self.pA.textMilestonedescription(self.MilestoneDescription)
        time.sleep(1)
        self.pA.clickSaveMilestone()
        time.sleep(2)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        if toast_msg:
            result = toast_msg[0].text
            self.logger.info("Toast Message: %s", result)
        else:
            self.logger.info("No toast message found")

        if result == "Milestone updated successfully.":
            assert True
            self.logger.info("********** Milestone Added Successfully and Positive Test passed *********")
        else:
            assert False
            self.logger.info("********** Milestone not Added and Positive Test failed *********")

        time.sleep(2)
        self.pA.clickEditMilestone()
        time.sleep(1)
        self.pA.clickDelMilestone()
        time.sleep(1)
        self.pA.clickDelSaveMilestone()
        time.sleep(2)

        toast_msgA = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        if toast_msgA:
            resultA = toast_msgA[0].text
            self.logger.info("Toast Message: %s", resultA)
        else:
            self.logger.info("No toast message found")

        if resultA == "Milestone updated successfully.":
            assert True
            self.logger.info("********** Milestone Deleted Successfully and Positive Test passed *********")
        else:
            assert False
            self.logger.info("********** Milestone not Deleted and Positive Test failed *********")

        self.driver.close()
        self.logger.info("********** Ending Edit Milestone Positive Test *********")


    @pytest.mark.sanity
    def test_editMilestoneNegative(self,setup):
        # Positive Test
        self.logger.info("********** Test_009_Edit Milestone - Negative **********")
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
        self.pA.scrollEditMilestone()
        time.sleep(3)
        self.pA.clickEditMilestone()
        time.sleep(1)
        self.pA.clickAddMilestone()
        time.sleep(1)
        self.pA.clickSaveMilestone()
        time.sleep(2)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/main/section/div[2]/form/div[2]/div/div[1]/div")
        if toast_msg:
            result = toast_msg[0].text
            self.logger.info("Toast Message: %s", result)
        else:
            self.logger.info("No toast message found")

        if result == "Year is required.":
            assert True
            self.logger.info("********** Year is required Negative Test passed *********")
        else:
            assert False
            self.logger.info("********** Year is required Negative Test failed *********")

        time.sleep(2)

        toast_msgA = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/main/section/div[2]/form/div[2]/div/div[2]/div")
        if toast_msgA:
            resultA = toast_msgA[0].text
            self.logger.info("Toast Message: %s", resultA)
        else:
            self.logger.info("No toast message found")

        if resultA == "Description is required.":
            assert True
            self.logger.info("********** Description is required Negative Test passed *********")
        else:
            assert False
            self.logger.info("********** Description is required Negative Test failed *********")



        time.sleep(2)
        self.pA.txtMSDescripAtLeast(self.MSDescriptionAtLeast)
        time.sleep(2)


        toast_msgB = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/main/section/div[2]/form/div[2]/div/div[2]/div")
        if toast_msgB:
            resultB = toast_msgB[0].text
            self.logger.info("Toast Message: %s", resultB)
        else:
            self.logger.info("No toast message found")

        if resultB == "Description should be at least 100 characters in length.":
            assert True
            self.logger.info("********** Milestone at least 100 characters Negative Test passed *********")
        else:
            assert False
            self.logger.info("********** Milestone at least 100 characters Negative Test failed *********")

        time.sleep(2)
        self.pA.txtMSDescripAtLeast(self.MSDescriptionMaxChar)
        time.sleep(2)

        toast_msgC = self.driver.find_elements(By.XPATH,"/html/body/div[3]/div[3]/div/div[2]/main/section/div[2]/form/div[2]/div/div[2]/div")
        if toast_msgC:
            resultC = toast_msgC[0].text
            self.logger.info("Toast Message: %s", resultC)
        else:
            self.logger.info("No toast message found")

        if resultC == "Maximum 150 characters allowed.":
            assert True
            self.logger.info("********** Milestone Maximum 150 characters Negative Test passed *********")
        else:
            assert False
            self.logger.info("********** Milestone Maximum 150 characters Negative Test failed *********")

        time.sleep(2)
        self.pA.textInvalidyr(self.InvalidYear)
        # time.sleep(1)
        # self.pA.clickSaveMilestone()
        time.sleep(2)

        toast_msgD = self.driver.find_elements(By.XPATH,"/html/body/div[3]/div[3]/div/div[2]/main/section/div[2]/form/div[2]/div/div[1]/div")
        if toast_msgD:
            resultD = toast_msgD[0].text
            self.logger.info("Toast Message: %s", resultD)
        else:
            self.logger.info("No toast message found")

        if resultD == "Invalid Year.":
            assert True
            self.logger.info("********** Invalid Year Negative Test passed *********")
        else:
            assert False
            self.logger.info("********** Invalid Year Negative Test failed *********")

        self.driver.close()
        self.logger.info("********** Ending Edit Milestone Negative Test *********")

    @pytest.mark.sanity
    def test_editMilestoneDelBin(self,setup):
        # Positive Test
        self.logger.info("********** Test_009_Edit Milestone - Delete using Bin **********")
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
        self.pA.scrollEditMilestone()
        time.sleep(3)
        self.pA.clickEditMilestone()
        time.sleep(1)
        self.pA.clickAddMilestone()
        time.sleep(1)
        self.pA.textyearMilestone(self.MilestoneYear)
        time.sleep(1)
        self.pA.textMilestonedescription(self.MilestoneDescription)
        time.sleep(1)
        self.pA.clickSaveMilestone()
        time.sleep(2)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        if toast_msg:
            result = toast_msg[0].text
            self.logger.info("Toast Message: %s", result)
        else:
            self.logger.info("No toast message found")

        if result == "Milestone updated successfully.":
            assert True
            self.logger.info("********** Milestone Added Successfully and Positive Test passed *********")
        else:
            assert False
            self.logger.info("********** Milestone not Added and Positive Test failed *********")

        time.sleep(2)
        self.pA.clickBinDelMilestone()
        time.sleep(2)

        toast_msgA = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        if toast_msgA:
            resultA = toast_msgA[0].text
            self.logger.info("Toast Message: %s", resultA)
        else:
            self.logger.info("No toast message found")

        if resultA == "Milestone deleted successfully.":
            assert True
            self.logger.info("********** Milestone Deleted Successfully using Bin Symbol  *********")
        else:
            assert False
            self.logger.info("********** Milestone Not Deleted using Bin Symbol *********")


        self.driver.close()
        self.logger.info("********** Ending Edit Milestone Delete Test *********")