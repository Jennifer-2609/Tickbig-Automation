import configparser
import pytest
import time
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import Login
from pageObjects.applyproject import applyproject
from pageObjects.postprojects import projects
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


config=configparser.ConfigParser()
config.read('C:\\Users\\jenni\\PycharmProjects\\PythonFramework\\Configurations\\config.ini')


class Test_017_ProjectSubscription:

    BaseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    # Project type - Post subscription
    # @pytest.mark.sanity
    def test_projecttypesubscription(self, setup):

        self.logger.info("********** Test_017 Projects - Project type Subscription Test  **********")
        self.logger.info("********** Post Project - Project type Subscription Test Started **********")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.pjt = projects(self.driver)
        self.ap = applyproject(self.driver)
        self.l.clicksignin()
        time.sleep(1)
        self.driver.refresh()
        time.sleep(3)
        self.l.setUserName(self.username)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        # time.sleep(2)
        time.sleep(3)
        self.pjt.selectionelement()
        time.sleep(3)
        self.pjt.clickPjtButton()
        time.sleep(2)
        self.pjt.clickPostPjtButton()
        time.sleep(2)
        self.pjt.setpjtname1()
        time.sleep(2)
        self.pjt.selectsectortype1()
        time.sleep(2)
        self.pjt.selectpricingtype1()
        time.sleep(2)
        self.pjt.selectpricingtype2()
        time.sleep(2)
        self.pjt.setmin2()
        time.sleep(2)
        self.pjt.setmax2()
        time.sleep(2)
        self.pjt.setpjtreq1()
        time.sleep(2)
        self.pjt.setpjtresponsibility1()
        time.sleep(2)
        self.pjt.setpjtskill1()
        time.sleep(2)
        self.pjt.clicknextskill1()
        time.sleep(2)
        self.pjt.setpjtskill2()
        time.sleep(2)
        self.pjt.scrollPostPjt()
        time.sleep(2)
        self.pjt.setwhocanapply1()
        time.sleep(2)
        self.ap.selectWhocanapplyAccount1()
        time.sleep(2)
        self.ap.selectWhocanapplyAccount1()
        time.sleep(2)
        self.ap.selectWhocanapplyAccount1()
        time.sleep(2)
        self.ap.selectWhocanapplyAccount1()
        time.sleep(2)
        self.ap.selectWhocanapplyAccount1()
        time.sleep(2)
        self.ap.selectWhocanapplyAccount1()
        time.sleep(2)
        self.ap.selectWhocanapplyAccount1()
        time.sleep(2)
        self.pjt.clickonbehalfofpjtpost()
        time.sleep(2)
        self.pjt.clickbehalfchooseonepjtpost()
        time.sleep(2)
        self.pjt.clickPostPjtFinalButton()
        time.sleep(1)

        error_msg2 = self.driver.find_elements(By.XPATH,"/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = error_msg2[0].text
        if result == "You need to subscribe to create a New Project.":
            self.logger.info("Error Message Is: %s", result)
        else:
            assert False
            self.logger.info("*************** You need to subscribe to create a New Project Failed *************")


        self.logger.info("************** Post Project - Project type Subscription Test Passed Successfully *************")
        self.driver.quit()

    # Staff Augmentation - Post Subscription
    # @pytest.mark.sanity
    def test_pjtstaffsubscription(self, setup):

        self.logger.info("********** Test_017 Projects - Staff Augmentation Subcription Test  **********")
        self.logger.info("********** Post Project - Staff Augmentation Subscription Test Started **********")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.pjt = projects(self.driver)
        self.ap = applyproject(self.driver)
        self.l.clicksignin()
        time.sleep(1)
        self.driver.refresh()
        time.sleep(3)
        self.l.setUserName(self.username)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        # time.sleep(2)
        time.sleep(3)
        self.pjt.selectionelement()
        time.sleep(3)
        self.pjt.clickPjtButton()
        time.sleep(2)
        self.pjt.clickPostPjtButton()
        time.sleep(2)
        self.pjt.clickstaffdrop()
        time.sleep(2)
        self.pjt.clickselectstaff()
        time.sleep(5)
        self.pjt.setpjtname2()
        time.sleep(2)
        self.pjt.selectsectortype2()
        time.sleep(2)
        self.pjt.setcontractperiod()
        time.sleep(2)
        self.pjt.setnoofposition()
        time.sleep(2)
        self.pjt.setemploymenttype()
        time.sleep(2)
        # self.pjt.scrollstaffpricing()
        # time.sleep(5)
        self.pjt.selectpricingstaff1()
        time.sleep(2)
        self.pjt.selectpricingstaff2()
        time.sleep(2)
        self.pjt.setstaffmin2()
        time.sleep(2)
        self.pjt.setstaffmax2()
        time.sleep(2)
        self.pjt.setpjtreq2()
        time.sleep(2)
        self.pjt.setpjtresponsibility2()
        time.sleep(2)
        self.pjt.setstaffskill1()
        time.sleep(2)
        self.pjt.clicknextskill2()
        time.sleep(2)
        self.pjt.setstaffskill2()
        time.sleep(2)
        self.pjt.scrollPostPjt1()
        time.sleep(2)
        self.pjt.setwhocanapply2()
        time.sleep(2)
        self.ap.selectWhocanapplyAccount2()
        time.sleep(2)
        self.ap.selectWhocanapplyAccount2()
        time.sleep(2)
        self.ap.selectWhocanapplyAccount2()
        time.sleep(2)
        self.ap.selectWhocanapplyAccount2()
        time.sleep(2)
        self.ap.selectWhocanapplyAccount2()
        time.sleep(2)
        self.ap.selectWhocanapplyAccount2()
        time.sleep(2)
        self.ap.selectWhocanapplyAccount2()
        time.sleep(2)
        self.pjt.clickonbehalfofstaffpost()
        time.sleep(2)
        self.pjt.clickbehalfchooseonestaffpost()
        time.sleep(4)
        self.pjt.clickPostPjtFinalButton1()
        time.sleep(1)

        error_msg2 = self.driver.find_elements(By.XPATH,"/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = error_msg2[0].text
        if result == "You need to subscribe to create a New Project.":
            self.logger.info("Error Message Is: %s", result)
        else:
            assert False
            self.logger.info("*************** You need to subscribe to create a New Project Failed *************")


        self.logger.info("************** Post Project - Staff Augmentation Positive Test Passed Successfully *************")
        self.driver.quit()


    # Staff Augmentation - Apply - Subscription
    # @pytest.mark.sanity
    def test_pjtstaffapplysubscrition(self, setup):

        self.logger.info("********** Staff Augmentation Apply Subscription Test Started **********")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.pjt = projects(self.driver)
        self.ap = applyproject(self.driver)
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

        if result == "You need to subscribe before apply project.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** You need to subscribe before apply project Test Passed *************")
        else:
            assert False
            self.logger.info("*************** You need to subscribe before apply project Test Failed *************")


        self.logger.info("************** Staff Augmentation Apply Subscription Test Ended Successfully *************")
        self.driver.quit()


    # Project type - Apply - Subscription Test
    # @pytest.mark.sanity
    def test_projecttypeapplysubscription(self, setup):

        self.logger.info("********** Project Type -  Apply Subscription Test Started **********")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.pjt = projects(self.driver)
        self.ap = applyproject(self.driver)
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
        self.ap.clickbehalfchooseonepjtapply()  # Manually select on behalf of accounts from the dropdown
        time.sleep(5)
        self.ap.clickpjttypesubmit()
        time.sleep(1)

        error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = error_msg[0].text

        if result == "You need to subscribe before apply project":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** You need to subscribe before apply project Test Passed *************")
        else:
            assert False
            self.logger.info("*************** You need to subscribe before apply project Test Failed *************")


        self.logger.info("************** Project Type -  Apply Subscription Test Ended Successfully *************")
        self.driver.quit()