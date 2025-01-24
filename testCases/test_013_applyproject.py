import configparser
import pytest
import time
from selenium.webdriver.common.by import By
from pageObjects.Profile import profile
from pageObjects.LoginPage import Login
from pageObjects.postprojects import projects
from pageObjects.applyproject import applyproject
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


config=configparser.ConfigParser()
config.read('C:\\Users\\jenni\\PycharmProjects\\PythonFramework\\Configurations\\config.ini')


class Test_013_ApplyProjects:

    BaseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    # # Project Review - Positive & Negative
    # # @pytest.mark.sanity
    # def test_projectreview(self, setup):
    #
    #     self.logger.info("********** Project Review Test Started **********")
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
    #     # time.sleep(1)
    #     self.pjt.clickPjtButton()
    #     time.sleep(1)
    #     self.ap.clickPjtthreedots()
    #     time.sleep(1)
    #     self.ap.clickPjtreview()
    #     time.sleep(1)
    #     self.ap.clickPjtreviewsubmit()
    #     time.sleep(1)
    #
    #     error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
    #     result = error_msg[0].text
    #     if result == "Rating is required":
    #         self.logger.info("Error Message Is: %s", result)
    #         assert True
    #         self.logger.info("*************** Project Rating Negative Test Passed *************")
    #     else:
    #         assert False
    #         self.logger.info("*************** Project Rating Negative Test Failed *************")
    #
    #
    #     time.sleep(1)
    #     self.ap.clickPjtrating()
    #     time.sleep(1)
    #     self.ap.clickPjtreviewsubmit()
    #     time.sleep(1)
    #
    #     error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
    #     result = error_msg1[0].text
    #     if result == "Review comment is required.":
    #         self.logger.info("Error Message Is: %s", result)
    #         assert True
    #         self.logger.info("*************** Project Review Negative Test Passed *************")
    #     else:
    #         assert False
    #         self.logger.info("*************** Project Review Negative Test Failed *************")
    #
    #     time.sleep(1)
    #     self.ap.clickPjtreviewtext()
    #     time.sleep(1)
    #     self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_pjtreview.png")
    #     time.sleep(1)
    #     self.ap.clickPjtreviewsubmit()
    #     time.sleep(1)
    #
    #     error_msg2 = self.driver.find_elements(By.XPATH,
    #                                            "/html/body/div[1]/div/div/div/div[1]/div[2]")
    #     result = error_msg2[0].text
    #     if result == "Reviewed a Project successfully.":
    #         self.logger.info("Error Message Is: %s", result)
    #         assert True
    #         self.logger.info("*************** Project Review Positive Test Passed *************")
    #     else:
    #         assert False
    #         self.logger.info("*************** Project Review Positive Test Failed *************")
    #
    #
    #     self.logger.info("************** Project Review Test Ended Successfully *************")
    #     self.driver.quit()
    #
    #
    # # Project Report - Positive & Negative
    # # @pytest.mark.sanity
    # def test_projectreport(self, setup):
    #
    #     self.logger.info("********** Project Report Test Started **********")
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
    #     # time.sleep(1)
    #     self.pjt.clickPjtButton()
    #     time.sleep(2)
    #     self.ap.clickPjtthreedots()
    #     time.sleep(1)
    #     self.ap.clickpjtreport()
    #     time.sleep(1)
    #     self.ap.clickpjtreportsubmit()
    #     time.sleep(1)
    #
    #
    #     error_msg = self.driver.find_elements(By.XPATH,
    #                                           "/html/body/div[1]/div/div/div/div[1]/div[2]")
    #     result = error_msg[0].text
    #     if result == "Please type your comment.":
    #         self.logger.info("Error Message Is: %s", result)
    #         assert True
    #         self.logger.info("*************** Project Report Negative Test Passed *************")
    #     else:
    #         assert False
    #         self.logger.info("*************** Project Report Negative Test Failed *************")
    #
    #
    #     time.sleep(1)
    #     self.ap.clickpjtreporttext()
    #     time.sleep(1)
    #     self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_pjtreport.png")
    #     time.sleep(1)
    #     self.ap.clickpjtreportsubmit()
    #     time.sleep(1)
    #
    #     error_msg1 = self.driver.find_elements(By.XPATH,
    #                                            "/html/body/div[1]/div/div/div/div[1]/div[2]")
    #     result = error_msg1[0].text
    #     if result == "Project Reported successfully.":
    #         self.logger.info("Error Message Is: %s", result)
    #         assert True
    #         self.logger.info("*************** Project Report Positive Test Passed *************")
    #     else:
    #         assert False
    #         self.logger.info("*************** Project Report Positive Test Failed *************")
    #
    #
    #     self.logger.info("************** Project Report Test Ended Successfully *************")
    #     self.driver.quit()
    #
    # # Project copy link
    # # @pytest.mark.sanity
    # def test_projectcopylink(self, setup):
    #
    #     self.logger.info("********** Project Copy Link Test Started **********")
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
    #     # time.sleep(1)
    #     self.pjt.clickPjtButton()
    #     time.sleep(2)
    #     self.ap.clickPjtthreedots()
    #     time.sleep(1)
    #     self.ap.clickpjtcopylink()
    #     time.sleep(1)
    #
    #     error_msg = self.driver.find_elements(By.XPATH,
    #                                           "/html/body/div[1]/div/div/div/div[1]/div[2]")
    #     result = error_msg[0].text
    #     if result == "Link copied":
    #         self.logger.info("Error Message Is: %s", result)
    #         assert True
    #         self.logger.info("*************** Link copied Test Passed *************")
    #     else:
    #         assert False
    #         self.logger.info("*************** Link copied Test Failed *************")
    #
    #     self.logger.info("************** Project Copy Link Test Ended Successfully *************")
    #     self.driver.quit()
    #
    # # Project Save/Unsave
    # # @pytest.mark.sanity
    # def test_projectsave(self, setup):
    #
    #     self.logger.info("********** Project Save/Unsave Test Started **********")
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
    #     # time.sleep(1)
    #     self.pjt.clickPjtButton()
    #     time.sleep(1)
    #     self.ap.clickPjtSave()
    #     time.sleep(1)
    #
    #     error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
    #     result = error_msg[0].text
    #     self.logger.info("Error Message Is: %s", result)
    #
    #     time.sleep(1)
    #     self.ap.clickPjtSave()
    #     time.sleep(1)
    #
    #     error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
    #     result = error_msg1[0].text
    #     self.logger.info("Error Message Is: %s", result)
    #
    #     self.logger.info("************** Project Save/Unsave Test Ended Successfully *************")
    #     self.driver.quit()


    # Staff Augmentation - Apply - Negative Test
    # @pytest.mark.sanity
    def test_pjtstaffapplynegative(self, setup):

            self.logger.info("********** Staff Augmentation Apply Negative Test Started **********")
            self.driver = setup
            self.driver.get(self.BaseURL)
            self.driver.maximize_window()
            self.l = Login(self.driver)
            self.pjt = projects(self.driver)
            self.ap = applyproject(self.driver)
            self.l.clicksignin()
            time.sleep(1)
            self.l.setUserName(self.username)
            time.sleep(1)
            self.l.setPassword(self.password)
            time.sleep(1)
            self.l.clickLogin()
            time.sleep(3)
            self.pjt.selectionelement()
            time.sleep(3)
            # time.sleep(1)
            self.pjt.clickPjtButton()
            time.sleep(2)
            self.ap.clickPjtApply()
            time.sleep(2)
            self.ap.scrollstaffapplysubmit()
            time.sleep(3)
            self.ap.clickstaffapplysubmit()
            time.sleep(1)

            error_msg = self.driver.find_elements(By.XPATH,
                                                  "/html/body/div[4]/div[3]/div/form/p[3]")
            result = error_msg[0].text
            if result == "Description is required.":
                self.logger.info("Error Message Is: %s", result)
                assert True
                self.logger.info("*************** Description is required Test Passed *************")
            else:
                assert False
                self.logger.info("*************** Description is required Test Failed *************")

            time.sleep(2)
            self.ap.setpjtstaffapplydescneg()
            time.sleep(1)
            self.ap.clickstaffapplysubmit()
            time.sleep(1)

            error_msg1 = self.driver.find_elements(By.XPATH,
                                                   "/html/body/div[4]/div[3]/div/form/p[3]")
            result = error_msg1[0].text
            if result == "Description should be more than 160 characters long.":
                self.logger.info("Error Message Is: %s", result)
                assert True
                self.logger.info(
                    "*************** Description should be more than 160 characters long Test Passed *************")
            else:
                assert False
                self.logger.info(
                    "*************** Description should be more than 160 characters long Test Failed *************")

            time.sleep(2)
            self.ap.setpjtstaffapplydesc()
            time.sleep(1)
            self.ap.clickstaffapplysubmit()
            time.sleep(1)

            error_msg2 = self.driver.find_elements(By.XPATH,
                                                   "/html/body/div[1]/div/div/div/div[1]/div[2]")
            result = error_msg2[0].text
            if result == "Please upload the Profile Tracker document.":
                self.logger.info("Error Message Is: %s", result)
                assert True
                self.logger.info("*************** Please upload the Profile Tracker document Test Passed *************")
            else:
                assert False
                self.logger.info("*************** Please upload the Profile Tracker document Test Failed *************")

            time.sleep(2)
            self.ap.uploadprofiletracker()
            time.sleep(3)
            self.ap.clickstaffapplysubmit()
            time.sleep(1)

            error_msg3 = self.driver.find_elements(By.XPATH,
                                                   "/html/body/div[1]/div/div/div/div[1]/div[2]")
            result = error_msg3[0].text
            if result == "Please upload the Profile document.":
                self.logger.info("Error Message Is: %s", result)
                assert True
                self.logger.info("*************** Please upload the Profile document Test Passed *************")
            else:
                assert False
                self.logger.info("*************** Please upload the Profile document Test Failed *************")

            time.sleep(2)
            self.ap.uploadpjtprofile()
            time.sleep(3)
            self.ap.clickonbehalfofstaffapply()
            time.sleep(1)
            self.ap.clickstaffapplysubmit()
            time.sleep(1)

            error_msg4 = self.driver.find_elements(By.XPATH,
                                                   "/html/body/div[1]/div/div/div/div[1]/div[2]")
            result = error_msg4[0].text
            if result == "Select On Behalf of account.":
                self.logger.info("Error Message Is: %s", result)
                assert True
                self.logger.info("*************** Select On Behalf of account Test Passed *************")
            else:
                assert False
                self.logger.info("*************** Select On Behalf of account Test Failed *************")

            self.logger.info("************** Staff Augmentation Apply Negative Test Ended Successfully *************")
            self.driver.quit()

    # Staff Augmentation - Apply - Positive Test
    # @pytest.mark.sanity
    def test_pjtstaffapplyPositive(self, setup):

            self.logger.info("********** Staff Augmentation Apply Positive Test Started **********")
            self.driver = setup
            self.driver.get(self.BaseURL)
            self.driver.maximize_window()
            self.l = Login(self.driver)
            self.pjt = projects(self.driver)
            self.ap = applyproject(self.driver)
            self.l.clicksignin()
            time.sleep(1)
            self.l.setUserName(self.username)
            time.sleep(1)
            self.l.setPassword(self.password)
            time.sleep(1)
            self.l.clickLogin()
            time.sleep(3)
            self.pjt.selectionelement()
            time.sleep(3)
            # time.sleep(1)
            self.pjt.clickPjtButton()
            time.sleep(2)
            self.ap.clickPjtApply()
            time.sleep(1)
            self.ap.uploadprofiletracker()
            time.sleep(1)
            self.ap.uploadpjtprofile()
            time.sleep(1)
            self.ap.setpjtstaffapplydesc()
            time.sleep(1)
            self.ap.clickonbehalfofstaffapply()
            time.sleep(2)
            self.ap.clickbehalfchooseonestaffapply()  # Manually select on behalf of accounts from the dropdown
            time.sleep(5)
            self.ap.clickstaffapplysubmit()
            time.sleep(1)

            error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
            result = error_msg[0].text

            if result == "Project Applied Successfully.":
                self.logger.info("Error Message Is: %s", result)
                assert True
                self.logger.info("*************** Project Applied Successfully Test Passed *************")
            else:
                assert False
                self.logger.info("*************** Project Applied Successfully Test Failed *************")

            self.logger.info("************** Staff Augmentation Apply Positive Test Ended Successfully *************")
            self.driver.quit()


    # Project type - Apply - Negative Test
    # @pytest.mark.sanity
    def test_projecttypeapplynegative(self, setup):

        self.logger.info("********** Project Type Apply Negative Test Started **********")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.pjt = projects(self.driver)
        self.ap = applyproject(self.driver)
        self.l.clicksignin()
        time.sleep(1)
        self.l.setUserName(self.username)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        time.sleep(3)
        self.pjt.selectionelement()
        time.sleep(3)
        # time.sleep(1)
        self.pjt.clickPjtButton()
        time.sleep(2)
        self.ap.clickPjtApply()
        time.sleep(2)
        self.ap.clickpjttypesubmit()
        time.sleep(1)

        error_msg = self.driver.find_elements(By.XPATH,
                                              "/html/body/div[4]/div[3]/form/p[1]")
        result = error_msg[0].text
        if result == "No of days is required.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** No of days is required Test Passed *************")
        else:
            assert False
            self.logger.info("*************** No of days is required Test Failed *************")



        error_msg1 = self.driver.find_elements(By.XPATH,
                                              "/html/body/div[4]/div[3]/form/p[2]")
        result = error_msg1[0].text
        if result == "Bid amount should not be blank.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Bid amount should not be blank Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Bid amount should not be blank Test Failed *************")



        error_msg2 = self.driver.find_elements(By.XPATH,
                                              "/html/body/div[4]/div[3]/form/p[3]")
        result = error_msg2[0].text
        if result == "Proposal Description is required.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Proposal Description is required Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Proposal Description is required Test Failed *************")

        time.sleep(2)
        self.ap.clickPjtdeliveryneg()
        time.sleep(1)
        self.ap.clickBidamtneg()
        time.sleep(1)
        self.ap.setpjtproposaldescneg()
        time.sleep(1)
        self.ap.clickpjttypesubmit()
        time.sleep(1)


        error_msg3 = self.driver.find_elements(By.XPATH,
                                              "/html/body/div[4]/div[3]/form/p[1]")
        result = error_msg3[0].text
        if result == "No of days should be more than 0":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** No of days should be more than 0 Test Passed *************")
        else:
            assert False
            self.logger.info("*************** No of days should be more than 0 Test Failed *************")


        error_msg4 = self.driver.find_elements(By.XPATH,
                                               "/html/body/div[4]/div[3]/form/p[2]")
        result = error_msg4[0].text
        if result == "Bid amount should be greater than 0.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Bid amount should be greater than 0 Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Bid amount should be greater than 0 Test Failed *************")


        error_msg5 = self.driver.find_elements(By.XPATH,
                                               "/html/body/div[4]/div[3]/form/p[3]")
        result = error_msg5[0].text
        if result == "Proposal Description should be at least 160 characters long.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Proposal Description should be at least 160 characters long Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Proposal Description should be at least 160 characters long Test Failed *************")


        time.sleep(2)
        self.ap.clickPjtdeliveryneg1()
        time.sleep(1)
        self.ap.clickBidamtneg1()
        time.sleep(1)
        self.ap.clickpjttypesubmit()
        time.sleep(1)

        error_msg6 = self.driver.find_elements(By.XPATH,
                                               "/html/body/div[4]/div[3]/form/p[1]")
        result = error_msg6[0].text
        if result == "Invalid number of required days.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info( "*************** Invalid number of required days Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Invalid number of required days Test Failed *************")


        error_msg7 = self.driver.find_elements(By.XPATH,
                                               "/html/body/div[4]/div[3]/form/p[2]")
        result = error_msg7[0].text
        if result == "Invalid Bid amount.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Invalid Bid amount Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Invalid Bid amount Test Failed *************")


        time.sleep(2)
        self.ap.clickPjtdelivery()
        time.sleep(1)
        self.ap.clickBidamt()
        time.sleep(1)
        self.ap.setpjtproposaldesc()
        time.sleep(1)
        self.ap.clickpjttypesubmit()
        time.sleep(1)

        error_msg8 = self.driver.find_elements(By.XPATH,
                                               "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = error_msg8[0].text
        if result == "Please check the Proposal document.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Please check the Proposal document Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Please check the Proposal document Test Failed *************")


        self.logger.info("************** Project Type Apply Negative Test Ended Successfully *************")
        self.driver.quit()


    # Project type - Apply - Positive Test
    # @pytest.mark.sanity
    def test_projecttypeapplyPositive(self, setup):

        self.logger.info("********** Project Type Apply Positive Test Started **********")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.pjt = projects(self.driver)
        self.ap = applyproject(self.driver)
        self.l.clicksignin()
        time.sleep(1)
        self.l.setUserName(self.username)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        time.sleep(3)
        self.pjt.selectionelement()
        time.sleep(3)
        # time.sleep(1)
        self.pjt.clickPjtButton()
        time.sleep(2)
        self.ap.clickPjtApply()
        time.sleep(1)
        self.ap.clickPjtdelivery()
        time.sleep(1)
        self.ap.clickBidamt()
        time.sleep(1)
        self.ap.uploadProposaldoc()
        time.sleep(1)
        self.ap.setpjtproposaldesc()
        time.sleep(1)
        self.ap.clickonbehalfofpjtapply()
        time.sleep(2)
        self.ap.clickbehalfchooseonepjtapply()
        time.sleep(5)
        self.ap.clickpjttypesubmit()  # Manually select on behalf of accounts from the dropdown
        time.sleep(1)

        error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = error_msg[0].text

        if result == "Project Applied Successfully.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Project Applied Successfully Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Project Applied Successfully Test Failed *************")


        self.logger.info("************** Project Type Apply Positive Test Ended Successfully *************")
        self.driver.quit()


    # Project Not Interested
    # @pytest.mark.sanity
    def test_projectnotinterested(self, setup):

        self.logger.info("********** Project Not Interested Test Started **********")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.pjt = projects(self.driver)
        self.ap = applyproject(self.driver)
        self.l.clicksignin()
        time.sleep(1)
        self.l.setUserName(self.username)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        time.sleep(3)
        self.pjt.selectionelement()
        time.sleep(3)
        # time.sleep(1)
        self.pjt.clickPjtButton()
        time.sleep(1)
        self.ap.clickPjtthreedots()
        time.sleep(1)
        self.ap.clickpjtnotinterest()
        time.sleep(1)
        self.ap.clickpjtnotinterestyes()
        time.sleep(1)

        error_msg = self.driver.find_elements(By.XPATH,
                                              "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = error_msg[0].text
        if result == "Not interested successfully.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Project Not Interested Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Project Not Interested Test Failed *************")

        self.logger.info("************** Project Not Interested Test Ended Successfully *************")
        self.driver.quit()


    # Project - Open,Close,applied,save
    # @pytest.mark.sanity
    def test_pjtASOC(self, setup):

        self.logger.info("********** Open Close Applied Saved Test Started **********")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.pjt = projects(self.driver)
        self.ap = applyproject(self.driver)
        self.l.clicksignin()
        time.sleep(1)
        self.l.setUserName(self.username)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        # time.sleep(5)
        time.sleep(3)
        self.pjt.selectionelement()
        time.sleep(3)
        self.ap.clickprofilenavbardroparrow()
        time.sleep(2)
        self.ap.clickpjtdownarrow()
        time.sleep(1)
        self.ap.clickopenpjt()
        time.sleep(1)
        self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_openpjt.png")
        time.sleep(1)
        self.ap.clickopenpjt3dots()
        time.sleep(1)
        self.ap.clickopenpjtclose()
        time.sleep(1)


        error_msg = self.driver.find_elements(By.XPATH,
                                              "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = error_msg[0].text
        if result == "project has been closed successfully.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** project has been closed successfully Test Passed *************")
        else:
            assert False
            self.logger.info("*************** project has been closed successfully Test Failed *************")


        time.sleep(2)
        self.ap.clickclosedpjt()
        time.sleep(1)
        self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_closedpjt.png")
        time.sleep(1)
        self.ap.clickclosedpjtrepost()
        time.sleep(1)
        self.ap.scrollpjtrepostbutton()
        time.sleep(1)
        self.ap.clickpjtrepostbutton()
        time.sleep(1)

        error_msg1 = self.driver.find_elements(By.XPATH,
                                              "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = error_msg1[0].text
        if result == "Project created successfully":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Project created successfully Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Project created successfully Test Failed *************")


        time.sleep(2)
        self.ap.clickprofilenavbardroparrow()
        time.sleep(2)
        self.ap.clickpjtdownarrow()
        time.sleep(1)
        self.ap.clickappliedpjt()
        time.sleep(1)
        self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_appliedpjt.png")
        time.sleep(1)
        self.ap.clicksavedpjt()
        time.sleep(1)
        self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_savedpjt.png")
        time.sleep(1)


        self.logger.info("************** Open Close Applied Saved Test Ended Successfully *************")
        self.driver.quit