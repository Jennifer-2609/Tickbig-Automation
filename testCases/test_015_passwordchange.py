import configparser
import pytest
import time
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import Login
from pageObjects.passwordchange import passwordchange
from pageObjects.applyproject import applyproject
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


config=configparser.ConfigParser()
config.read('C:\\Users\\jenni\\PycharmProjects\\PythonFramework\\Configurations\\config.ini')


class Test_015_Passwordchange:

    BaseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    currentpwd = ReadConfig.getcurrentpwd()
    newpwd = ReadConfig.getnewpwd()
    renewpwd = ReadConfig.getrenewpwd()
    forgptpwdmail = ReadConfig.getforgptpwdmail()


    logger = LogGen.loggen()


    # # Security - Negative Testcase
    # @pytest.mark.sanity
    # def test_securitynegative(self, setup):
    #
    #     self.logger.info("********** Test_015 Password change - Negative Test  **********")
    #     self.logger.info("********** Password change - Negative Test  Started **********")
    #     self.driver = setup
    #     self.driver.get(self.BaseURL)
    #     self.driver.maximize_window()
    #     self.l = Login(self.driver)
    #     self.ap = applyproject(self.driver)
    #     self.pc = passwordchange(self.driver)
    #     # self.l.clicksignin()
    #     # time.sleep(1)
    #     self.l.setUserName(self.username)
    #     time.sleep(1)
    #     self.l.setPassword(self.password)
    #     time.sleep(1)
    #     self.l.clickLogin()
    #     time.sleep(1)
    #     self.ap.clickprofilenavbardroparrow()
    #     time.sleep(2)
    #     self.pc.clicksettings()
    #     time.sleep(2)
    #     self.pc.clicksecurity()
    #     time.sleep(2)
    #     self.pc.clicksecuritysave()
    #     time.sleep(2)
    #
    #
    #     error_msg1 = self.driver.find_elements(By.XPATH,"/html/body/div[1]/div[2]/section[1]/main/div/div/div/div[2]/main/section/div/div/div/div[2]/form/div[1]/p")
    #     result = error_msg1[0].text
    #     if result == "Current Password is required":
    #         self.logger.info("Error Message Is: %s", result)
    #     else:
    #         assert False
    #         self.logger.info("***************  Current Password is required Failed   *************")
    #
    #
    #     error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/div/div[2]/main/section/div/div/div/div[2]/form/div[2]/div/p")
    #     result = error_msg2[0].text
    #     if result == "New Password is required":
    #         self.logger.info("Error Message Is: %s", result)
    #     else:
    #         assert False
    #         self.logger.info("***************  New Password is required Failed   *************")
    #
    #
    #     error_msg3 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/div/div[2]/main/section/div/div/div/div[2]/form/div[3]/div/p")
    #     result = error_msg3[0].text
    #     if result == "Confirm Password is required":
    #         self.logger.info("Error Message Is: %s", result)
    #     else:
    #         assert False
    #         self.logger.info("***************  Confirm Password is required Failed  *************")
    #
    #     # time.sleep(2)
    #     # self.pc.entercurrentpwdneg1()
    #     # time.sleep(1)
    #     # self.pc.enternewpwd(self.newpwd)
    #     # time.sleep(1)
    #     # self.pc.enterrenewpwd(self.renewpwd)
    #     # time.sleep(1)
    #     # self.pc.clicksecuritysave()
    #     # time.sleep(1)
    #     #
    #     # error_msg4 = self.driver.find_elements(By.XPATH,"")
    #     # result = error_msg4[0].text
    #     # if result == "":
    #     #     self.logger.info("Error Message Is: %s", result)
    #     # else:
    #     #     assert False
    #     #     self.logger.info("***************   Failed  *************")
    #
    #     time.sleep(2)
    #     self.pc.enternewpwdneg1()
    #     time.sleep(1)
    #     self.pc.enterrenewpwdneg1()
    #     time.sleep(1)
    #
    #     error_msg5 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/div/div[2]/main/section/div/div/div/div[2]/form/div[2]/div/p")
    #     result = error_msg5[0].text
    #     if result == "Use 8 or more characters with a mix of letters, numbers, space & symbols.":
    #         self.logger.info("Error Message Is: %s", result)
    #     else:
    #         assert False
    #         self.logger.info("*************** Use 8 or more characters Failed  *************")
    #
    #
    #     error_msg6 = self.driver.find_elements(By.XPATH,"/html/body/div[1]/div[2]/section[1]/main/div/div/div/div[2]/main/section/div/div/div/div[2]/form/div[3]/div/p")
    #     result = error_msg6[0].text
    #     if result == "New and confirm passwords doesnot match.":
    #         self.logger.info("Error Message Is: %s", result)
    #     else:
    #         assert False
    #         self.logger.info("*************** New and confirm passwords does not match. Failed  *************")
    #
    #     self.logger.info("************** Password change - Negative Test Ended Successfully *************")
    #     self.driver.quit()
    #
    # # Security - Positive Testcase
    # @pytest.mark.sanity
    # def test_securitypositive(self, setup):
    #
    #     self.logger.info("********** Test_015 Password change - Positive Test  **********")
    #     self.logger.info("********** Password change - Positive Test  Started **********")
    #     self.driver = setup
    #     self.driver.get(self.BaseURL)
    #     self.driver.maximize_window()
    #     self.l = Login(self.driver)
    #     self.ap = applyproject(self.driver)
    #     self.pc = passwordchange(self.driver)
    #     # self.l.clicksignin()
    #     # time.sleep(1)
    #     self.l.setUserName(self.username)
    #     time.sleep(1)
    #     self.l.setPassword(self.password)
    #     time.sleep(1)
    #     self.l.clickLogin()
    #     time.sleep(1)
    #     self.ap.clickprofilenavbardroparrow()
    #     time.sleep(2)
    #     self.pc.clicksettings()
    #     time.sleep(2)
    #     self.pc.clicksecurity()
    #     time.sleep(2)
    #     self.pc.entercurrentpwd(self.currentpwd)
    #     time.sleep(2)
    #     self.pc.enternewpwd(self.newpwd)
    #     time.sleep(2)
    #     self.pc.enterrenewpwd(self.renewpwd)
    #     time.sleep(2)
    #     self.pc.clicksecuritysave()
    #     time.sleep(2)
    #     self.pc.clickchangepwdyes()
    #     time.sleep(3)
    #     act_url = self.driver.current_url
    #
    #     if act_url=="http://localhost:3000/":
    #         assert True
    #         self.logger.info("********** Security test is passed *********")
    #     else:
    #         assert False
    #         self.logger.info("********** Security test is failed *********")
    #
    #
    #     self.logger.info("************** Password change - Positive Test Ended Successfully *************")
    #     self.driver.quit()


    # Forgot Password - Positive and Negative
    @pytest.mark.sanity
    def test_forgotpassword(self, setup):

        self.logger.info("********** Test_015 Forgot Password - Positive and Negative Test  **********")
        self.logger.info("********** Forgot Password Test Started **********")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.ap = applyproject(self.driver)
        self.pc = passwordchange(self.driver)
        self.l.clicksignin()
        time.sleep(1)
        # self.l.setUserName(self.username)
        # time.sleep(1)
        # self.l.setPassword(self.password)
        # time.sleep(1)
        # self.l.clickLogin()
        # time.sleep(1)
        self.pc.clickforgotpwd()
        time.sleep(1)
        self.pc.clickforgotpwdsendOTP()
        time.sleep(1)

        error_msg1 = self.driver.find_elements(By.XPATH,"/html/body/div[1]/section[2]/section/form/div/p")
        result = error_msg1[0].text
        if result == "email is required":
            self.logger.info("Error Message Is: %s", result)
        else:
            assert False
            self.logger.info("***************  email is required Failed   *************")

        time.sleep(1)
        self.pc.enterforgotpwdmailneg()
        time.sleep(1)

        error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/section[2]/section/form/div/p")
        result = error_msg2[0].text
        if result == "Invalid email":
            self.logger.info("Error Message Is: %s", result)
        else:
            assert False
            self.logger.info("***************  Invalid email Failed   *************")

        time.sleep(1)
        self.pc.enterforgotpwdmailneg1()
        time.sleep(1)
        self.pc.clickforgotpwdsendOTP()
        time.sleep(1)

        error_msg3 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = error_msg3[0].text
        if result == "Email doesn't exists":
            self.logger.info("Error Message Is: %s", result)
        else:
            assert False
            self.logger.info("***************  Email doesn't exists Failed   *************")


        time.sleep(2)
        self.pc.clickbacktologin()
        time.sleep(2)
        self.pc.clickforgotpwd()
        time.sleep(3)
        self.pc.enterforgotpwdmail(self.forgptpwdmail)
        time.sleep(3)
        self.pc.clickforgotpwdsendOTP()
        time.sleep(2)

        error_msg4 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = error_msg4[0].text
        if result == "OTP sent to your registered mail id.":
            self.logger.info("Error Message Is: %s", result)
        else:
            assert False
            self.logger.info("***************  OTP sent to your registered mail id Failed   *************")


        time.sleep(2)
        self.pc.enterOTP()
        time.sleep(10)
        self.pc.clickforgotpwdverifyOTP()
        time.sleep(1)

        error_msg5 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = error_msg5[0].text
        if result == "Incorrect otp entered":
            self.logger.info("Error Message Is: %s", result)
        else:
            assert False
            self.logger.info("***************  Incorrect otp entered Failed   *************")

        time.sleep(55)
        self.pc.enterOTP()
        time.sleep(10)
        self.pc.clickforgotpwdverifyOTP()
        time.sleep(1)

        error_msg6 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = error_msg6[0].text
        if result == "OTP expired. Resend OTP Now.":
            self.logger.info("Error Message Is: %s", result)
        else:
            assert False
            self.logger.info("***************  OTP expired. Resend OTP Nowx Failed   *************")


        time.sleep(2)
        self.pc.clickforgotpwdresendOTP()
        time.sleep(2)
        self.pc.enterOTP()
        time.sleep(20)
        self.pc.clickforgotpwdverifyOTP()
        time.sleep(1)

        error_msg7 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = error_msg7[0].text
        if result == "OTP verified":
            self.logger.info("Error Message Is: %s", result)
        else:
            assert False
            self.logger.info("***************  OTP verified Failed   *************")

        time.sleep(2)
        self.pc.enterforgotpwdnew()
        time.sleep(2)
        self.pc.enterforgotpwdconfirm()
        time.sleep(2)
        self.pc.clickresetpwd()
        time.sleep(1)

        error_msg8 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = error_msg8[0].text
        if result == "Password reset successfully":
            self.logger.info("Error Message Is: %s", result)
        else:
            assert False
            self.logger.info("***************  Password reset successfully Failed   *************")


        self.logger.info("************** Forgot Password Test Ended Successfully *************")
        self.driver.quit()