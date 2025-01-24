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
    # button_logout_xpath="//*[@id='root']/div[2]/section[1]/main/nav/main/div[1]/aside[1]/div/div/div/div[2]/div[2]/ul/li[5]/div/label"
    # button_yes_xpath="//*[@id='yes']"
    # button_logout_xpath="/html/body/div[1]/div[2]/section[1]/main/nav/main/div[1]/aside[1]/div/div/div/div[6]/ul/li[4]/div/div/span"
    button_logout_xpath="//span[text()='Logout']"
    button_logoutYes_xpath="//button[text()='Yes']"

    # file upload apply job and pitch investing
    job_btn_xpath="/html/body/div[1]/section[1]/main/div/div[1]/main/section[1]/main/div[2]/ul/li[1]/a"
    jobapply_btn_xpath="/html/body/div[1]/section[1]/main/div/div[1]/main/section[2]/div/div/main/main[1]/div[4]/div/button[1]"
    onbehalfofjobapply_toggle_xpath="/html/body/div[4]/div[3]/div[2]/label/span[1]/span[1]/input"
    jobupload_proftracker_xpath="/html/body/div[4]/div[3]/div[2]/div[1]/input"
    jobupload_prof_xpath="/html/body/div[4]/div[3]/div[2]/div[2]/input"

    investing_btn_xpath="/html/body/div[1]/section[1]/main/div/div[1]/main/section[1]/main/div[2]/ul/li[4]/a"
    pitchinvest_btn_xpath="/html/body/div[1]/section[1]/main/div/div[1]/main/section[2]/div/div/main/main/div[7]/div/button[1]/span"
    pitchdocupload_xpath="/html/body/div[4]/div[3]/form/div[3]/input"


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
        self.driver.find_element(By.XPATH,self.button_logout_xpath).click()

    def clickLogoutYes(self):
        self.driver.find_element(By.XPATH,self.button_logoutYes_xpath).click()


    # file upload apply job and pitch investing

    def clickJobbtn(self):
        self.driver.find_element(By.XPATH,self.job_btn_xpath).click()

    def clickJobapplybtn(self):
        self.driver.find_element(By.XPATH,self.jobapply_btn_xpath).click()

    def clickonbehalfofjobapply(self):
        self.driver.find_element(By.XPATH,self.onbehalfofjobapply_toggle_xpath).click()

    def uploadjobproftrackerlarge(self):  # large file
        self.driver.find_element(By.XPATH,self.jobupload_proftracker_xpath).send_keys("D://largefile.pdf")

    def uploadjobproftrackerincfile(self): # incorrect file type
        self.driver.find_element(By.XPATH,self.jobupload_proftracker_xpath).send_keys("D://localfile.zip")

    def uploadjobproflarge(self):  # large file
        self.driver.find_element(By.XPATH,self.jobupload_prof_xpath).send_keys("D://largefile.zip")

    def uploadjobprofincfile(self): # incorrect file type
        self.driver.find_element(By.XPATH,self.jobupload_prof_xpath).send_keys("D://largefile.pdf")




    def clickinvestbtn(self):
        self.driver.find_element(By.XPATH,self.investing_btn_xpath).click()

    def clickpitchinvestbtn(self):
        self.driver.find_element(By.XPATH,self.pitchinvest_btn_xpath).click()

    def uploadpitchdoclarge(self):  # large file
        self.driver.find_element(By.XPATH,self.pitchdocupload_xpath).send_keys("D://largefile.pdf")

    def uploadpitchdocincfile(self): # incorrect file type
        self.driver.find_element(By.XPATH,self.pitchdocupload_xpath).send_keys("D://localfile.zip")