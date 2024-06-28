from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    button_signin_xpath="//*[@id='root']/div[2]/div/div[2]/a[2]"
    # text_username_xpath="//*[@id='root']/section[2]/section/form/div[1]/input"
    # text_password_xpath="//*[@id='root']/section[2]/section/form/div[2]/input"
    text_username_xpath = "//*[@id='root']/div[2]/section[1]/main/div/div/section[2]/section/form/div[1]/input"
    text_password_xpath = "//*[@id='root']/div[2]/section[1]/main/div/div/section[2]/section/form/div[2]/input"
    # button_login_xpath="//*[@id='root']/section[2]/section/form/div[4]/button"
    button_login_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section[2]/section/form/div[4]/button"
    button_profile_xpath="//*[@id='root']/div[2]/section[1]/main/nav/main/div[1]/aside[1]/div/span/p"
    button_logout_xpath="//*[@id='root']/div[2]/section[1]/main/nav/main/div[1]/aside[1]/div/div/div/div[2]/div[2]/ul/li[5]/div/label"
    button_yes_xpath="//*[@id='yes']"


    def __init__(self, driver):
        self.driver = driver

    def clicksignin(self):
        self.driver.find_element(By.XPATH, self.button_signin_xpath).click()


    def setUserName(self,  username):
        self.driver.find_element(By.XPATH, self.text_username_xpath).clear()
        self.driver.find_element(By.XPATH,self.text_username_xpath).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.text_password_xpath).clear()
        self.driver.find_element(By.XPATH,self.text_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH,self.button_profile_xpath).click()
        self.driver.find_element(By.XPATH,self.button_logout_xpath).click()
        self.driver.find_element(By.XPATH,self.button_yes_xpath).click()





