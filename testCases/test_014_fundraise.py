import configparser
import pytest
import time
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import Login
from pageObjects.Fundraise import fundraise
from pageObjects.applyproject import applyproject
from pageObjects.postprojects import projects
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


config=configparser.ConfigParser()
config.read('C:\\Users\\jenni\\PycharmProjects\\PythonFramework\\Configurations\\config.ini')


class Test_014_Fundraise:

    BaseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    # # Post Fundraise - Negative Testcase1
    # @pytest.mark.sanity
    # def test_postfundnegative1(self, setup):
    #
    #     self.logger.info("********** Test_014 Fundraise - Post Fundraise Negative Test 1 **********")
    #     self.logger.info("********** Post Fundraise - Negative Test 1 Started **********")
    #     self.driver = setup
    #     self.driver.get(self.BaseURL)
    #     self.driver.maximize_window()
    #     self.l = Login(self.driver)
    #     self.pjt = projects(self.driver)
    #     self.fund= fundraise(self.driver)
    #     # self.l.clicksignin()
    #     # time.sleep(1)
    #     self.l.setUserName(self.username)
    #     time.sleep(1)
    #     self.l.setPassword(self.password)
    #     time.sleep(1)
    #     self.l.clickLogin()
    #     # time.sleep(10)
    #     # self.pjt.selectionelement()
    #     # time.sleep(10)
    #     time.sleep(1)
    #     self.fund.clickfundraise()
    #     time.sleep(2)
    #     self.fund.clickpostfund()
    #     time.sleep(5)
    #     self.fund.scrollpostfundfinal()
    #     time.sleep(10)
    #     self.fund.clickpostfundfinal()
    #     time.sleep(10)
    #
    #
    #     error_msg1 = self.driver.find_elements(By.XPATH,"/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[2]/p")
    #     result = error_msg1[0].text
    #     if result == "Company Name is required":
    #         self.logger.info("Error Message Is: %s", result)
    #     else:
    #         assert False
    #         self.logger.info("***************  Company Name is required Failed *************")
    #
    #
    #     error_msg2 = self.driver.find_elements(By.XPATH,"/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[3]/p")
    #     result = error_msg2[0].text
    #     if result == "Company Age is required.":
    #         self.logger.info("Error Message Is: %s", result)
    #     else:
    #         assert False
    #         self.logger.info("*************** Company Age is required Failed *************")
    #
    #
    #     error_msg3 = self.driver.find_elements(By.XPATH,"/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[4]/p")
    #     result = error_msg3[0].text
    #     if result == "Company Valuation is required":
    #         self.logger.info("Error Message Is: %s", result)
    #     else:
    #         assert False
    #         self.logger.info("*************** Company Valuation is required Failed *************")
    #
    #     error_msg4 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[5]/p[1]")
    #     result = error_msg4[0].text
    #     if result == "Company Min Size is required":
    #         self.logger.info("Error Message Is: %s", result)
    #     else:
    #         assert False
    #         self.logger.info("*************** Company Min Size is required Failed *************")
    #
    #
    #     error_msg5 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[5]/p[2]")
    #     result = error_msg5[0].text
    #     if result == "Company Max Size is required.":
    #         self.logger.info("Error Message Is: %s", result)
    #     else:
    #         assert False
    #         self.logger.info("*************** Company Max Size is required Failed *************")
    #
    #
    #     error_msg6 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[7]/p")
    #     result = error_msg6[0].text
    #     if result == "Stage is required":
    #         self.logger.info("Error Message Is: %s", result)
    #     else:
    #         assert False
    #         self.logger.info("*************** Stage is required Failed *************")
    #
    #
    #     error_msg7 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[9]/div/div/div")
    #     result = error_msg7[0].text
    #     if result == "Short Description is required":
    #         self.logger.info("Error Message Is: %s", result)
    #     else:
    #         assert False
    #         self.logger.info("*************** Short Description is required Failed *************")
    #
    #
    #     error_msg8 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[11]/p")
    #     result = error_msg8[0].text
    #     if result == "Who can apply is required":
    #         self.logger.info("Error Message Is: %s", result)
    #     else:
    #         assert False
    #         self.logger.info("*************** Who can apply is required Failed *************")
    #
    #     self.logger.info("************** Post Fundraise - Negative Test 1 Ended Successfully *************")
    #     self.driver.quit()


    # # Post Fundraise - Negative Testcase 2
    # @pytest.mark.sanity
    # def test_postfundnegative2(self, setup):
    #
    #     self.logger.info("********** Post Fundraise - Negative Test 2 Started **********")
    #     self.driver = setup
    #     self.driver.get(self.BaseURL)
    #     self.driver.maximize_window()
    #     self.l = Login(self.driver)
    #     self.pjt = projects(self.driver)
    #     self.fund = fundraise(self.driver)
    #     # self.l.clicksignin()
    #     # time.sleep(1)
    #     self.l.setUserName(self.username)
    #     time.sleep(1)
    #     self.l.setPassword(self.password)
    #     time.sleep(1)
    #     self.l.clickLogin()
    #     # time.sleep(10)
    #     # self.pjt.selectionelement()
    #     # time.sleep(10)
    #     time.sleep(1)
    #     self.fund.clickfundraise()
    #     time.sleep(2)
    #     self.fund.clickpostfund()
    #     time.sleep(5)
    #     self.fund.scrollpostfundfinal()
    #     time.sleep(10)
    #     self.fund.clickpostfundfinal()
    #     time.sleep(10)
    #     self.fund.clickfundcompnameneg1()
    #     time.sleep(2)
    #
    #     error_msg = self.driver.find_elements(By.XPATH,"/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[2]/p")
    #     result = error_msg[0].text
    #     if result == "Invalid Company Name.":
    #         self.logger.info("Error Message Is: %s", result)
    #     else:
    #         assert False
    #         self.logger.info("*************** Invalid Company Name Failed *************")
    #
    #     time.sleep(2)
    #     self.fund.clickfundcompnameneg2()
    #     time.sleep(2)
    #
    #     error_msg1 = self.driver.find_elements(By.XPATH,
    #                                           "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[2]/p")
    #     result = error_msg1[0].text
    #     if result == "Company name contains invalid character.":
    #         self.logger.info("Error Message Is: %s", result)
    #     else:
    #         assert False
    #         self.logger.info("*************** Company name contains invalid character Failed *************")
    #
    #     time.sleep(2)
    #     self.fund.clickfundcompageneg()
    #     time.sleep(2)
    #
    #     error_msg2 = self.driver.find_elements(By.XPATH,
    #                                            "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[3]/p")
    #     result = error_msg2[0].text
    #     if result == "Invalid Company Age":
    #         self.logger.info("Error Message Is: %s", result)
    #     else:
    #         assert False
    #         self.logger.info("*************** Invalid Company Age Failed *************")
    #
    #     time.sleep(2)
    #     self.fund.clickfundcompvaluationneg()
    #     time.sleep(2)
    #
    #     error_msg3 = self.driver.find_elements(By.XPATH,
    #                                            "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[4]/p")
    #     result = error_msg3[0].text
    #     if result == "Invalid Company Valuation.":
    #         self.logger.info("Error Message Is: %s", result)
    #     else:
    #         assert False
    #         self.logger.info("*************** Invalid Company Valuation Failed *************")
    #
    #     time.sleep(2)
    #     self.fund.clickfundcompsizeminneg1()
    #     time.sleep(2)
    #     self.fund.clickfundcompsizemaxneg1()
    #     time.sleep(2)
    #
    #
    #     error_msg4 = self.driver.find_elements(By.XPATH,
    #                                            "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[5]/p[1]")
    #     result = error_msg4[0].text
    #     if result == "Invalid Company Size":
    #         self.logger.info("Error Message Is: %s", result)
    #     else:
    #         assert False
    #         self.logger.info("*************** Invalid Company Size Failed *************")
    #
    #     error_msg5 = self.driver.find_elements(By.XPATH,
    #                                            "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[5]/p[2]")
    #     result = error_msg5[0].text
    #     if result == "Invalid Company Size":
    #         self.logger.info("Error Message Is: %s", result)
    #     else:
    #         assert False
    #         self.logger.info("*************** Invalid Company Size Failed *************")
    #
    #     time.sleep(2)
    #     self.fund.clickfundcompsizeminneg2()
    #     time.sleep(2)
    #     self.fund.clickfundcompsizemaxneg2()
    #     time.sleep(2)
    #
    #     error_msg6 = self.driver.find_elements(By.XPATH,
    #                                            "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[5]/p")
    #     result = error_msg6[0].text
    #     if result == "Min value should be less than or equal to Max value":
    #         self.logger.info("Error Message Is: %s", result)
    #     else:
    #         assert False
    #         self.logger.info("*************** Min value should be less than or equal to Max value Failed *************")
    #
    #     time.sleep(2)
    #     self.fund.clickfundshortdescneg1()
    #     time.sleep(2)
    #
    #     error_msg7 = self.driver.find_elements(By.XPATH,
    #                                            "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[9]/div/div/div")
    #     result = error_msg7[0].text
    #     if result == "Invalid Short Description.":
    #         self.logger.info("Error Message Is: %s", result)
    #     else:
    #         assert False
    #         self.logger.info("*************** Invalid Short Description Failed *************")
    #
    #     time.sleep(2)
    #     self.fund.clickfundshortdescneg2()
    #     time.sleep(2)
    #
    #     error_msg8 = self.driver.find_elements(By.XPATH,
    #                                            "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[9]/div/div/div")
    #     result = error_msg8[0].text
    #     if result == "Short Description less than 200 character long":
    #         self.logger.info("Error Message Is: %s", result)
    #     else:
    #         assert False
    #         self.logger.info("*************** Invalid Short Description Failed *************")
    #
    #     self.logger.info("************** Post Fundraise - Negative Test 2 Ended Successfully *************")
    #     self.driver.quit()


    # # Project type - Positive Testcase
    # @pytest.mark.sanity
    # def test_postfundpositive(self, setup):
    #
    #     self.logger.info("********** Post Fundraise -  Positive Test  Started **********")
    #     self.driver = setup
    #     self.driver.get(self.BaseURL)
    #     self.driver.maximize_window()
    #     self.l = Login(self.driver)
    #     self.pjt = projects(self.driver)
    #     self.fund = fundraise(self.driver)
    #     # self.l.clicksignin()
    #     # time.sleep(1)
    #     self.l.setUserName(self.username)
    #     time.sleep(1)
    #     self.l.setPassword(self.password)
    #     time.sleep(1)
    #     self.l.clickLogin()
    #     # time.sleep(10)
    #     # self.pjt.selectionelement()
    #     # time.sleep(10)
    #     time.sleep(1)
    #     self.fund.clickfundraise()
    #     time.sleep(2)
    #     self.fund.clickpostfund()
    #     time.sleep(2)
    #     self.fund.clickfundcompname()
    #     time.sleep(2)
    #     self.fund.clickfundcompage()
    #     time.sleep(2)
    #     self.fund.clickfundcompvaluation()
    #     time.sleep(2)
    #     self.fund.clickfundcompsizemin()
    #     time.sleep(2)
    #     self.fund.clickfundcompsizemax()
    #     time.sleep(2)
    #     self.fund.clickfundstage()
    #     time.sleep(2)
    #     self.fund.clickfundstagedetails()
    #     time.sleep(2)
    #     self.fund.clickfundsector()
    #     time.sleep(2)
    #     self.fund.clickfundsectoranimation()
    #     time.sleep(2)
    #     self.fund.clickfundshortdesc()
    #     time.sleep(2)
    #     self.fund.uploadfunddescdoc()
    #     time.sleep(7)
    #     self.fund.clickwhocanapplyfund()  # manually select who can apply from the list
    #     time.sleep(7)
    #     self.fund.clickfundpostonbehalf()
    #     time.sleep(2)
    #     self.fund.clickfundonbehalfchooseone() # manually select onbehalfof from the list
    #     time.sleep(5)
    #     self.fund.clickpostfundfinal()
    #     time.sleep(2)
    #
    #
    #     error_msg2 = self.driver.find_elements(By.XPATH,"/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
    #     result = error_msg2[0].text
    #     if result == "Fundraise reposted successfully":
    #         self.logger.info("Error Message Is: %s", result)
    #     else:
    #         assert False
    #         self.logger.info("*************** Fundraise reposted successfully Test Failed *************")
    #
    #
    #     self.logger.info("************** Post Fundraise - Positive Test  Ended Successfully  *************")
    #     self.driver.quit()


    # Review,Report,Copy link, Save, Not interest, Like, Superlike


    # Fund Review - Positive & Negative
    @pytest.mark.sanity
    def test_fundreview(self, setup):

        self.logger.info("********** Fund Review Test Started **********")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.pjt = projects(self.driver)
        self.fund = fundraise(self.driver)
        # self.l.clicksignin()
        # time.sleep(1)
        self.l.setUserName(self.username)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        # time.sleep(7)
        # self.pjt.selectionelement()
        # time.sleep(7)
        time.sleep(1)
        self.fund.clickfundraise()
        time.sleep(1)
        self.fund.clickFundthreedots()
        time.sleep(1)
        self.fund.clickFundreview()
        time.sleep(1)
        self.fund.clickFundreviewsubmit()
        time.sleep(1)

        error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = error_msg[0].text
        if result == "Rating is required":
            self.logger.info("Error Message Is: %s", result)
        else:
            assert False
            self.logger.info("*************** Fund Rating Negative Test Failed *************")


        time.sleep(1)
        self.fund.clickFundrating()
        time.sleep(1)
        self.fund.clickFundreviewsubmit()
        time.sleep(1)

        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = error_msg1[0].text
        if result == "Review comment is required.":
            self.logger.info("Error Message Is: %s", result)
        else:
            assert False
            self.logger.info("*************** Fund Review Negative Test Failed *************")

        time.sleep(1)
        self.fund.clickFundreviewtext()
        time.sleep(1)
        self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_fundreview.png")
        time.sleep(1)
        self.fund.clickFundreviewsubmit()
        time.sleep(1)

        error_msg2 = self.driver.find_elements(By.XPATH,
                                               "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = error_msg2[0].text
        if result == "Reviewed a fundraising successfully.":
            self.logger.info("Error Message Is: %s", result)
        else:
            assert False
            self.logger.info("*************** Fund Review Positive Test Failed *************")


        self.logger.info("************** Fund Review Test Ended Successfully *************")
        self.driver.quit()


    # Fund Report - Positive & Negative
    @pytest.mark.sanity
    def test_fundreport(self, setup):

        self.logger.info("********** Fund Report Test Started **********")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.pjt = projects(self.driver)
        self.fund = fundraise(self.driver)
        # self.l.clicksignin()
        # time.sleep(1)
        self.l.setUserName(self.username)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        # time.sleep(7)
        # self.pjt.selectionelement()
        # time.sleep(7)
        time.sleep(1)
        self.fund.clickfundraise()
        time.sleep(2)
        self.fund.clickFundthreedots()
        time.sleep(1)
        self.fund.clickFundreport()
        time.sleep(1)
        self.fund.clickFundreportsubmit()
        time.sleep(1)


        error_msg = self.driver.find_elements(By.XPATH,
                                              "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = error_msg[0].text
        if result == "Please type your comment.":
            self.logger.info("Error Message Is: %s", result)
        else:
            assert False
            self.logger.info("*************** Fund Report Negative Test Failed *************")


        time.sleep(1)
        self.fund.clickFundreporttext()
        time.sleep(1)
        self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_fundreport.png")
        time.sleep(1)
        self.fund.clickFundreportsubmit()
        time.sleep(1)

        error_msg1 = self.driver.find_elements(By.XPATH,
                                               "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = error_msg1[0].text
        if result == "Fundraising Reported":
            self.logger.info("Error Message Is: %s", result)
        else:
            assert False
            self.logger.info("*************** Fund Report Positive Test Failed *************")


        self.logger.info("************** Fund Report Test Ended Successfully *************")
        self.driver.quit()


    # Fund copy link
    @pytest.mark.sanity
    def test_fundcopylink(self, setup):

        self.logger.info("********** Fund Copy Link Test Started **********")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.pjt = projects(self.driver)
        self.fund = fundraise(self.driver)
        # self.l.clicksignin()
        # time.sleep(1)
        self.l.setUserName(self.username)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        # time.sleep(7)
        # self.pjt.selectionelement()
        # time.sleep(7)
        time.sleep(1)
        self.fund.clickfundraise()
        time.sleep(2)
        self.fund.clickFundthreedots()
        time.sleep(1)
        self.fund.clickFundcopylink()
        time.sleep(1)

        error_msg = self.driver.find_elements(By.XPATH,
                                              "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = error_msg[0].text
        if result == "Link copied":
            self.logger.info("Error Message Is: %s", result)
        else:
            assert False
            self.logger.info("*************** Link copied Test Failed *************")

        self.logger.info("************** Fund Copy Link Test Ended Successfully *************")
        self.driver.quit()


    # Fund Save/Unsave
    @pytest.mark.sanity
    def test_fundsave(self, setup):

        self.logger.info("********** Fund Save/Unsave Test Started **********")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.pjt = projects(self.driver)
        self.fund = fundraise(self.driver)
        # self.l.clicksignin()
        # time.sleep(1)
        self.l.setUserName(self.username)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        # time.sleep(7)
        # self.pjt.selectionelement()
        # time.sleep(7)
        time.sleep(1)
        self.fund.clickfundraise()
        time.sleep(1)
        self.fund.clickFundthreedots()
        time.sleep(1)
        self.fund.clickFundsave()
        time.sleep(1)

        error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = error_msg[0].text
        self.logger.info("Error Message Is: %s", result)

        time.sleep(1)
        self.fund.clickFundthreedots()
        time.sleep(1)
        self.fund.clickFundsave()
        time.sleep(1)

        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = error_msg1[0].text
        self.logger.info("Error Message Is: %s", result)

        self.logger.info("************** Fund Save/Unsave Test Ended Successfully *************")
        self.driver.quit()

    # Fund Not Interested
    @pytest.mark.sanity
    def test_fundnotinterested(self, setup):

        self.logger.info("********** Fund Not Interested Test Started **********")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.pjt = projects(self.driver)
        self.fund = fundraise(self.driver)
        # self.l.clicksignin()
        # time.sleep(1)
        self.l.setUserName(self.username)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        # time.sleep(7)
        # self.pjt.selectionelement()
        # time.sleep(7)
        time.sleep(1)
        self.fund.clickfundraise()
        time.sleep(1)
        self.fund.clickFundthreedots()
        time.sleep(1)
        self.fund.clickFundnotinterest()
        time.sleep(1)
        self.fund.clickFundnotinterestyes()
        time.sleep(1)

        error_msg = self.driver.find_elements(By.XPATH,
                                              "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = error_msg[0].text
        if result == "Fundraising notIntrested successfully.":
            self.logger.info("Error Message Is: %s", result)
        else:
            assert False
            self.logger.info("***************  Fund Not Interested Test Failed *************")

        self.logger.info("************** Fund Not Interested Test Ended Successfully *************")
        self.driver.quit()


    # Fund Like, Superlike
    @pytest.mark.sanity
    def test_fundlikeSuperlike(self, setup):

        self.logger.info("********** Fund Like & Superlike Test Started **********")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.pjt = projects(self.driver)
        self.fund = fundraise(self.driver)
        # self.l.clicksignin()
        # time.sleep(1)
        self.l.setUserName(self.username)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        # time.sleep(7)
        # self.pjt.selectionelement()
        # time.sleep(7)
        time.sleep(1)
        self.fund.clickfundraise()
        time.sleep(1)
        self.fund.clickFundlike()
        time.sleep(1)

        error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = error_msg[0].text
        self.logger.info("Error Message Is: %s", result)

        time.sleep(2)
        self.fund.clickFundlike()
        time.sleep(1)

        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = error_msg1[0].text
        self.logger.info("Error Message Is: %s", result)

        time.sleep(2)
        self.fund.clickFundsuperlike()
        time.sleep(1)

        error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = error_msg2[0].text
        self.logger.info("Error Message Is: %s", result)

        time.sleep(2)
        self.fund.clickFundsuperlike()
        time.sleep(1)

        error_msg3 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = error_msg3[0].text
        self.logger.info("Error Message Is: %s", result)

        self.logger.info("************** Fund Like & Superlike Test Ended Successfully *************")
        self.driver.quit()

    # # Fund - Open,Close,saved
    # @pytest.mark.sanity
    # def test_fundASOC(self, setup):
    #
    #     self.logger.info("********** Fund - Open Close Applied Saved Test Started **********")
    #     self.driver = setup
    #     self.driver.get(self.BaseURL)
    #     self.driver.maximize_window()
    #     self.l = Login(self.driver)
    #     self.pjt = projects(self.driver)
    #     self.ap = applyproject(self.driver)
    #     self.fund = fundraise(self.driver)
    #     # self.l.clicksignin()
    #     # time.sleep(1)
    #     self.l.setUserName(self.username)
    #     time.sleep(1)
    #     self.l.setPassword(self.password)
    #     time.sleep(1)
    #     self.l.clickLogin()
    #     time.sleep(5)
    #     self.ap.clickprofilenavbardroparrow()
    #     time.sleep(2)
    #     self.fund.clickfunddownarrow()
    #     time.sleep(1)
    #     self.fund.clickopenfund()
    #     time.sleep(1)
    #     self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_openfund.png")
    #     time.sleep(1)
    #     self.fund.clickopenfund3dots()
    #     time.sleep(1)
    #     self.fund.clickopenfundclose()
    #     time.sleep(1)
    #
    #
    #     error_msg = self.driver.find_elements(By.XPATH,
    #                                           "/html/body/div[1]/div/div/div/div[1]/div[2]")
    #     result = error_msg[0].text
    #     if result == "Fundraise closed":
    #         self.logger.info("Error Message Is: %s", result)
    #     else:
    #         assert False
    #         self.logger.info("*************** Fund has been closed successfully Test Failed *************")
    #
    #
    #     time.sleep(2)
    #     self.fund.clickclosedfund()
    #     time.sleep(1)
    #     self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_closedfund.png")
    #     time.sleep(1)
    #     self.fund.clickclosedfundrepost()
    #     time.sleep(1)
    #     self.fund.scrollfundrepostbutton()
    #     time.sleep(1)
    #     self.fund.clickfundrepostbutton()
    #     time.sleep(1)
    #
    #     error_msg1 = self.driver.find_elements(By.XPATH,
    #                                           "/html/body/div[1]/div/div/div[1]/div[1]/div[2]")
    #     result = error_msg1[0].text
    #     if result == "Fundraise reposted successfully":
    #         self.logger.info("Error Message Is: %s", result)
    #     else:
    #         assert False
    #         self.logger.info("***************  Fund Reposted  successfully Test Failed *************")
    #
    #
    #     time.sleep(2)
    #     self.ap.clickprofilenavbardroparrow()
    #     time.sleep(2)
    #     self.fund.clickfunddownarrow()
    #     time.sleep(1)
    #     self.fund.clicksavedfund()
    #     time.sleep(1)
    #     self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_savedfund.png")
    #     time.sleep(1)
    #
    #     self.logger.info("************** Fund - Open Close Saved Test Ended Successfully *************")
    #     self.driver.quit