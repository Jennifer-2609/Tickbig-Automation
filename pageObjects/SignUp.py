import time
from telnetlib import EC
from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from utilities.customLogger import LogGen


class signup:

    logger = LogGen.loggen()

    def __init__(self, driver):
        self.driver = driver

    def clickProfileicon(self):
        self.driver.find_element(By.XPATH,self.profile_icon_xpath).click()