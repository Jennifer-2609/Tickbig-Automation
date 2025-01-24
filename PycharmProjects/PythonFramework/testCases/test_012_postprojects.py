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


class Test_012_Projects:

    BaseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    # Project type - Negative Testcase1
    # @pytest.mark.sanity
    def test_projectnegative1(self, setup):

        self.logger.info("********** Test_012 Projects - Project type Negative Test 1 **********")
        self.logger.info("********** Post Project - Project type Negative Test 1 Started **********")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.pjt = projects(self.driver)
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
        self.pjt.clickPjtButton()
        time.sleep(2)
        self.pjt.clickPostPjtButton()
        time.sleep(5)
        self.pjt.scrollPostPjt()
        time.sleep(5)
        self.pjt.clickPostPjtFinalButton()
        time.sleep(5)
        self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_pjtsnegative1.png")
        time.sleep(2)
        self.pjt.setpjtskill1()
        time.sleep(2)
        self.pjt.clickPostPjtFinalButton()
        time.sleep(2)


        error_msg1 = self.driver.find_elements(By.XPATH,"/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[2]/div/p")
        result = error_msg1[0].text
        if result == "Project Name is required":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Project Name is required Test Passed *************")
        else:
            assert False
            self.logger.info("***************  Project Name is required Test Failed *************")


        error_msg2 = self.driver.find_elements(By.XPATH,"/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[3]/p")
        result = error_msg2[0].text
        if result == "Project Sector is required":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Project Sector is required Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Project Sector is required Test Failed *************")


        error_msg3 = self.driver.find_elements(By.XPATH,"/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/p[1]")
        result = error_msg3[0].text
        if result == "Invalid Price range":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Invalid Price range Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Invalid Price range Test Failed *************")

        error_msg4 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/p[2]")
        result = error_msg4[0].text
        if result == "Invalid Price range":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Invalid Price range Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Invalid Price range Test Failed *************")

        error_msg5 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/p[3]")
        result = error_msg5[0].text
        if result == "Payout or Currency type is missing.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Payout or Currency type is missing Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Payout or Currency type is missing Test Failed *************")

        time.sleep(2)
        self.pjt.scrollPostPjt()
        time.sleep(5)

        error_msg6 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[5]/div[1]/div/p")
        result = error_msg6[0].text
        if result == "Project Requirement is required":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Project Requirement is required Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Project Requirement is required Test Failed *************")

        error_msg7 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[6]/div/p")
        result = error_msg7[0].text
        if result == "Responsibility is required.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Responsibility is required Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Responsibility is required Test Failed *************")

        error_msg8 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[9]/p")
        result = error_msg8[0].text
        if result == "Who can apply is required.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Who can apply is required Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Who can apply is required Test Failed *************")

        self.logger.info("************** Post Project - Project type Negative Test 1 Passed Successfully *************")
        self.driver.quit()


    # Project type - Negative Testcase 2
    # @pytest.mark.sanity
    def test_projectnegative2(self, setup):

        self.logger.info("********** Test_012 Projects - Project type Negative Test 2 **********")
        self.logger.info("********** Post Project - project type Negative Test 2 Started **********")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.pjt = projects(self.driver)
        self.l.clicksignin()
        time.sleep(1)
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
        time.sleep(5)
        self.pjt.scrollPostPjt()
        time.sleep(5)
        self.pjt.clickPostPjtFinalButton()
        time.sleep(5)
        self.pjt.setpjtskill1()
        time.sleep(2)
        self.pjt.clickPostPjtFinalButton()
        time.sleep(2)
        self.pjt.setmin1()
        time.sleep(2)
        self.pjt.setmax1()
        time.sleep(2)


        error_msg2 = self.driver.find_elements(By.XPATH,
                                                   "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/p[1]")
        result = error_msg2[0].text
        if result == "Min value should be less than or equal to Max value":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Min Max value negative Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Min Max value negative Test Failed *************")


        self.logger.info("************** Post Project - Project type Negative Test 2 Passed Successfully *************")
        self.driver.quit()


    # Project type - Positive Testcase
    # @pytest.mark.sanity
    def test_projecttypepositive(self, setup):

        self.logger.info("********** Test_012 Projects - Project type Positive Test  **********")
        self.logger.info("********** Post Project - Project type Positive Test 2 Started **********")
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
        self.pjt.scrollPostPjt()
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
        self.pjt.clickPostPjtFinalButton()
        time.sleep(2)


        error_msg2 = self.driver.find_elements(By.XPATH,"/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = error_msg2[0].text
        if result == "Project created successfully":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Project Created Successfully Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Project Created Successfully Test Failed *************")


        self.logger.info("************** Post Project - Project type Positive Test Passed Successfully *************")
        self.driver.quit()


    # Staff Augmentation - Negative Testcase 1
    # @pytest.mark.sanity
    def test_staffnegative1(self, setup):

        self.logger.info("********** Test_012 Projects - Staff Augmentation Negative Test 1 **********")
        self.logger.info("********** Post Project - Staff Augmentation Negative Test 1 Started **********")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.pjt = projects(self.driver)
        self.l.clicksignin()
        time.sleep(1)
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
        self.pjt.scrollPostPjt1()
        time.sleep(5)
        self.pjt.clickPostPjtFinalButton1()
        time.sleep(5)
        self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_pjtsstaffnegative1.png")
        time.sleep(2)
        self.pjt.setstaffskill1()
        time.sleep(2)
        self.pjt.clickPostPjtFinalButton1()
        time.sleep(2)

        error_msg1 = self.driver.find_elements(By.XPATH,"/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[2]/div/p")
        result = error_msg1[0].text
        if result == "Project Name is required":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Project Name is required Test Passed *************")
        else:
            assert False
            self.logger.info("***************  Project Name is required Test Failed *************")


        error_msg2 = self.driver.find_elements(By.XPATH,"/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[3]/p")
        result = error_msg2[0].text
        if result == "Project Sector is required":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Project Sector is required Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Project Sector is required Test Failed *************")


        error_msg3 = self.driver.find_elements(By.XPATH,"/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/p[1]")
        result = error_msg3[0].text
        if result == "Invalid Price range":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Invalid Price range Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Invalid Price range Test Failed *************")

        error_msg4 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/p[2]")
        result = error_msg4[0].text
        if result == "Invalid Price range":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Invalid Price range Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Invalid Price range Test Failed *************")

        error_msg5 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/p[3]")
        result = error_msg5[0].text
        if result == "Payout or Currency type is missing.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Payout or Currency type is missing Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Payout or Currency type is missing Test Failed *************")

        error_msg9 = self.driver.find_elements(By.XPATH,
                                               "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[4]/p")
        result = error_msg9[0].text
        if result == "Contract Period is required":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Contract Period is required Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Contract Period is required Test Failed *************")


        error_msg10 = self.driver.find_elements(By.XPATH,
                                               "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[5]/p")
        result = error_msg10[0].text
        if result == "Positions is required":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Positions is required Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Positions is required Test Failed *************")


        error_msg11 = self.driver.find_elements(By.XPATH,
                                                "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[6]/p")
        result = error_msg11[0].text
        if result == "Employment Type is required":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Employment Type is required Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Employment Type is required Test Failed *************")


        error_msg6 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[8]/div[1]/div/p")
        result = error_msg6[0].text
        if result == "Project Requirement is required":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Project Requirement is required Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Project Requirement is required Test Failed *************")


        error_msg7 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[9]/div/p")
        result = error_msg7[0].text
        if result == "Responsibility is required.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Responsibility is required Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Responsibility is required Test Failed *************")


        error_msg8 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[12]/p")
        result = error_msg8[0].text
        if result == "Who can apply is required.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Who can apply is required Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Who can apply is required Test Failed *************")


        self.logger.info("************** Post Project - Staff Augmentation Negative Test 1 Passed Successfully *************")
        self.driver.quit()


    # Staff Augmentation - Negative Testcase 2
    # @pytest.mark.sanity
    def test_staffnegative2(self, setup):

        self.logger.info("********** Test_012 Projects - Staff Augmentation Negative Test 2 **********")
        self.logger.info("********** Post Project - Staff Augmentation Negative Test 2 Started **********")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.pjt = projects(self.driver)
        self.l.clicksignin()
        time.sleep(1)
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
        time.sleep(5)
        self.pjt.clickstaffdrop()
        time.sleep(2)
        self.pjt.clickselectstaff()
        time.sleep(5)
        self.pjt.scrollPostPjt1()
        time.sleep(5)
        self.pjt.clickPostPjtFinalButton1()
        time.sleep(5)
        self.pjt.setstaffskill1()
        time.sleep(2)
        self.pjt.clickPostPjtFinalButton1()
        time.sleep(2)
        self.pjt.setstaffmin1()
        time.sleep(2)
        self.pjt.setstaffmax1()
        time.sleep(2)


        error_msg2 = self.driver.find_elements(By.XPATH,
                                                   "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/p[1]")
        result = error_msg2[0].text
        if result == "Min value should be less than or equal to Max value":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Min Max value negative Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Min Max value negative Test Failed *************")


        self.logger.info("************** Post Project - Staff Augmentation Negative Test 2 Passed Successfully *************")
        self.driver.quit()


    # Staff Augmentation - Positive Testcase
    # @pytest.mark.sanity
    def test_staffpositive(self, setup):

        self.logger.info("********** Test_012 Projects - Staff Augmentation Positive Test  **********")
        self.logger.info("********** Post Project - Staff Augmentation Positive Test 2 Started **********")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.pjt = projects(self.driver)
        self.l.clicksignin()
        self.ap = applyproject(self.driver)
        time.sleep(1)
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
        self.pjt.scrollstaffpricing()
        time.sleep(5)
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
        self.pjt.clickPostPjtFinalButton1()
        time.sleep(2)

        error_msg2 = self.driver.find_elements(By.XPATH,"/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = error_msg2[0].text
        if result == "Project created successfully":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Project Created Successfully Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Project Created Successfully Test Failed *************")


        self.logger.info("************** Post Project - Staff Augmentation Positive Test Passed Successfully *************")
        self.driver.quit()