import configparser

import pytest
import time

from selenium.webdriver.common.by import By
from pageObjects.LoginPage import Login
from pageObjects.Profile import profile, read_excel_data
from utilities.ExcelUtils import get_data_from_excel
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


config=configparser.ConfigParser()
config.read('C:\\Users\\jenni\\PycharmProjects\\PythonFramework\\Configurations\\config.ini')


class Test_004_EditSkill:

    BaseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    level = ReadConfig.getlevel()
    skill = ReadConfig.getskill()
    logger = LogGen.loggen()


    @pytest.mark.sanity
    def test_editSkillNegative(self, setup):
            # Negative Test
            self.logger.info("********** Test_004_EditSkill Negative Test **********")
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
            time.sleep(3)
            # self.p.scrollExpertise()
            self.p.scrollAbout()
            time.sleep(3)
            self.p.clickExpertise()
            time.sleep(3)
            self.p.clickaddskill()
            time.sleep(2)
            self.p.clickSubmit()
    
            time.sleep(2)
            # toast_msg = self.driver.find_elements(By.XPATH,"/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
            # result = toast_msg[0].text
            # print(result)
    
            error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/main/section/div[2]/form/div[2]/div[1]/div")
            result = error_msg1[0].text
            if result == "Skill Name is required":
                self.logger.info("Error Message Is: %s", result)
            else:
                assert False
                self.logger.info("***************  Skill Name is required Failed   *************")
    
    
            error_msg2 = self.driver.find_elements(By.XPATH,"/html/body/div[3]/div[3]/main/section/div[2]/form/div[2]/div[2]/p")
            result = error_msg2[0].text
            if result == "Skill Level is required":
                self.logger.info("Error Message Is: %s", result)
            else:
                assert False
                self.logger.info("***************  Skill Level is required Failed   *************")
    
    
            self.driver.close()
            self.logger.info("********** Ending Edit Skill Negative Test *********")


    @pytest.mark.sanity
    def test_editSkillPositive(self,setup):
        # Positive Test
        self.logger.info("********** Test_004_EditSkill Positive Test **********")
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
        time.sleep(3)
        self.p.scrollAbout()
        time.sleep(3)
        self.p.clickExpertise()
        time.sleep(2)
        # self.p.clickaddskill()
        # time.sleep(10)
        # self.p.typeskill(self.skill)
        # time.sleep(3)
        # self.p.clickLevel(self.level)
        # time.sleep(2)
        # self.p.clickSubmit()

        # file_path = 'C:/Users/jenni/PycharmProjects/PythonFramework/TestData/LoginData.xlsx'
        # sheet_name = 'skills'
        # skills = read_excel_data(file_path, sheet_name)

        self.p.addallskills()
        time.sleep(2)
        # self.logger.info("*********** Skill Saved **********")
        #
        # time.sleep(2)
        # toast_msg = self.driver.find_elements(By.XPATH,"/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        # result = toast_msg[0].text
        # print(result)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        if toast_msg:
            result = toast_msg[0].text
            self.logger.info("Toast Message: %s", result)
        else:
            self.logger.info("No toast message found")

        if result == "Skills updated successfully.":
            assert True
            self.logger.info("********** Edit Skill Saved test passed *********")
        else:
            assert False
            self.logger.info("********** Edit Skill Saved test failed *********")

        time.sleep(2)
        self.p.clickExpertise()
        time.sleep(2)
        self.p.clickDelskill()
        time.sleep(2)
        # self.p.clickSubmitDelskill()
        # time.sleep(1)

        toast_msgA = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        if toast_msgA:
            resultA = toast_msgA[0].text
            self.logger.info("Toast Message: %s", resultA)
        else:
            self.logger.info("No toast message found")

        if resultA == "Skills updated successfully.":
            assert True
            self.logger.info("********** Edit Skill Deleted Successfully passed *********")
        else:
            assert False
            self.logger.info("********** Edit Skill Deleted Successfully failed *********")


        self.driver.close()
        self.logger.info("********** Ending Edit Skill Positive Test *********")
