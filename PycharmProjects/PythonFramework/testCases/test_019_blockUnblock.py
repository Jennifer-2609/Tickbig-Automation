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


class Test_019_BlockUnblock:

    BaseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()


    # Block Unblock
    # @pytest.mark.sanity
    def test_blockUnblock(self, setup):

        self.logger.info("********** Test_019 Block Unblock Test  **********")
        self.logger.info("********** Block Unblock Test Started **********")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.ap = applyproject(self.driver)
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
        self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_beforeblock.png")
        time.sleep(2)
        self.ff.clickfirstaccount()
        time.sleep(2)
        self.ff.clickprofile3dots()
        time.sleep(2)
        self.ff.clickblockuser()
        time.sleep(1)

        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = error_msg1[0].text
        if result == "Blocked successfully.":
            self.logger.info("Error Message Is: %s", result)
        else:
            assert False
            self.logger.info("*************** Blocked Failed  *************")

        time.sleep(2)
        self.ff.clickprofilenavbardrop()
        time.sleep(2)
        self.ff.clicksettingsunblock()
        time.sleep(2)
        self.ff.clickunblock()
        time.sleep(2)
        self.ff.clickunblockYes()
        time.sleep(1)

        error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = error_msg2[0].text
        if result == "Unblocked successfully.":
            self.logger.info("Error Message Is: %s", result)
        else:
            assert False
            self.logger.info("***************  Unblocked Failed  *************")

        time.sleep(2)
        self.ff.clicksettingfollow()
        time.sleep(2)
        self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_afterunblock.png")
        time.sleep(2)

        self.logger.info("************** Block Unblock Test Ended Successfully *************")
        self.driver.quit()