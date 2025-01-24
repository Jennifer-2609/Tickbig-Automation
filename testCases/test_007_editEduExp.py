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


class Test_007_EditEduExp:

    BaseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    ExpDesgination = ReadConfig.getExpDesgination()
    ExpCompname = ReadConfig.getExpCompname()
    JobLocation = ReadConfig.getJobLocation()
    StartYearExp = ReadConfig.getStartYearExp()
    EndYearExp = ReadConfig.getEndYearExp()

    qualification = ReadConfig.getqualification()
    instname = ReadConfig.getinstname()
    InstLocation = ReadConfig.getInstLocation()
    StartYearEdu = ReadConfig.getStartYearEdu()
    EndYearEdu = ReadConfig.getEndYearEdu()

    # @pytest.mark.sanity
    def test_editEduExpPositive(self,setup):
        # Positive Test
        self.logger.info("********** Test_007_Edit Edu & Exp - Positive **********")
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

        # Add Experience
        time.sleep(3)
        # self.pA.scrollEduExp()
        self.p.scrollExpertise()
        time.sleep(3)
        self.pA.clickEduExp()
        time.sleep(1)
        self.pA.clickAddExp()
        time.sleep(1)
        self.pA.textdesignExp(self.ExpDesgination)
        time.sleep(1)
        self.pA.textcompnameExp(self.ExpCompname)
        time.sleep(1)
        self.pA.textjoblocExp(self.JobLocation)
        time.sleep(5)
        self.pA.selectEmploymenttype()
        time.sleep(5)
        self.pA.textstartyrExp(self.StartYearExp)
        time.sleep(1)
        self.pA.textendyrExp(self.EndYearExp)
        time.sleep(1)
        self.pA.clickSaveExp()
        time.sleep(1)

        toast_msg = self.driver.find_elements(By.XPATH,"/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = toast_msg[0].text
        print(result)

        if result=="Experience updated successfully.":
            assert True
            self.logger.info("********** Experience updated successfully passed *********")
        else:
            assert False
            self.logger.info("********** Experience updated successfully failed *********")

        # Add Education
        time.sleep(1)
        self.pA.clickEduExp()
        time.sleep(1)
        self.pA.clickEducation()
        time.sleep(1)
        self.pA.clickAddEdu()
        time.sleep(1)
        self.pA.textQualificationEdu(self.qualification)
        time.sleep(1)
        self.pA.textInstnameEdu(self.instname)
        time.sleep(3)
        self.pA.scrollSaveEdu()
        time.sleep(3)
        self.pA.textInstlocExp(self.InstLocation)
        time.sleep(3)
        self.pA.textstartyrEdu(self.StartYearEdu)
        time.sleep(5)
        # self.pA.scrollendyrEdu()
        # time.sleep(2)
        self.pA.textendyrEdu(self.EndYearEdu)
        time.sleep(5)
        self.pA.clickSaveEdu()
        time.sleep(1)

        toast_msgA = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        resultA = toast_msgA[0].text
        print(resultA)

        if resultA == "Qualifications updated successfully.":
            assert True
            self.logger.info("********** Education updated successfully passed *********")
        else:
            assert False
            self.logger.info("********** Education updated successfully failed *********")

        # Delete Experience using "Delete" button
        time.sleep(1)
        self.pA.clickEduExp()
        time.sleep(1)
        self.pA.clickDelExp()
        time.sleep(1)
        self.pA.clicksaveExpDel()
        time.sleep(1)

        toast_msgB = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        resultB = toast_msgB[0].text
        print(resultB)

        if resultB == "Experience updated successfully.":
            assert True
            self.logger.info("********** Experience Deleted successfully passed *********")
        else:
            assert False
            self.logger.info("********** Experience Deleted successfully failed *********")

        # Delete Education using "Delete" button
        time.sleep(1)
        self.pA.clickEduExp()
        time.sleep(1)
        self.pA.clickEducation()
        time.sleep(1)
        self.pA.clickDelEdu()
        time.sleep(1)
        self.pA.clicksaveEduDel()
        time.sleep(1)

        toast_msgC = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        resultC = toast_msgC[0].text
        print(resultC)

        if resultC == "Qualifications updated successfully.":
            assert True
            self.logger.info("********** Education Deleted successfully passed *********")
        else:
            assert False
            self.logger.info("********** Education Deleted successfully failed *********")


        # self.logger.info("********** Edit Edu & Exp Positive Test passed *********")
        # self.logger.info("********** Edit Edu & Exp Positive Test failed *********")
        self.driver.close()
        self.logger.info("********** Ending Edit Edu & Exp Positive Test *********")

    # @pytest.mark.sanity
    def test_editEduExpNegative(self,setup):
        # Positive Test
        self.logger.info("********** Test_007_Edit Edu & Exp - Negative **********")
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

        # Add Experience Negative
        time.sleep(3)
        # self.pA.scrollEduExp()
        self.p.scrollExpertise()
        time.sleep(3)
        self.pA.clickEduExp()
        time.sleep(1)
        self.pA.clickAddExp()
        time.sleep(1)
        self.pA.clickSaveExp()
        time.sleep(2)

        self.driver.save_screenshot(".\\Screenshots\\" + "test_negStartDateExp.png")
        time.sleep(1)
        self.logger.info("********** Validation for Start Date for Experience Screenshot taken successfully *********")
        time.sleep(1)
        self.pA.textstartyrExp(self.StartYearExp)
        time.sleep(1)
        self.pA.clickSaveExp()
        time.sleep(2)

        toast_msgD = self.driver.find_elements(By.XPATH,"/html/body/div[3]/div[3]/main/section/div[3]/div/div/div[1]/div/div/form/div[2]/div/div[1]/div")
        resultD = toast_msgD[0].text
        print(resultD)

        if resultD=="Designation is required":
            assert True
            self.logger.info("********** Desgination Negative Test passed *********")
        else:
            assert False
            self.logger.info("********** Desgination Negative Test failed *********")

        time.sleep(2)

        toast_msgE = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/main/section/div[3]/div/div/div[1]/div/div/form/div[2]/div/div[2]/div")
        resultE = toast_msgE[0].text
        print(resultE)

        if resultE == "Company Name is required":
            assert True
            self.logger.info("********** Company Name Negative Test passed *********")
        else:
            assert False
            self.logger.info("********** Company Name Negative Test failed *********")

        time.sleep(2)

        toast_msgF = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/main/section/div[3]/div/div/div[1]/div/div/form/div[2]/div/div[3]/div")
        resultF = toast_msgF[0].text
        print(resultF)

        if resultF == "Job Location is required":
            assert True
            self.logger.info("********** Job Location Negative Test passed *********")
        else:
            assert False
            self.logger.info("********** Job Location Negative Test failed *********")

        time.sleep(2)

        toast_msgG = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/main/section/div[3]/div/div/div[1]/div/div/form/div[2]/div/div[4]/p")
        resultG = toast_msgG[0].text
        print(resultG)

        if resultG == "Employment Type is required.":
            assert True
            self.logger.info("********** Employment Type Negative Test passed *********")
        else:
            assert False
            self.logger.info("********** Employment Type Negative Test failed *********")

        time.sleep(2)
        self.pA.textdesignExp(self.ExpDesgination)
        time.sleep(1)
        self.pA.textcompnameExp(self.ExpCompname)
        time.sleep(1)
        self.pA.textjoblocExp(self.JobLocation)
        time.sleep(2)
        self.pA.validatestartyrExp()
        time.sleep(1)
        self.pA.clickSaveExp()
        time.sleep(2)

        toast_msgO = self.driver.find_elements(By.XPATH,"/html/body/div[3]/div[3]/main/section/div[3]/div/div/div[1]/div/div/form/div[2]/div/div[5]/div")
        resultO = toast_msgO[0].text
        print(resultO)

        if resultO == "Dates in the future are not permitted":
            assert True
            self.logger.info("********** Start Year Invalid Year Negative Test passed *********")
        else:
            assert False
            self.logger.info("********** Start Year Invalid Year Negative Test failed *********")

        # Add Education Negative
        time.sleep(2)
        self.pA.clickEducation()
        time.sleep(1)
        self.pA.clickAddEdu()
        time.sleep(1)
        self.pA.scrollSaveEdu()
        time.sleep(1)
        self.pA.clickSaveEdu()
        time.sleep(1)
        self.pA.textstartyrEdu(self.StartYearEdu)
        time.sleep(1)
        self.pA.clickSaveEdu()
        time.sleep(2)

        toast_msgI = self.driver.find_elements(By.XPATH,"/html/body/div[3]/div[3]/main/section/div[3]/div/div/div[2]/div/div/form/div[2]/div/div[1]/div")
        resultI = toast_msgI[0].text
        print(resultI)

        if resultI == "Qualification is required":
            assert True
            self.logger.info("********** Qualification Negative Test passed *********")
        else:
            assert False
            self.logger.info("********** Qualification Negative Test failed *********")

        time.sleep(2)

        toast_msgJ = self.driver.find_elements(By.XPATH,"/html/body/div[3]/div[3]/main/section/div[3]/div/div/div[2]/div/div/form/div[2]/div/div[2]/div")
        resultJ = toast_msgJ[0].text
        print(resultJ)

        if resultJ == "Institute Name is required":
            assert True
            self.logger.info("********** Institute Name Negative Test passed *********")
        else:
            assert False
            self.logger.info("********** Institute Name Negative Test failed *********")

        time.sleep(2)

        toast_msgK = self.driver.find_elements(By.XPATH,"/html/body/div[3]/div[3]/main/section/div[3]/div/div/div[2]/div/div/form/div[2]/div/div[3]/div")
        resultK = toast_msgK[0].text
        print(resultK)

        if resultK == "Institute Location is required":
            assert True
            self.logger.info("********** Institute Location Negative Test passed *********")
        else:
            assert False
            self.logger.info("********** Institute Location Negative Test failed *********")

        time.sleep(2)

        #  Validation for Start Date (Education)
        time.sleep(2)
        self.pA.textQualificationEdu(self.qualification)
        time.sleep(1)
        self.pA.textInstnameEdu(self.instname)
        time.sleep(3)
        self.pA.scrollSaveEdu()
        time.sleep(3)
        self.pA.textInstlocExp(self.InstLocation)
        time.sleep(3)
        self.pA.validatestartyrEdu()
        time.sleep(3)
        self.pA.clickSaveEdu()
        time.sleep(2)

        toast_msgN = self.driver.find_elements(By.XPATH,"/html/body/div[3]/div[3]/main/section/div[3]/div/div/div[2]/div/div/form/div[2]/div/div[4]/div")
        resultN = toast_msgN[0].text
        print(resultN)

        if resultN == "Dates in the future are not permitted":
            assert True
            self.logger.info("********** Start Year Negative Test passed *********")
        else:
            assert False
            self.logger.info("********** Start Year Negative Test failed *********")


        self.driver.close()
        self.logger.info("********** Ending Edit Edu & Exp Negative Test *********")

    # @pytest.mark.sanity
    def test_editEduExpPositive1(self, setup):
            # Delete Test
            self.logger.info("********** Test_007_Edit Edu & Exp - Delete **********")
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

            # Add Experience
            time.sleep(3)
            # self.pA.scrollEduExp()
            self.p.scrollExpertise()
            time.sleep(3)
            self.pA.clickEduExp()
            time.sleep(1)
            self.pA.clickAddExp()
            time.sleep(1)
            self.pA.textdesignExp(self.ExpDesgination)
            time.sleep(1)
            self.pA.textcompnameExp(self.ExpCompname)
            time.sleep(1)
            self.pA.textjoblocExp(self.JobLocation)
            time.sleep(5)
            self.pA.selectEmploymenttype()
            time.sleep(5)
            self.pA.textstartyrExp(self.StartYearExp)
            time.sleep(1)
            self.pA.textendyrExp(self.EndYearExp)
            time.sleep(1)
            self.pA.clickSaveExp()
            time.sleep(2)

            toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
            result = toast_msg[0].text
            print(result)

            if result == "Experience updated successfully.":
                assert True
                self.logger.info("********** Experience updated successfully passed *********")
            else:
                assert False
                self.logger.info("********** Experience updated successfully failed *********")

            time.sleep(2)
            self.pA.mousehoverexpcardDel()
            time.sleep(2)

            toast_msgA = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
            resultA = toast_msgA[0].text
            print(resultA)

            if resultA == "Experience deleted.":
                assert True
                self.logger.info("********** Experience Deleted successfully using Bin symbol *********")
            else:
                assert False
                self.logger.info("********** Experience Not Deleted using Bin symbol *********")


            self.driver.close()
            self.logger.info("********** Ending Edit Edu & Exp Bin Delete Test *********")