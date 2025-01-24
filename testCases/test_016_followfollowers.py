import configparser
import pytest
import time
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import Login
from pageObjects.followfollowers import followfollowers
from pageObjects.passwordchange import passwordchange
from pageObjects.applyproject import applyproject
from pageObjects.postprojects import projects
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


config=configparser.ConfigParser()
config.read('C:\\Users\\jenni\\PycharmProjects\\PythonFramework\\Configurations\\config.ini')


class Test_016_Followfollowers:

    BaseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()


    # Follow Followers
    # @pytest.mark.sanity
    def test_followfollowers(self, setup):

        self.logger.info("********** Test_016 Follow Followers Test  **********")
        self.logger.info("********** Follow Followers Test Started **********")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.ff = followfollowers(self.driver)
        self.pjt = projects(self.driver)
        self.l.clicksignin()
        time.sleep(1)
        self.driver.refresh()
        time.sleep(3)
        self.l.setUserName(self.username)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        # time.sleep(1)
        time.sleep(3)
        self.pjt.selectionelement()
        time.sleep(3)
        self.ff.clickfollowfollowers()
        time.sleep(2)
        self.ff.selectionfollow()
        time.sleep(5)
        self.ff.clickprofilefollow()
        time.sleep(2)

        error_msg1 = self.driver.find_elements(By.XPATH,"/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = error_msg1[0].text
        if result == "Follow request sent.":
            self.logger.info("Error Message Is: %s", result)
        else:
            assert False
            self.logger.info("*************** Follow request sent Failed   *************")

        self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_reqpending.png")


        time.sleep(2)
        self.ff.clicksecondfollowfollowers()
        time.sleep(2)

        count1_element=self.driver.find_element(By.XPATH, "/html/body/div[1]/section[1]/main/div/div[1]/section/div/div[2]/a/div/div/span/p[2]")
        count1 = int(count1_element.text)


        # self.ff.clickmyfollowerscount1()
        # time.sleep(2)
        self.ff.clickmyfollowers()
        time.sleep(2)
        self.ff.clickunfollow()
        time.sleep(2)
        self.ff.clickunfollowYes()
        time.sleep(2)
        self.ff.clickmyfollowersbackarrow()
        time.sleep(2)
        # self.ff.clickmyfollowerscount2()
        # time.sleep(2)

        count2_element = self.driver.find_element(By.XPATH,
                                                  "/html/body/div[1]/section[1]/main/div/div[1]/section/div/div[2]/a/div/div/span/p[2]")
        count2 = int(count2_element.text)

        time.sleep(2)
        self.ff.compare(count1,count2)
        time.sleep(2)
        self.ff.clickbrandaccount()
        time.sleep(2)
        self.ff.clickprofilefollow()
        time.sleep(2)

        error_msg2 = self.driver.find_elements(By.XPATH,"/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = error_msg2[0].text
        if result == "Follow request accepted.":
            self.logger.info("Error Message Is: %s", result)
        else:
            assert False
            self.logger.info("*************** Follow request accepted Failed  *************")

        self.logger.info("************** Follow Followers Test Ended Successfully *************")
        self.driver.quit()