import configparser
import pytest
import time
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import Login
from pageObjects.passwordchange import passwordchange
from pageObjects.applyproject import applyproject
from pageObjects.postprojects import projects
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


config=configparser.ConfigParser()
config.read('C:\\Users\\jenni\\PycharmProjects\\PythonFramework\\Configurations\\config.ini')


class Test_018_Subscription:

    BaseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()


    logger = LogGen.loggen()


    # Subscription
    # @pytest.mark.sanity
    def test_subscription1(self, setup):

        self.logger.info("********** Test_018 Subscription - Test  **********")
        self.logger.info("********** Subscription - Test Started **********")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.ap = applyproject(self.driver)
        self.pc = passwordchange(self.driver)
        self.pjt = projects(self.driver)
        self.l.clicksignin()
        time.sleep(1)
        self.l.setUserName(self.username)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        # time.sleep(1)
        time.sleep(3)
        self.pjt.selectionelement()
        time.sleep(3)
        self.ap.clickprofilenavbardroparrow()
        time.sleep(2)
        self.pc.clicksettings()
        time.sleep(2)
        self.pc.clicksubscription()
        time.sleep(2)
        self.pc.scrolltillpageend()
        time.sleep(2)
        self.pc.clickpjtapply()
        time.sleep(1)

        error_msg1 = self.driver.find_elements(By.XPATH,"/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = error_msg1[0].text
        if result == "Product added To cart":
            self.logger.info("Error Message Is: %s", result)
            self.logger.info("***************  Project Apply added to cart  *************")
        else:
            assert False
            self.logger.info("***************  Project Apply added to cart Failed   *************")

        time.sleep(2)
        self.pc.clickpjtcreate()
        time.sleep(1)

        error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = error_msg2[0].text
        if result == "Product added To cart":
            self.logger.info("Error Message Is: %s", result)
            self.logger.info("***************  Project Create added to cart  *************")
        else:
            assert False
            self.logger.info("***************  Project Create added to cart Failed   *************")

        time.sleep(2)
        self.pc.clickjobcreate()
        time.sleep(1)

        error_msg3 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = error_msg3[0].text
        if result == "Product added To cart":
            self.logger.info("Error Message Is: %s", result)
            self.logger.info("***************  Job Create added to cart  *************")
        else:
            assert False
            self.logger.info("***************  Job Create added to cart Failed   *************")

        time.sleep(2)
        self.pc.clickjobapply()
        time.sleep(1)

        error_msg4 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = error_msg4[0].text
        if result == "Product added To cart":
            self.logger.info("Error Message Is: %s", result)
            self.logger.info("***************  Job Apply added to cart  *************")
        else:
            assert False
            self.logger.info("***************  Job Apply added to cart Failed   *************")

        time.sleep(2)
        self.pc.clickstaffapply()
        time.sleep(1)

        error_msg5 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = error_msg5[0].text
        if result == "Product added To cart":
            self.logger.info("Error Message Is: %s", result)
            self.logger.info("***************  Staff Apply added to cart  *************")
        else:
            assert False
            self.logger.info("***************  Staff Apply added to cart Failed   *************")


        time.sleep(2)
        self.pc.clickstaffcreate()
        time.sleep(1)

        error_msg6 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = error_msg6[0].text
        if result == "Product added To cart":
            self.logger.info("Error Message Is: %s", result)
            self.logger.info("***************  Staff Create added to cart  *************")
        else:
            assert False
            self.logger.info("***************  Staff Create added to cart Failed   *************")

        time.sleep(2)
        # self.pc.scrollup()
        # time.sleep(3)
        # self.pc.clickaddtocart()
        # time.sleep(2)
        # self.pc.clickcartdel()
        #
        # error_msg7 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        # result = error_msg7[0].text
        # if result == "Product removed Succesfully":
        #     self.logger.info("Error Message Is: %s", result)
        # else:
        #     assert False
        #     self.logger.info("***************  Product removed Failed   *************")
        #
        # time.sleep(2)
        # self.pc.clickcartdel()
        # time.sleep(2)
        # self.pc.clickcartdel()
        # time.sleep(2)
        # self.pc.clickcartdel()
        # time.sleep(2)
        # self.pc.clickcartdel()
        # time.sleep(2)
        #
        # error_msg8 = self.driver.find_elements(By.XPATH, "(//div[@class='cart__amt'])[3]")
        # result = error_msg8[0].text
        # if result == "211.22":
        #     self.logger.info("***************  Total is correct - Passed   *************")
        # else:
        #     assert False
        #     self.logger.info("***************  Total is incorrect - Failed  *************")


        self.logger.info("************** Subscription - Test Ended Successfully *************")
        self.driver.quit()


    # @pytest.mark.sanity
    def test_subscription2(self, setup):

        self.logger.info("********** Test_018 Subscription - Test  **********")
        self.logger.info("********** Subscription Item Delete - Test Started **********")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.ap = applyproject(self.driver)
        self.pc = passwordchange(self.driver)
        self.pjt = projects(self.driver)
        self.l.clicksignin()
        time.sleep(1)
        self.l.setUserName(self.username)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        # time.sleep(1)
        time.sleep(3)
        self.pjt.selectionelement()
        time.sleep(3)
        self.ap.clickprofilenavbardroparrow()
        time.sleep(2)
        self.pc.clicksettings()
        time.sleep(2)
        self.pc.clicksubscription()
        time.sleep(2)
        self.pc.clickaddtocart()
        time.sleep(2)
        self.pc.clickcartdel()
        time.sleep(1)

        error_msg7 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = error_msg7[0].text
        if result == "Product removed Succesfully":
            self.logger.info("Error Message Is: %s", result)
        else:
            assert False
            self.logger.info("***************  Product removed Failed   *************")

        time.sleep(4)
        self.pc.clickcartdel()
        time.sleep(4)
        self.pc.clickcartdel()
        time.sleep(4)
        self.pc.clickcartdel()
        time.sleep(4)
        self.pc.clickcartdel()
        time.sleep(4)

        error_msg8 = self.driver.find_elements(By.XPATH, "(//div[@class='cart__amt'])[3]")
        result = error_msg8[0].text
        if result == "211.22":
            self.logger.info("Total Amount Is: %s", result)
            self.logger.info("***************  Total is correct - Passed   *************")
        else:
            assert False
            self.logger.info("***************  Total is incorrect - Failed  *************")

        time.sleep(4)

        self.logger.info("************** Subscription Item Delete - Test Ended Successfully *************")
        self.driver.quit()