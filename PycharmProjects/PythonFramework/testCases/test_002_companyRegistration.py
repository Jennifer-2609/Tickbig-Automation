import configparser
from telnetlib import EC

import pytest
import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.LoginPage import Login
from pageObjects.Registration_companyPage import companyRegistration
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


config=configparser.ConfigParser()
config.read('C:\\Users\\jenni\\PycharmProjects\\PythonFramework\\Configurations\\config.ini')


class Test_002_CompanyRegistration:

    BaseURL = ReadConfig.getApplicationURL()
    type=ReadConfig.getType()
    email=ReadConfig.getNewemail()
    emailone = ReadConfig.getNewemailone()
    newpassword=ReadConfig.getNewpwd()
    confirmpwd=ReadConfig.getConfirmpwd()
    compname=ReadConfig.getcompname()
    brandname=ReadConfig.getbrandname()
    mobnum=ReadConfig.getmobnum()
    lengthpassword=ReadConfig.getlengthpassword()
    lengthemail=ReadConfig.getlengthemail()

    # username = ReadConfig.getUseremail()
    # password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    # @pytest.mark.sanity
    def test_positivecompanyRegistration(self,setup):
        self.logger.info("********** Test_002_CompanyRegistration **********")
        self.driver=setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l=Login(self.driver)
        self.CR=companyRegistration(self.driver)
        time.sleep(1)
        self.CR.clickRegistration()
        time.sleep(1)
        self.CR.clickCompany()
        time.sleep(1)
        self.CR.clickChoosecategory()
        time.sleep(1)
        self.CR.selectCompanytype(self.type)
        time.sleep(1)
        self.CR.clickNextButton()
        time.sleep(1)
        # self.email=random_generator()+"@gmail.com"
        time.sleep(1)
        self.CR.setNewEmail(self.email)
        time.sleep(1)
        self.CR.setNewPassword(self.newpassword)
        time.sleep(1)
        self.CR.setConfirmpwd(self.confirmpwd)
        time.sleep(1)
        self.CR.clickSecnext()
        time.sleep(1)
        self.CR.setCompanyname(self.compname)
        time.sleep(1)
        self.CR.setBrandname(self.brandname)
        time.sleep(1)
        self.CR.setMobilenum(self.mobnum)
        time.sleep(2)
        self.CR.clickAgreejoin()
        time.sleep(30)
        # self.CR.typeOTP()
        # time.sleep(1)
        self.CR.clickVerifyjoin()
        time.sleep(2)

        self.logger.info("*********** OTP verified info **********")
        self.logger.info("*********** OTP verified validation started **********")

        time.sleep(2)
        toast_msg = self.driver.find_elements(By.XPATH,"/html/body/div[1]/div")
        result = toast_msg[0].text
        print(result)

        self.driver.close()
        self.logger.info("********** Ending Company Registration Test *********")


    # @pytest.mark.sanity
    def test_Signupnegative1Home(self, setup):#Email & Password & Confirm password is required for the signup
        self.logger.info("*************** SignUp Test *************")
        self.logger.info("************** Signup negative 1 test *************")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.CR=companyRegistration(self.driver)
        time.sleep(1)
        self.CR.clickRegistration()
        time.sleep(1)
        self.CR.clickCompany()
        time.sleep(1)
        self.CR.clickChoosecategory()
        time.sleep(1)
        self.CR.selectCompanytype(self.type)
        time.sleep(1)
        self.CR.clickNextButton()
        time.sleep(1)
        self.CR.clickSecnext()
        time.sleep(1)
        self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_sigupnegative1.png")
        print("Screenshot saved.")
        time.sleep(5)

        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[2]/section/form/div[1]/p")
        result = error_msg1[0].text
        if result == "email is required":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** Email is required test passed successfully *************")
        else:
           assert False
           self.logger.info("*************** Email is required test failed *************")

        error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[2]/section/form/div[2]/p")
        result = error_msg2[0].text
        if result == "Password is required":
            self.logger.info("Error Message Is: %s", result)


            assert True
            self.logger.info("*************** Password is required test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Password is required test failed *************")

        error_msg3 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[2]/section/form/div[3]/p")
        result = error_msg3[0].text
        if result == "Confirm Password is required":
            self.logger.info("Error Message Is: %s", result)

            assert True
            self.logger.info("*************** Confirm Password is required test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Confirm Password is required test failed *************")

        self.logger.info("************** Signup negative 1 test passed *************")
        self.driver.quit()

    # @pytest.mark.sanity
    def test_Signupnegative2Home(self, setup):#Email & Password is too length for the signup
        self.logger.info("*************** SignUp Test *************")
        self.logger.info("************** Signup negative 2 test *************")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.CR=companyRegistration(self.driver)
        time.sleep(1)
        self.CR.clickRegistration()
        time.sleep(1)
        self.CR.clickCompany()
        time.sleep(1)
        self.CR.clickChoosecategory()
        time.sleep(1)
        self.CR.selectCompanytype(self.type)
        time.sleep(1)
        self.CR.clickNextButton()
        time.sleep(1)
        self.CR.clickSecnext()
        time.sleep(1)
        self.CR.typeLenemail(self.lengthemail)
        time.sleep(3)
        self.CR.typeLenpassword(self.lengthpassword)
        time.sleep(3)
        self.CR.setConfirmpwd(self.confirmpwd)
        time.sleep(3)
        self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_sigupnegative2.png")
        print("Screenshot saved.")

        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[2]/section/form/div[1]/p")
        result = error_msg1[0].text
        if result == "Email Id should not be more than 128 characters.":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** Email length test passed successfully *************")
        else:
           assert False
           self.logger.info("*************** Email length test failed *************")

        error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[2]/section/form/div[2]/p")
        result = error_msg2[0].text
        if result == "Password length should not exceed 128 characters":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Password length test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Password length test failed *************")

        error_msg3 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[2]/section/form/div[3]/p")
        result = error_msg3[0].text
        if result == "The passwords don't match.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Incorrect confirm password  test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Incorrect confirm password test failed *************")

        self.logger.info("************** Successfully Signup negative 2 test Passed *************")
        self.driver.quit()

    # @pytest.mark.sanity
    def test_Signupnegative3Home(self, setup):#Email & Password is too short for the signup
        self.logger.info("*************** SignUp Test *************")
        self.logger.info("************** Signup negative 3 test *************")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.CR=companyRegistration(self.driver)
        time.sleep(1)
        self.CR.clickRegistration()
        time.sleep(1)
        self.CR.clickCompany()
        time.sleep(1)
        self.CR.clickChoosecategory()
        time.sleep(1)
        self.CR.selectCompanytype(self.type)
        time.sleep(1)
        self.CR.clickNextButton()
        time.sleep(1)
        self.CR.clickSecnext()
        time.sleep(3)
        self.CR.typeShortemail()
        time.sleep(3)
        self.CR.typeShortpassword()
        time.sleep(3)
        self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_sigupnegative3.png")
        print("Screenshot saved.")
        time.sleep(5)

        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[2]/section/form/div[1]/p")
        result = error_msg1[0].text
        if result == "Email Id is very short.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Email is too short test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Email is too short test failed *************")

        error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[2]/section/form/div[2]/p")
        result = error_msg2[0].text
        if result == "Password is too short.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Password is too short test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** password is too short test failed *************")
        time.sleep(3)

        self.CR.typeShortemail1()
        time.sleep(6)
        self.CR.typeShortpassword1()
        time.sleep(5)

        error_msg3 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[2]/section/form/div[1]/p")
        result = error_msg3[0].text
        if result == "Invalid email":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Invalid Email test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Invalid Email test failed *************")

        error_msg4 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[2]/section/form/div[2]/p")
        result = error_msg4[0].text
        if result == "Use 8 or more characters with a mix of letters, numbers, space & symbols":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Password is mixed & 8 more characters test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Password is mixed & 8 more characters test failed *************")


        self.logger.info("************** Successfully Signup negative 3 test Passed *************")
        self.driver.quit()

    # @pytest.mark.sanity
    def test_Signupnegative4Home(self, setup):  # already existing user email using signup
        self.logger.info("*************** SignUp Test *************")
        self.logger.info("************** Signup Company Negative test 4  *************")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l=Login(self.driver)
        self.CR=companyRegistration(self.driver)
        time.sleep(1)
        self.CR.clickRegistration()
        time.sleep(1)
        self.CR.clickCompany()
        time.sleep(1)
        self.CR.clickChoosecategory()
        time.sleep(1)
        self.CR.selectCompanytype(self.type)
        time.sleep(1)
        self.CR.clickNextButton()
        time.sleep(1)
        # self.email=random_generator()+"@gmail.com"
        time.sleep(1)
        self.CR.setNewEmail(self.emailone)
        time.sleep(1)
        self.CR.setNewPassword(self.newpassword)
        time.sleep(1)
        self.CR.setConfirmpwd(self.confirmpwd)
        time.sleep(1)
        self.CR.clickSecnext()
        time.sleep(1)
        self.CR.setCompanyname(self.compname)
        time.sleep(1)
        self.CR.setBrandname(self.brandname)
        time.sleep(1)
        self.CR.setMobilenum(self.mobnum)
        time.sleep(1)
        self.CR.clickAgreejoin()
        #time.sleep(1)

        # time.sleep(1)
        self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_signupnegative4.png")
        time.sleep(1)

        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = error_msg1[0].text
        if result == "User with the same Email or mobile number already exist.":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** Existing Email Negative Test Passed *************")
        else:
           assert False
           self.logger.info("*************** Existing Email Negative Test Failed *************")

        self.logger.info("************** Signup Company Negative test 4  *************")
        self.driver.quit()

    # @pytest.mark.sanity
    def test_Signupnegative5Home(self, setup):  # Signup second page(Firstname,Lastname,Mobile) is required
        self.logger.info("*************** SignUp Test *************")
        self.logger.info("************** Signup Company Negative test 5  *************")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l=Login(self.driver)
        self.CR=companyRegistration(self.driver)
        time.sleep(1)
        self.CR.clickRegistration()
        time.sleep(1)
        self.CR.clickCompany()
        time.sleep(1)
        self.CR.clickChoosecategory()
        time.sleep(1)
        self.CR.selectCompanytype(self.type)
        time.sleep(1)
        self.CR.clickNextButton()
        time.sleep(1)
        self.CR.setNewEmail(self.email)
        time.sleep(1)
        self.CR.setNewPassword(self.newpassword)
        time.sleep(1)
        self.CR.setConfirmpwd(self.confirmpwd)
        time.sleep(1)
        self.CR.clickSecnext()
        time.sleep(1)
        # self.CR.setCompanyname(self.compname)
        # time.sleep(1)
        # self.CR.setBrandname(self.brandname)
        # time.sleep(1)
        # self.CR.setMobilenum(self.mobnum)
        # time.sleep(2)
        self.CR.clickAgreejoin()
        time.sleep(5)


        self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_signunegative5-1.png")

        error_msg1 = self.driver.find_elements(By.XPATH,
                                               "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[3]/section/main/form/div[1]/p")
        result = error_msg1[0].text
        if result == "Company Name is required":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Company Name is required Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Company Name is required Test Failed *************")

        error_msg2 = self.driver.find_elements(By.XPATH,
                                               "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[3]/section/main/form/div[2]/p")
        result = error_msg2[0].text
        if result == "Brand Name is required":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Brand Name is required Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Brand Name is required Test Failed *************")

        error_msg3 = self.driver.find_elements(By.XPATH,
                                               "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[3]/section/main/form/div[3]/p")
        result = error_msg3[0].text
        if result == "Mobile number is required":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Mobile Number is required Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Mobile Number is required Test Failed *************")


        # Invalid Company Name  & Brand name (only space given)

        time.sleep(3)
        self.CR.typeCNnegative2()
        time.sleep(3)
        self.CR.typeBNnegative2()
        self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_signupnegative5-2.png")

        error_msg1 = self.driver.find_elements(By.XPATH,"/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[3]/section/main/form/div[1]/p")
        result = error_msg1[0].text
        if result == "Invalid Company Name.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Company Name is Invalid Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Company Name is Invalid Test Failed *************")


        error_msg2 = self.driver.find_elements(By.XPATH,"/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[3]/section/main/form/div[2]/p")
        result = error_msg2[0].text
        if result == "Invalid Brand Name.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Brand Name is Invalid Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Brand Name is Invalid Test Failed *************")


        # Company name & Brand name should be accept only 100 characters

        time.sleep(3)
        self.CR.typeCNnegative3()
        time.sleep(3)
        self.CR.typeBNnegative3()
        time.sleep(3)
        self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_signupnegative5-3.png")

        error_msg1 = self.driver.find_elements(By.XPATH,
                                               "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[3]/section/main/form/div[1]/p")
        result = error_msg1[0].text
        if result == "Company Name should not exceed 50 letters.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Company name should accept 100 Characters Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Company name should accept 100 Characters Test Failed *************")

        error_msg2 = self.driver.find_elements(By.XPATH,
                                               "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[3]/section/main/form/div[2]/p")
        result = error_msg2[0].text
        if result == "Brand Name should not exceed 50 letters.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Brand name should accept 100 Characters Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Brand name should accept 100 Characters Test Failed *************")

        self.logger.info("************** Signup Company Negative test 5 Passed Successfully *************")
        self.driver.quit()