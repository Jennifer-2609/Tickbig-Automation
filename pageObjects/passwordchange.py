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



class passwordchange:

    logger = LogGen.loggen()

    # security password change xpath
    settings_button_xpath = "/html/body/div[1]/section[1]/nav/main/div[1]/aside[1]/div/div/div/div[7]/ul/div/div/div/span"
    security_button_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/div/div[1]/div/div[6]/a"
    currentpwd_input_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/div/div[2]/main/section/div/div/div/div[2]/form/div[1]/input"
    newpwd_input_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/div/div[2]/main/section/div/div/div/div[2]/form/div[2]/div/input"
    renewpwd_input_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/div/div[2]/main/section/div/div/div/div[2]/form/div[3]/div/input"
    securitysave_button_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/div/div[2]/main/section/div/div/div/div[2]/form/button"
    changepwdYes_button_xpath="/html/body/div[4]/div/div/div[2]/section/div/button[1]"

    # forgot password
    forgotpwd_button_xpath="/html/body/div[1]/div[2]/section/main/div/div/section[2]/section/p[3]/a"
    forgotpwd_emailinput_xpath="/html/body/div[1]/section[2]/section/form/div/input"
    forgotpwd_sendotp_xpath="/html/body/div[1]/section[2]/section/form/button"
    forgotpwd_verifyotp_xpath="/html/body/div[1]/section[2]/section/button"
    forgotpwdd_resendotp_xpath="/html/body/div[1]/section[2]/section/form/div[2]/div[2]/button"
    forgotpwd_newpwd_xpath="/html/body/div[1]/div[2]/div[2]/form/div[1]/input"
    forgotpwd_confirmpwd_xpath = "/html/body/div[1]/div[2]/div[2]/form/div[2]/input"
    forgotpwdbacktologin_button_xpath="/html/body/div[1]/section[2]/section/a/p"
    otpfield_xpath="/html/body/div[1]/section[2]/section/form/div[2]/div[1]/div/input[1]"
    resetpwd_xpath="/html/body/div[1]/div[2]/div[2]/form/button"

    # Subscription
    subscription_button_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/div/div[1]/div/div[3]/a"
    pjtapply_button_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/div/div[2]/main/section/div[2]/div[5]/section/div/div/div[1]/div/div/div[2]/button"
    pjtcreate_button_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/div/div[2]/main/section/div[2]/div[5]/section/div/div/div[2]/div/div/div[2]/button"
    jobcreate_button_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/div/div[2]/main/section/div[2]/div[5]/section/div/div/div[3]/div/div/div[2]/button"
    jobapply_button_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/div/div[2]/main/section/div[2]/div[5]/section/div/div/div[4]/div/div/div[2]/button"
    staffapply_button_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/div/div[2]/main/section/div[2]/div[5]/section/div/div/div[5]/div/div/div[2]/button"
    staffcreate_button_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/div/div[2]/main/section/div[2]/div[5]/section/div/div/div[6]/div/div/div[2]/button"
    addTocart_button_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/div/div[2]/main/section/div[2]/div[1]"
    cartdel_button_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/div/div[2]/main/section/div/div/div[2]/main/div[1]/div[2]/div/img"


    def __init__(self, driver):
        self.driver = driver

    def clicksettings(self):
        self.driver.find_element(By.XPATH, self.settings_button_xpath).click()

    def clicksecurity(self):
        self.driver.find_element(By.XPATH, self.security_button_xpath).click()

    def clicksubscription(self):
        self.driver.find_element(By.XPATH, self.subscription_button_xpath).click()

    def entercurrentpwd(self,currentpwd):
        self.driver.find_element(By.XPATH, self.currentpwd_input_xpath).clear()
        self.driver.find_element(By.XPATH, self.currentpwd_input_xpath).send_keys(currentpwd)

    def enternewpwd(self,newpwd):
        self.driver.find_element(By.XPATH, self.newpwd_input_xpath).clear()
        self.driver.find_element(By.XPATH, self.newpwd_input_xpath).send_keys(newpwd)

    def enterrenewpwd(self,renewpwd):
        self.driver.find_element(By.XPATH, self.renewpwd_input_xpath).clear()
        self.driver.find_element(By.XPATH, self.renewpwd_input_xpath).send_keys(renewpwd)

    def clicksecuritysave(self):
        self.driver.find_element(By.XPATH, self.securitysave_button_xpath).click()

    def clickchangepwdyes(self):
        self.driver.find_element(By.XPATH, self.changepwdYes_button_xpath).click()

    def entercurrentpwdneg1(self):
        self.driver.find_element(By.XPATH, self.currentpwd_input_xpath).clear()
        self.driver.find_element(By.XPATH, self.currentpwd_input_xpath).send_keys("P@ssw0rd 2022")

    def enternewpwdneg1(self):
        self.driver.find_element(By.XPATH, self.newpwd_input_xpath).clear()
        self.driver.find_element(By.XPATH, self.newpwd_input_xpath).send_keys("newpwd")

    def enterrenewpwdneg1(self):
        self.driver.find_element(By.XPATH, self.renewpwd_input_xpath).clear()
        self.driver.find_element(By.XPATH, self.renewpwd_input_xpath).send_keys("renewpwd")


    # forgot password

    def clickforgotpwd(self):
        self.driver.find_element(By.XPATH, self.forgotpwd_button_xpath).click()

    def clickforgotpwdsendOTP(self):
        self.driver.find_element(By.XPATH, self.forgotpwd_sendotp_xpath).click()

    def clickforgotpwdverifyOTP(self):
        self.driver.find_element(By.XPATH, self.forgotpwd_verifyotp_xpath).click()

    def clickforgotpwdresendOTP(self):
        self.driver.find_element(By.XPATH, self.forgotpwdd_resendotp_xpath).click()

    def enterforgotpwdnew(self):
        self.driver.find_element(By.XPATH, self.forgotpwd_newpwd_xpath).clear()
        self.driver.find_element(By.XPATH, self.forgotpwd_newpwd_xpath).send_keys("P@ssw0rd 2023")

    def enterforgotpwdconfirm(self):
        self.driver.find_element(By.XPATH, self.forgotpwd_confirmpwd_xpath).clear()
        self.driver.find_element(By.XPATH, self.forgotpwd_confirmpwd_xpath).send_keys("P@ssw0rd 2023")

    def enterforgotpwdmail(self,forgptpwdmail):
        self.driver.find_element(By.XPATH, self.forgotpwd_emailinput_xpath).clear()
        self.driver.find_element(By.XPATH, self.forgotpwd_emailinput_xpath).send_keys(forgptpwdmail)

    def enterforgotpwdmailneg(self):
        self.driver.find_element(By.XPATH, self.forgotpwd_emailinput_xpath).clear()
        self.driver.find_element(By.XPATH, self.forgotpwd_emailinput_xpath).send_keys("abg@gmail")

    def enterforgotpwdmailneg1(self):
        self.driver.find_element(By.XPATH, self.forgotpwd_emailinput_xpath).clear()
        self.driver.find_element(By.XPATH, self.forgotpwd_emailinput_xpath).send_keys("abg@gmail.com")

    def clickresetpwd(self):
        self.driver.find_element(By.XPATH, self. resetpwd_xpath).click()
    def clickbacktologin(self):
        self.driver.find_element(By.XPATH, self.forgotpwdbacktologin_button_xpath).click()

    def enterOTP(self):
        self.driver.find_element(By.XPATH, self.otpfield_xpath).clear()
        self.driver.find_element(By.XPATH, self.otpfield_xpath).send_keys("")

    # Subscription

    def scrolltillpageend(self):
        Button = self.driver.find_element(By.XPATH, self.staffcreate_button_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Button)

    def clickpjtapply(self):
        self.driver.find_element(By.XPATH, self.pjtapply_button_xpath).click()

    def clickpjtcreate(self):
        self.driver.find_element(By.XPATH, self.pjtcreate_button_xpath).click()

    def clickjobcreate(self):
        self.driver.find_element(By.XPATH, self.jobcreate_button_xpath).click()

    def clickjobapply(self):
        self.driver.find_element(By.XPATH, self.jobapply_button_xpath).click()

    def clickstaffapply(self):
        self.driver.find_element(By.XPATH, self.staffapply_button_xpath).click()

    def clickstaffcreate(self):
        self.driver.find_element(By.XPATH, self.staffcreate_button_xpath).click()

    def scrollup(self):
        self.driver.execute_script("window.scrollTo(0, 0);")  # scroll to the top of the page

    def clickaddtocart(self):
        self.driver.find_element(By.XPATH, self.addTocart_button_xpath).click()

    def clickcartdel(self):
        self.driver.find_element(By.XPATH, self.cartdel_button_xpath).click()