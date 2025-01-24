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


class Test_008_EditAchievement:

    BaseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    AchieveTitle = ReadConfig.getAchieveTitle()
    AchieveDescription = ReadConfig.getAchieveDescription()
    AchieveDescriptionnew = ReadConfig.getAchieveDescriptionnew()
    AchieveDescriptionmax = ReadConfig.getAchieveDescriptionmax()


    # @pytest.mark.sanity
    def test_editAchievementPositive(self,setup):
        # Positive Test
        self.logger.info("********** Test_008_Edit Achievement - Positive **********")
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
        # self.pA.scrollAchieve()
        self.pB.scrollPjtslinks()
        time.sleep(3)
        self.pA.clickEditachieve()
        time.sleep(1)
        self.pA.clickAddachieve()
        time.sleep(1)
        self.pA.textAchievetitle(self.AchieveTitle)
        time.sleep(1)
        self.pA.textAchievedescription(self.AchieveDescription)
        time.sleep(1)
        self.pA.clickAchievesubmit()
        time.sleep(1)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        if toast_msg:
            result = toast_msg[0].text
            self.logger.info("Toast Message: %s", result)
        else:
            self.logger.info("No toast message found")

        if result == "Achievement updated successfully.":
            assert True
            self.logger.info("********** Achievement Added Successfully and Positive Test passed *********")
        else:
            assert False
            self.logger.info("********** Achievement not Added and Positive Test failed *********")

        time.sleep(2)
        self.pA.clickEditachieve()
        time.sleep(1)
        self.pA.clickAchieveDel()
        time.sleep(1)
        self.pA.clickAchieveDelSubmit()
        time.sleep(1)

        toast_msgA = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        if toast_msgA:
            resultA = toast_msgA[0].text
            self.logger.info("Toast Message: %s", resultA)
        else:
            self.logger.info("No toast message found")

        if result == "Achievement updated successfully.":
            assert True
            self.logger.info("********** Achievement Deleted Successfully and Positive Test passed *********")
        else:
            assert False
            self.logger.info("********** Achievement not Deleted and Positive Test failed *********")


        self.driver.close()
        self.logger.info("********** Ending Edit Achievement Positive Test *********")


    # @pytest.mark.sanity
    def test_editAchievementNegative(self, setup):
            # Negative Test
            self.logger.info("********** Test_008_Edit Achievement - Negative **********")
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
            # self.pA.scrollAchieve()
            self.pB.scrollPjtslinks()
            time.sleep(3)
            self.pA.clickEditachieve()
            time.sleep(1)
            self.pA.clickAddachieve()
            time.sleep(1)
            self.pA.clickAchievesubmit()
            time.sleep(2)

            toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/main/section/div[2]/form/div[2]/div/div[1]/div/div")
            if toast_msg:
                result = toast_msg[0].text
                self.logger.info("Toast Message: %s", result)
            else:
                self.logger.info("No toast message found")

            if result == "Achievement Title is required.":
                assert True
                self.logger.info("********** Achievement Title Negative Test passed *********")
            else:
                assert False
                self.logger.info("********** Achievement Title Negative Test failed *********")

            time.sleep(2)

            toast_msgA = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/main/section/div[2]/form/div[2]/div/div[2]/div")
            if toast_msgA:
                resultA = toast_msgA[0].text
                self.logger.info("Toast Message: %s", resultA)
            else:
                self.logger.info("No toast message found")

            if resultA == "Achievement Description is required.":
                assert True
                self.logger.info("********** Achievement Description Negative Test passed *********")
            else:
                assert False
                self.logger.info("********** Achievement Description Negative Test failed *********")

            time.sleep(2)
            self.pA.textAchievedescriptionnew(self.AchieveDescriptionnew)
            time.sleep(2)

            toast_msgC = self.driver.find_elements(By.XPATH,"/html/body/div[3]/div[3]/div/div[2]/main/section/div[2]/form/div[2]/div/div[2]/div")
            if toast_msgC:
                resultC = toast_msgC[0].text
                self.logger.info("Toast Message: %s", resultC)
            else:
                self.logger.info("No toast message found")

            if resultC == "Description should be at least 120 characters in length.":
                assert True
                self.logger.info("********** at least 120 characters Achievement Description Negative Test passed *********")
            else:
                assert False
                self.logger.info("********** at least 120 characters Achievement Description Negative Test failed *********")

            time.sleep(2)
            self.pA.textAchievedescriptionmax(self.AchieveDescriptionmax)
            self.pA.clickAchievesubmit()
            time.sleep(2)

            toast_msgD = self.driver.find_elements(By.XPATH,"/html/body/div[3]/div[3]/div/div[2]/main/section/div[2]/form/div[2]/div/div[2]/div")
            if toast_msgD:
                resultD = toast_msgD[0].text
                self.logger.info("Toast Message: %s", resultD)
            else:
                self.logger.info("No toast message found")

            if resultD == "Description should not exceed 250 characters.":
                assert True
                self.logger.info("********** should not exceed 250 characters Achievement Description Negative Test passed *********")
            else:
                assert False
                self.logger.info("********** should not exceed 250 characters Achievement Description Negative Test failed *********")

            self.driver.close()
            self.logger.info("********** Ending Edit Achievement Negative Test *********")

    # @pytest.mark.sanity
    def test_editAchievementDelete(self, setup):
        # Delete Test
        self.logger.info("********** Test_008_Edit Achievement - Delete **********")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
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
        self.pA.scrollAchieve()
        time.sleep(3)
        self.pA.mousehoverachievecardDel()
        time.sleep(2)

        toast_msgA = self.driver.find_elements(By.XPATH,"/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        if toast_msgA:
            resultA = toast_msgA[0].text
            self.logger.info("Toast Message: %s", resultA)
        else:
            self.logger.info("No toast message found")

        if resultA == "Achievement deleted Sucessfully":
            assert True
            self.logger.info("********** Achievement Deleted Successfully using Bin Symbol *********")
        else:
            assert False
            self.logger.info("********** Achievement Not Deleted Successfully using Bin Symbol *********")



        self.driver.close()
        self.logger.info("********** Ending Edit Achievement Delete Test *********")