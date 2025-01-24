import time
from telnetlib import EC
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from utilities.customLogger import LogGen



class followfollowers:

    logger = LogGen.loggen()


    follow_button_xpath = "/html/body/div[1]/section[1]/nav/main/div[1]/aside[2]/div[2]/img"
    secondfollow_button_xpath="/html/body/div[1]/div[2]/section[1]/main/nav/main/div[1]/aside[2]/div[2]/img"
    firstaccept_xpath="/html/body/div[1]/section[1]/main/div/div[1]/div/section/div[1]/div[2]/div/div[1]/button"
    profilefollow_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[2]/section/div[2]/div[2]/div[2]/button[1]"
    followtext_xpath="//p[text()='Hema Priya']"
    firstfollow_xpath="/html/body/div[1]/section[1]/main/div/div[1]/div/section/div[1]/div[2]/div/button"
    myfollowers_xpath="/html/body/div[1]/section[1]/main/div/div[1]/section/div/div[2]/a/div/div/span/p[1]"
    unfollow_xpath="/html/body/div[1]/section[1]/main/div/div[1]/div/section/div[1]/div[2]/div/div/button"
    unfollowYes_xpath="/html/body/div[4]/div/div/div[2]/section/div/button[1]"
    myfollowersbackarrow_xpath="/html/body/div[1]/section[1]/main/div/div[1]/section/div/div[1]/img"
    myfollowerscount_xpath="/html/body/div[1]/section[1]/main/div/div[1]/section/div/div[2]/a/div/div/span/p[2]"
    followtextbrand_xpath = "//p[text()='Cosmetic Company Cosmetic']"
    firstaccount_xpath="(//p[@class='ffcards__name'])[1]"
    profile_3dots_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[2]/section/div[1]/div/div"
    blockuser_xpath="/html/body/div[3]/div[3]/ul/li[3]/p"
    unblock_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/div/div[2]/main/section/div[2]/div/div/div/div/div[2]/ul/li/div/button"
    unblockYes_xpath="/html/body/div[4]/div/div/div[2]/section/div/button[1]"
    settings_follow_xpath="/html/body/div[1]/div[2]/section[1]/main/nav/main/div[1]/aside[2]/div[2]/img"
    profilenavbardrop_xpath="/html/body/div[1]/div[2]/section[1]/main/nav/main/div[1]/aside[1]/div"
    settingsunblock_xpath="/html/body/div[1]/div[2]/section[1]/main/nav/main/div[1]/aside[1]/div/div/div/div[2]/div[2]/ul/li[1]/div/label"

    def __init__(self, driver):
        self.driver = driver

    def clickfollowfollowers(self):
        self.driver.find_element(By.XPATH, self.follow_button_xpath).click()

    def clicksecondfollowfollowers(self):
        self.driver.find_element(By.XPATH, self.secondfollow_button_xpath).click()

    def selectionfollow(self):
        # List of XPaths or CSS selectors for the elements you want to find
        element_selectors = [
            (By.XPATH,'/html/body/div[1]/section[1]/main/div/div[1]/div/section/div[1]/div[2]/div/button'),  # first follow
            (By.XPATH,'/html/body/div[1]/section[1]/main/div/div[1]/div/section/div[2]/div[2]/div/button'),  # second follow
            (By.XPATH,'/html/body/div[1]/section[1]/main/div/div[1]/div/section/div[1]/div[2]/div/div[1]/button'), # first accept
            (By.XPATH, "//p[text()='Hema Priya']")
        ]
        # Define a wait time
        wait = WebDriverWait(self.driver, 10)

        for by, selector in element_selectors:
            try:
                # Wait for the element to be present
                element = wait.until(EC.presence_of_element_located((by, selector)))
                # Perform actions with the element (e.g., click, extract text, etc.)
                element.click()
                # print(element.text)

            except (NoSuchElementException, TimeoutException):
                # Skip to the next element if not found
                print(f'Element not found: {selector}')
                continue

    def clickprofilefollow(self):
        self.driver.find_element(By.XPATH, self.profilefollow_xpath).click()

    def clickmyfollowers(self):
        self.driver.find_element(By.XPATH, self.myfollowers_xpath).click()

    def clickunfollow(self):
        self.driver.find_element(By.XPATH, self.unfollow_xpath).click()

    def clickunfollowYes(self):
        self.driver.find_element(By.XPATH, self.unfollowYes_xpath).click()

    def clickmyfollowersbackarrow(self):
        self.driver.find_element(By.XPATH, self.myfollowersbackarrow_xpath).click()

    def compare(self,count1,count2):
        if count1 == count2:
            self.logger.info("Followers count has not reduced - Failed")
        else:
            self.logger.info("Followers count has reduced - Passed")

    def clickbrandaccount(self):
        self.driver.find_element(By.XPATH, self.followtextbrand_xpath).click()

    def clickfirstaccount(self):
        self.driver.find_element(By.XPATH, self.firstaccount_xpath).click()

    def clickprofile3dots(self):
        self.driver.find_element(By.XPATH, self.profile_3dots_xpath).click()

    def clickblockuser(self):
        self.driver.find_element(By.XPATH, self.blockuser_xpath).click()

    def clickunblock(self):
        self.driver.find_element(By.XPATH, self.unblock_xpath).click()

    def clickunblockYes(self):
        self.driver.find_element(By.XPATH, self.unblockYes_xpath).click()

    def clicksettingfollow(self):
        self.driver.find_element(By.XPATH, self.settings_follow_xpath).click()

    def clickprofilenavbardrop(self):
        self.driver.find_element(By.XPATH, self.profilenavbardrop_xpath).click()

    def clicksettingsunblock(self):
        self.driver.find_element(By.XPATH, self.settingsunblock_xpath).click()