from telnetlib import EC

from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class companyRegistration:

    btn_registration_xpath="/html/body/div[1]/div[2]/div/div[2]/a[1]"
    btn_company_xpath="(//*[@id='green'])[2]"
    btn_ChooseCategory_xpath="//*[@id='root']/div[2]/section[1]/main/div/div/section[2]/section[1]/div[3]/div"
    lst_homegrown_xpath="//div[text()='Homegrown Company']"
    lst_registered_xpath="//div[text()='Registered Company']"
    btn_firstNext_xpath="//*[@id='root']/div[2]/section[1]/main/div/div/section[2]/section[1]/div[4]/button"
    txtEmail_xpath="//*[@id='root']/div[2]/section[1]/main/div/div/section[2]/section[2]/section/form/div[1]/input"
    txtPassword_xpath="/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[2]/section/form/div[2]/input"
    txtConfirmpwd_xpath="/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[2]/section/form/div[3]/input"
    btn_secondNext_xpath="/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[2]/section/form/div[5]/button"
    txtCompanyname_xpath="/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[3]/section/main/form/div[1]/input"
    txtBrandname_xpath="/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[3]/section/main/form/div[2]/input"
    txtMobilenum_xpath="/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[3]/section/main/form/div[3]/div/input"
    btn_agreejoin_xpath="/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[3]/section/main/form/div[6]/button"
    # txtOTP_xpath="/html/body/div[1]/section[2]/section/form/div[1]/div[1]/div/input[1]"
    btn_verifyjoin_xpath="/html/body/div[1]/section[2]/section/form/div[2]/button"


    def __init__(self, driver):
        self.driver = driver

    def clickRegistration(self):
        self.driver.find_element(By.XPATH,self.btn_registration_xpath).click()

    def clickCompany(self):
        self.driver.find_element(By.XPATH,self.btn_company_xpath).click()

    def clickChoosecategory(self):
        self.driver.find_element(By.XPATH,self.btn_ChooseCategory_xpath).click()


    def selectCompanytype(self,type):
        if type=="Homegrown":
            self.driver.find_element(By.XPATH,self.lst_homegrown_xpath).click()
        elif type=="Registered":
            self.driver.find_element(By.XPATH,self.lst_registered_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.lst_registered_xpath).click()

    def clickNextButton(self):
        self.driver.find_element(By.XPATH,self.btn_firstNext_xpath).click()

    def setNewEmail(self,email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setNewEmailone(self,emailone):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(emailone)

    def setNewPassword(self,newpassword):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(newpassword)

    def setConfirmpwd(self,confirmpwd):
        self.driver.find_element(By.XPATH, self.txtConfirmpwd_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtConfirmpwd_xpath).send_keys(confirmpwd)

    def typeLenemail(self,lengthemail):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(lengthemail)

    def typeLenpassword(self,lengthpassword):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(lengthpassword)

    def typeShortemail(self):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys("ghh")

    def typeShortpassword(self):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys("njj")

    def typeShortemail1(self):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys("jbn@gmail")

    def typeShortpassword1(self):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys("gbbjjjyb")


    def clickSecnext(self):
        self.driver.find_element(By.XPATH,self.btn_secondNext_xpath).click()

    def setCompanyname(self,compname):
        self.driver.find_element(By.XPATH, self.txtCompanyname_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtCompanyname_xpath).send_keys(compname)

    def setBrandname(self,brandname):
        self.driver.find_element(By.XPATH, self.txtBrandname_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtBrandname_xpath).send_keys(brandname)

    def typeCNnegative2(self):
        self.driver.find_element(By.XPATH, self.txtCompanyname_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtCompanyname_xpath).send_keys("           ")

    def typeBNnegative2(self):
        self.driver.find_element(By.XPATH, self.txtBrandname_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtBrandname_xpath).send_keys("            ")

    def typeCNnegative3(self):
        self.driver.find_element(By.XPATH, self.txtCompanyname_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtCompanyname_xpath).send_keys("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

    def typeBNnegative3(self):
        self.driver.find_element(By.XPATH, self.txtBrandname_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtBrandname_xpath).send_keys("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    def setMobilenum(self,mobnum):
        self.driver.find_element(By.XPATH, self.txtMobilenum_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtMobilenum_xpath).send_keys(mobnum)

    def clickAgreejoin(self):
        # try:
        #     element = WebDriverWait(self.driver, 10).until(
        #         EC.presence_of_element_located((By.XPATH, self.btn_agreejoin_xpath))
        #     )
        #     # Once the element is clickable, perform actions on it
        #     element.click()
        # except TimeoutException:
        #     print("Element not found within the specified time.")

        self.driver.find_element(By.XPATH,self.btn_agreejoin_xpath).click()

    def typeOTP(self):
        self.driver.find_element(By.XPATH,self.txtOTP_xpath).send_keys("")

    def clickVerifyjoin(self):
        self.driver.find_element(By.XPATH,self.btn_verifyjoin_xpath).click()




