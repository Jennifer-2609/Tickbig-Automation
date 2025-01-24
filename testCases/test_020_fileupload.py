import configparser
import pytest
import time
from selenium.webdriver.common.by import By

from pageObjects.Fundraise import fundraise
from pageObjects.LoginPage import Login
from pageObjects.applyproject import applyproject
from pageObjects.postprojects import projects
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


config=configparser.ConfigParser()
config.read('C:\\Users\\jenni\\PycharmProjects\\PythonFramework\\Configurations\\config.ini')


class Test_020_Fileupload:

    BaseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    # Project Type Apply - Upload
    # @pytest.mark.sanity
    # def test_projecttypeapplyuploadneg(self, setup):
    #
    #     self.logger.info("**********  Project Type Apply - File Upload Negative Test Started **********")
    #     self.driver = setup
    #     self.driver.get(self.BaseURL)
    #     self.driver.maximize_window()
    #     self.l = Login(self.driver)
    #     self.pjt = projects(self.driver)
    #     self.ap = applyproject(self.driver)
    #     self.l.clicksignin()
    #     time.sleep(1)
    #     self.l.setUserName(self.username)
    #     time.sleep(1)
    #     self.l.setPassword(self.password)
    #     time.sleep(1)
    #     self.l.clickLogin()
    #     time.sleep(3)
    #     self.pjt.selectionelement()
    #     time.sleep(3)
    #     self.pjt.clickPjtButton()
    #     time.sleep(2)
    #     self.ap.clickPjtApply()
    #     time.sleep(2)
    #     self.ap.uploadProposaldoclarge()
    #     time.sleep(1)
    #
    #     error_msg = self.driver.find_elements(By.XPATH,"/html/body/div[1]/div/div/div/div[1]/div[2]")
    #     result = error_msg[0].text
    #     if result == "File is too large.":
    #         self.logger.info("Error Message Is: %s", result)
    #         assert True
    #     else:
    #         assert False
    #         self.logger.info("*************** File is too large for Project type apply Failed *************")
    #
    #     time.sleep(2)
    #     self.ap.uploadProposaldocincfile()
    #     time.sleep(1)
    #
    #     error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
    #     result = error_msg[0].text
    #     if result == "Invalid file format.":
    #         self.logger.info("Error Message Is: %s", result)
    #         assert True
    #     else:
    #         assert False
    #         self.logger.info("*************** Invalid file format for Project type apply Failed *************")
    #
    #
    #     self.logger.info("************** Project Type Apply - File Upload Negative Test Ended Successfully *************")
    #     self.driver.quit()

    # Staff Augmentation Apply - Upload
    # @pytest.mark.sanity
    # def test_staffapplyuploadneg(self, setup):
    #
    #     self.logger.info("**********  Staff Augmentation Apply - File Upload Negative Test Started **********")
    #     self.driver = setup
    #     self.driver.get(self.BaseURL)
    #     self.driver.maximize_window()
    #     self.l = Login(self.driver)
    #     self.pjt = projects(self.driver)
    #     self.ap = applyproject(self.driver)
    #     self.l.clicksignin()
    #     time.sleep(1)
    #     self.l.setUserName(self.username)
    #     time.sleep(1)
    #     self.l.setPassword(self.password)
    #     time.sleep(1)
    #     self.l.clickLogin()
    #     time.sleep(3)
    #     self.pjt.selectionelement()
    #     time.sleep(3)
    #     self.pjt.clickPjtButton()
    #     time.sleep(2)
    #     self.ap.clickPjtApply()
    #     time.sleep(2)
    #     self.ap.uploadprofiletrackerlarge()
    #     time.sleep(1)
    #
    #     error_msg = self.driver.find_elements(By.XPATH,"/html/body/div[1]/div/div/div/div[1]/div[2]")
    #     result = error_msg[0].text
    #     if result == "File is too large.":
    #         self.logger.info("Error Message Is: %s", result)
    #         assert True
    #     else:
    #         assert False
    #         self.logger.info("*************** File is too large for Staff apply - Profile Tracker Failed *************")
    #
    #     time.sleep(2)
    #     self.ap.uploadprofiletrackerincfile()
    #     time.sleep(1)
    #
    #     error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
    #     result = error_msg[0].text
    #     if result == "Invalid file format.":
    #         self.logger.info("Error Message Is: %s", result)
    #         assert True
    #     else:
    #         assert False
    #         self.logger.info("*************** Invalid file format for Staff apply - Profile Tracker Failed *************")
    #
    #     time.sleep(2)
    #     self.ap.uploadpjtprofilelarge()
    #     time.sleep(1)
    #
    #     error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
    #     result = error_msg[0].text
    #     if result == "File is too large.":
    #         self.logger.info("Error Message Is: %s", result)
    #         assert True
    #     else:
    #         assert False
    #         self.logger.info("*************** File is too large for Staff apply - Profile Failed *************")
    #
    #     time.sleep(2)
    #     self.ap.uploadpjtprofileincfile()
    #     time.sleep(1)
    #
    #     error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
    #     result = error_msg[0].text
    #     if result == "Invalid file format.":
    #         self.logger.info("Error Message Is: %s", result)
    #         assert True
    #     else:
    #         assert False
    #         self.logger.info("*************** Invalid file format for Staff apply - Profile Failed *************")
    #
    #
    #     self.logger.info("************** Staff Augmnetaion Apply - File Upload Negative Test Ended Successfully *************")
    #     self.driver.quit()


    # Post fundraise - Upload
    # @pytest.mark.sanity
    def test_postfunduploadneg(self, setup):

        self.logger.info("********** Post Fundraise -  File Upload Negative Test Started **********")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.pjt = projects(self.driver)
        self.fund = fundraise(self.driver)
        self.l.clicksignin()
        time.sleep(1)
        self.driver.refresh()
        time.sleep(3)
        self.l.setUserName(self.username)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        time.sleep(3)
        self.pjt.selectionelement()
        time.sleep(3)
        self.fund.clickfundraise()
        time.sleep(2)
        self.fund.clickpostfund()
        time.sleep(2)
        self.fund.scrollpostfundfinal()
        time.sleep(2)
        self.fund.uploadfunddescdoclarge()
        time.sleep(1)

        error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = error_msg[0].text
        if result == "File is too large.":
            self.logger.info("Error Message Is: %s", result)
            assert True
        else:
            assert False
            self.logger.info("*************** File is too large for Post Fundraise - Desc Doc Failed *************")

        time.sleep(2)
        self.fund.uploadfunddescdocincfile()
        time.sleep(1)

        error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = error_msg[0].text
        if result == "Unsupported File type found.":
            self.logger.info("Error Message Is: %s", result)
            assert True
        else:
            assert False
            self.logger.info("*************** Unsupported File type found for Post Fundraise - Desc Doc Failed *************")

        self.logger.info("************** Staff Augmnetaion Apply - File Upload Negative Test Ended Successfully *************")
        self.driver.quit()

    # Apply Job - Upload
    # @pytest.mark.sanity
    def test_applyjobuploadneg(self, setup):

        self.logger.info("********** Job Apply -  File Upload Negative Test Started **********")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.pjt = projects(self.driver)
        self.fund = fundraise(self.driver)
        self.l.clicksignin()
        time.sleep(1)
        self.driver.refresh()
        time.sleep(3)
        self.l.setUserName(self.username)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        time.sleep(3)
        self.pjt.selectionelement()
        time.sleep(3)
        self.l.clickJobbtn()
        time.sleep(2)
        self.l.clickJobapplybtn()
        time.sleep(2)
        self.l.clickonbehalfofjobapply()
        time.sleep(2)
        self.l.uploadjobproftrackerlarge()
        time.sleep(1)

        error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = error_msg[0].text
        if result == "File is too large.":
            self.logger.info("Error Message Is: %s", result)
            assert True
        else:
            assert False
            self.logger.info("*************** File is too large for Job apply - Profile Tracker Failed *************")

        time.sleep(2)
        self.l.uploadjobproftrackerincfile()
        time.sleep(1)

        error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = error_msg[0].text
        if result == "Please choose correct File type":
            self.logger.info("Error Message Is: %s", result)
            assert True
        else:
            assert False
            self.logger.info("*************** Please choose correct File type for Job apply - Profile Tracker Failed *************")

        time.sleep(2)
        self.l.uploadjobproflarge()
        time.sleep(1)

        error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = error_msg[0].text
        if result == "File is too large.":
            self.logger.info("Error Message Is: %s", result)
            assert True
        else:
            assert False
            self.logger.info("*************** File is too large for Job apply - Profile Failed *************")

        time.sleep(2)
        self.l.uploadjobprofincfile()
        time.sleep(1)

        error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = error_msg[0].text
        if result == "Please choose correct File type":
            self.logger.info("Error Message Is: %s", result)
            assert True
        else:
            assert False
            self.logger.info("*************** Please choose correct File type for Job apply - Profile Failed *************")


        self.logger.info("************** Job Apply - File Upload Negative Test Ended Successfully *************")
        self.driver.quit()


    # Pitch Invest - Upload
    # @pytest.mark.sanity
    def test_pitchinvestuploadneg(self, setup):

        self.logger.info("********** Pitch Invest -  File Upload Negative Test Started **********")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.pjt = projects(self.driver)
        self.fund = fundraise(self.driver)
        self.l.clicksignin()
        time.sleep(1)
        self.driver.refresh()
        time.sleep(3)
        self.l.setUserName(self.username)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        time.sleep(3)
        self.pjt.selectionelement()
        time.sleep(3)
        self.l.clickinvestbtn()
        time.sleep(2)
        self.l.clickpitchinvestbtn()
        time.sleep(2)
        self.l.uploadpitchdoclarge()
        time.sleep(1)

        error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = error_msg[0].text
        if result == "File is too large.":
            self.logger.info("Error Message Is: %s", result)
            assert True
        else:
            assert False
            self.logger.info("*************** File is too large for Pitch Investing - Pitch Deck Failed *************")

        time.sleep(2)
        self.l.uploadpitchdocincfile()
        time.sleep(1)

        error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = error_msg[0].text
        if result == "Invalid file format.":
            self.logger.info("Error Message Is: %s", result)
            assert True
        else:
            assert False
            self.logger.info("*************** Invalid file format for Pitch Investing - Pitch Deck Failed *************")


        self.logger.info("************** Pitch Invest - File Upload Negative Test Ended Successfully *************")
        self.driver.quit()