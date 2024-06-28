# from telnetlib import EC
import string
import time
from random import random
from telnetlib import EC

import openpyxl
from selenium.common import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from utilities.customLogger import LogGen




# def generate_random_string(length=10):
#     letters = string.ascii_letters
#     return ''.join(random.choice(letters) for i in range(length))


# def read_excel_data(file_path, sheet_name):
#     workbook = openpyxl.load_workbook(file_path)
#     sheet = workbook[sheet_name]
#     data = []
#
#     for row in sheet.iter_rows(values_only=True):
#         data.append(row)


class profile:

    logger = LogGen.loggen()

    #path to profile page
    profile_icon_xpath="/html/body/div[1]/section[1]/nav/main/div[1]/aside[1]/div/span"
    profile_page_xpath="/html/body/div[1]/section[1]/nav/main/div[1]/aside[1]/div/div/div/div[1]/div[2]/p[2]"

    # Edit quote
    btn_edit_quote="/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[2]/section/div[2]/button/span"
    txtquote_xpath="/html/body/div[3]/div[3]/div/div/main/section/form/div[1]/div/textarea[1]"
    btn_savequote_xpath="/html/body/div[3]/div[3]/div/div/main/section/form/div[2]/button"
    # close_xpath="/html/body/div[3]/div[3]/div/div/main/section/div/div[2]/div"

    # Edit skill
    btn_expertise_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[4]/section/div[2]"
    # btn_addskill_xpath="/html/body/div[3]/div[3]/main/section/div[2]/form/div[3]/button[2]"

    btn_addskill_xpath="/html/body/div[3]/div[3]/main/section/div[2]/form/div/button[2]"

    txt_skill_xpath="/html/body/div[3]/div[3]/main/section/div[2]/form/div[2]/div[1]/input"
    btn_submit_xpath="/html/body/div[3]/div[3]/main/section/div[2]/form/div[3]/button[1]"
    btn_del_xpath="/html/body/div[3]/div[3]/main/section/div[2]/form/div[3]/div[3]/button/span/i"
    btn_subDel_xpath="/html/body/div[3]/div[3]/main/section/div[2]/form/div[11]/button"
    btn_level_xpath="/html/body/div[3]/div[3]/main/section/div[2]/form/div/div[2]/select"
    beginner_xpath="/html/body/div[3]/div[3]/main/section/div[2]/form/div[2]/div[2]/select/option[2]"
    intermediate_xpath="/html/body/div[3]/div[3]/main/section/div[2]/form/div[2]/div[2]/select/option[3]"
    expert_xpath="/html/body/div[3]/div[3]/main/section/div[2]/form/div[2]/div[2]/select/option[4]"
    # (//*[contains( @class,'floating-label')])[1]

    # Edit about
    btn_aboutme_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[3]/main/div[1]/div/img"
    tog_OTW_xpath="/html/body/div[3]/div[3]/main/section/div[2]/form[2]/div[2]/div[1]/div/label/span/span[1]/input"
    tog_RF_xpath="/html/body/div[3]/div[3]/main/section/div[2]/form[2]/div[2]/div[3]/div/label/span/span[1]/input"
    tog_OTI_xpath="/html/body/div[3]/div[3]/main/section/div[2]/form[2]/div[2]/div[5]/div/label/span/span[1]/input"
    tog_OTC_xpath="/html/body/div[3]/div[3]/main/section/div[2]/form[2]/div[2]/div[2]/div/label/span/span[1]/input"
    tog_hiring_xpath="/html/body/div[3]/div[3]/main/section/div[2]/form[2]/div[2]/div[4]/div/label/span/span[1]/input"
    txt_description_xpath="/html/body/div[3]/div[3]/main/section/div[2]/form[2]/div[3]/div/div/textarea[1]"
    btn_save_xpath="/html/body/div[3]/div[3]/main/section/div[2]/form[2]/span/button"
    btn_updateRes_xpath="/html/body/div[3]/div[3]/main/section/div[2]/form[1]/div[2]/div[1]/div/label/input"
    btn_resSave_xpath="/html/body/div[3]/div[3]/main/section/div[2]/form[1]/div[2]/div[1]/div/button[1]"

    # business card
    btn_editcard_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[2]/section/div[3]/div[1]/button[2]"
    txt_firstname_xpath="/html/body/div[3]/div[3]/div/div/form/div[1]/div/input"
    txt_lastname_xpath="/html/body/div[3]/div[3]/div/div/form/div[2]/div/input"
    txt_designation_xpath="/html/body/div[3]/div[3]/div/div/form/div[3]/div/input"
    # select_compname_xpath=""
    # txt_dob_xpath=""
    txt_tagline_xpath="/html/body/div[3]/div[3]/div/div/form/div[6]/div/input"
    txt_summary_xpath="/html/body/div[3]/div[3]/div/div/form/div[7]/div/textarea[1]"
    txt_addline1_xpath="/html/body/div[3]/div[3]/div/div/form/div[9]/div/textarea[1]"
    txt_addline2_xpath="/html/body/div[3]/div[3]/div/div/form/div[10]/div/textarea[1]"
    txt_city_xpath="/html/body/div[3]/div[3]/div/div/form/div[11]/div[1]/div/div/input"
    txt_state_xpath="/html/body/div[3]/div[3]/div/div/form/div[11]/div[2]/div/div/input"
    txt_country_xpath="/html/body/div[3]/div[3]/div/div/form/div[11]/div[3]/div/div/input"
    txt_pincode_xpath="/html/body/div[3]/div[3]/div/div/form/div[11]/div[4]/div/div/input"
    txt_mobile_xpath="/html/body/div[3]/div[3]/div/div/form/div[12]/div/input"
    btn_savebusinesscard_xpath="/html/body/div[3]/div[3]/div/div/form/button"



    def __init__(self, driver):
        self.driver = driver

    def clickProfileicon(self):
        self.driver.find_element(By.XPATH,self.profile_icon_xpath).click()
    def clickProfilepage(self):
        self.driver.find_element(By.XPATH,self.profile_page_xpath).click()

    def clickEditquote(self):
        self.driver.find_element(By.XPATH,self.btn_edit_quote).click()
    def clickEditquoteshort(self,shortquote):
        self.driver.find_element(By.XPATH,self.btn_edit_quote).send_keys(shortquote)

    def clickEditquotelong(self,longquote):
        self.driver.find_element(By.XPATH,self.btn_edit_quote).send_keys(longquote)
    def setQuote(self,quote):
        self.driver.find_element(By.XPATH,self.txtquote_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtquote_xpath).send_keys(quote)
    def typeQuote(self):
        self.driver.find_element(By.XPATH,self.txtquote_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtquote_xpath).send_keys("")
    def clickSavequote(self):
        self.driver.find_element(By.XPATH,self.btn_savequote_xpath).click()

    def clickClose(self):
         self.driver.find_element(By.XPATH, self.close_xpath).click()

    def scrollAbout(self):
        Button=self.driver.find_element(By.XPATH,self.btn_aboutme_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();",Button)

    def scrollExpertise(self):
        Button=self.driver.find_element(By.XPATH,self.btn_expertise_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();",Button)

    def clickExpertise(self):
        self.driver.find_element(By.XPATH, self.btn_expertise_xpath).click()

    #     try:
    #         element = WebDriverWait(self.driver, 10).until(
    #             EC.element_to_be_clickable(locator)
    #         )
    #         element.click()
    #     except ElementClickInterceptedException:
    #         self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    #         element.click()
    #
    # locator=(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[4]/section/div[2]")


# *************************************************************************************************************************************
#
#     def clickaddskill(self):
#     #
#         # for i in range(2,11):
#         #     btn_addskill_xpath="/html/body/div[3]/div[3]/main/section/div[2]/form/div["+str(i)+"]/button[2]"
#         #     time.sleep(2)
#         #     self.driver.find_element(By.XPATH, self.btn_addskill_xpath).click()
#         #     # self.driver.back()
#
#
#         # Wait for an element to be clickable
#         # try:
#         #     element = WebDriverWait(self.driver, 10).until(
#         #         EC.element_to_be_clickable((By.XPATH, self.btn_addskill_xpath))
#         #     )
#         #     # Once the element is clickable, perform actions on it
#         #     element.click()
#         #     # element.send_keys(EndYearEdu)
#         # except TimeoutException:
#         #     print("Element not found within the specified time.")
#
#         # element=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.btn_addskill_xpath)))
#         # element.click()
#         self.driver.find_element(By.XPATH, self.btn_addskill_xpath).click()
#     #
#     def typeskill(self,skill):
#         self.driver.find_element(By.XPATH, self.txt_skill_xpath).send_keys(skill)
#
#         # for i in range(3,10):
#         #     xpath_contains="(//*[contains( @class,'floating-label')])["+str(i)+"]"
#         #     self.driver.find_element(By.XPATH,self.xpath_contains)
#     #
#     def clickLevel(self,level):
#         self.driver.find_element(By.XPATH,self.btn_level_xpath).click()
#         # drp=Select(element)
#         # drp.select_by_visible_text("Beginner")
#         # This Select will work when it has <select> not in <div> tag
#         # dropdown_element = self.driver.find_element(By.XPATH, self.btn_level_xpath)
#         # dropdown = Select(dropdown_element)
#         # # Method 1: Select option by visible text
#         # dropdown.select_by_visible_text("Beginner")
#
#         # Method 2: Select option by value
#         # dropdown.select_by_value("value_1")
#
#         # Method 3: Select option by index (0-based)
#         # dropdown.select_by_index(0)
#         # # self.driver.find_element(By.XPATH, self.txt_emptypeExp_xpath).send_keys(types)
#         if level == "Beginner":
#             self.driver.find_element(By.XPATH, self.beginner_xpath).click()
#         elif level == "Intermediate":
#             self.driver.find_element(By.XPATH, self.intermediate_xpath).click()
#         else:
#             self.driver.find_element(By.XPATH, self.expert_xpath).click()

 # *************************************************************************************************************************************

    def addallskills(self,skills):
        element_selectors1 = [
            (By.XPATH, '/html/body/div[3]/div[3]/main/section/div[2]/form/div[2]/button[2]'),# first add skill button
            (By.XPATH, '/html/body/div[3]/div[3]/main/section/div[2]/form/div[3]/button[2]'),# second add skill button and so on
            (By.XPATH, '/html/body/div[3]/div[3]/main/section/div[2]/form/div[4]/button[2]'),
            (By.XPATH, '/html/body/div[3]/div[3]/main/section/div[2]/form/div[5]/button[2]'),
            (By.XPATH, '/html/body/div[3]/div[3]/main/section/div[2]/form/div[6]/button[2]'),
            (By.XPATH, '/html/body/div[3]/div[3]/main/section/div[2]/form/div[7]/button[2]'),
            (By.XPATH, '/html/body/div[3]/div[3]/main/section/div[2]/form/div[8]/button[2]'),
            (By.XPATH, '/html/body/div[3]/div[3]/main/section/div[2]/form/div[9]/button[2]'),
            (By.XPATH, '/html/body/div[3]/div[3]/main/section/div[2]/form/div[10]/button[2]') # last add skill button
        ]

        # Define a wait time
        wait = WebDriverWait(self.driver, 5)

        for by, selector1 in element_selectors1:
            try:
                # Wait for the element to be present and click it
                element1 = wait.until(EC.presence_of_element_located((by, selector1)))
                element1.click()
            except (NoSuchElementException, TimeoutException) as e:
                # Handle the exception (e.g., log it, skip to the next element)
                print(f'Element not found: {selector1} - {e}')
                continue

        element_selectors2 = [
            (By.XPATH, '/html/body/div[3]/div[3]/main/section/div[2]/form/div[2]/div[1]/input'),  # second input field
            (By.XPATH, '/html/body/div[3]/div[3]/main/section/div[2]/form/div[3]/div[1]/input'),
            (By.XPATH, '/html/body/div[3]/div[3]/main/section/div[2]/form/div[4]/div[1]/input'),
            (By.XPATH, '/html/body/div[3]/div[3]/main/section/div[2]/form/div[5]/div[1]/input'),
            (By.XPATH, '/html/body/div[3]/div[3]/main/section/div[2]/form/div[6]/div[1]/input'),
            (By.XPATH, '/html/body/div[3]/div[3]/main/section/div[2]/form/div[7]/div[1]/input'),
            (By.XPATH, '/html/body/div[3]/div[3]/main/section/div[2]/form/div[8]/div[1]/input'),
            (By.XPATH, '/html/body/div[3]/div[3]/main/section/div[2]/form/div[9]/div[1]/input'),
            (By.XPATH, '/html/body/div[3]/div[3]/main/section/div[2]/form/div[10]/div[1]/input')  # last input field
        ]

        for index, (by, selector2) in enumerate(element_selectors2):
            try:
                # Wait for the element to be present and click it
                element2 = wait.until(EC.presence_of_element_located((by, selector2)))
                # random_value = generate_random_string()
                value = skills[index]
                element2.send_keys(value)

            except (NoSuchElementException, TimeoutException) as e:
                # Handle the exception (e.g., log it, skip to the next element)
                print(f'Element not found: {selector2} - {e}')
                continue

        element_selectors3 = [
            (By.XPATH, '/html/body/div[3]/div[3]/main/section/div[2]/form/div[2]/div[2]/select'),  # second dropdown
            (By.XPATH, '/html/body/div[3]/div[3]/main/section/div[2]/form/div[3]/div[2]/select'),
            (By.XPATH, '/html/body/div[3]/div[3]/main/section/div[2]/form/div[4]/div[2]/select'),
            (By.XPATH, '/html/body/div[3]/div[3]/main/section/div[2]/form/div[5]/div[2]/select'),
            (By.XPATH, '/html/body/div[3]/div[3]/main/section/div[2]/form/div[6]/div[2]/select'),
            (By.XPATH, '/html/body/div[3]/div[3]/main/section/div[2]/form/div[7]/div[2]/select'),
            (By.XPATH, '/html/body/div[3]/div[3]/main/section/div[2]/form/div[8]/div[2]/select'),
            (By.XPATH, '/html/body/div[3]/div[3]/main/section/div[2]/form/div[9]/div[2]/select'),
            (By.XPATH, '/html/body/div[3]/div[3]/main/section/div[2]/form/div[10]/div[2]/select')  # last dropdown
        ]

        for by, selector3 in element_selectors3:
            try:
                # Wait for the dropdown element and select an item
                dropdown = wait.until(EC.presence_of_element_located((by, selector3)))
                select = Select(dropdown)
                select.select_by_visible_text('Beginner')

            except (NoSuchElementException, TimeoutException) as e:
                # Handle the exception (e.g., log it, skip to the next element)
                print(f'Element not found: {selector3} - {e}')
                continue


        # Finally, click the submit button
        try:
            submit_button = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[3]/main/section/div[2]/form/div[11]/button')))
            submit_button.click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f'Submit button not found: {e}')

    def clickDelskill(self):
        # self.driver.find_element(By.XPATH, self.btn_del_xpath).click()
        element_selectors1 = [
            (By.XPATH, '/html/body/div[3]/div[3]/main/section/div[2]/form/div[10]/div[3]/button'),  # second del button
            (By.XPATH, '/html/body/div[3]/div[3]/main/section/div[2]/form/div[9]/div[3]/button'),
            (By.XPATH, '/html/body/div[3]/div[3]/main/section/div[2]/form/div[8]/div[3]/button'),
            (By.XPATH, '/html/body/div[3]/div[3]/main/section/div[2]/form/div[7]/div[3]/button'),
            (By.XPATH, '/html/body/div[3]/div[3]/main/section/div[2]/form/div[6]/div[3]/button'),
            (By.XPATH, '/html/body/div[3]/div[3]/main/section/div[2]/form/div[5]/div[3]/button'),
            (By.XPATH, '/html/body/div[3]/div[3]/main/section/div[2]/form/div[4]/div[3]/button'),
            (By.XPATH, '/html/body/div[3]/div[3]/main/section/div[2]/form/div[3]/div[3]/button'),
            (By.XPATH, '/html/body/div[3]/div[3]/main/section/div[2]/form/div[2]/div[3]/button')  # last del button
        ]

        # Define a wait time
        wait = WebDriverWait(self.driver, 10)

        for by, selector1 in element_selectors1:
            try:
                # Wait for the element to be present and click it
                element1 = wait.until(EC.presence_of_element_located((by, selector1)))
                element1.click()

            except (NoSuchElementException, TimeoutException) as e:
                # Handle the exception (e.g., log it, skip to the next element)
                print(f'Element not found: {selector1} - {e}')
                continue

            # Finally, click the submit button
        try:
            submit_button = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[3]/main/section/div[2]/form/div[2]/button[1]')))
            submit_button.click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f'Submit button not found: {e}')



    # def clickSubmitDelskill(self):
    #     self.driver.find_element(By.XPATH, self.btn_subDel_xpath).click()

    def clickSubmit(self):
        element=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.btn_submit_xpath)))
        element.click()

    def clickEditAbout(self):
        self.driver.find_element(By.XPATH, self.btn_aboutme_xpath).click()

    def clickOpenWork(self):
        self.driver.find_element(By.XPATH, self.tog_OTW_xpath).click()

    def clickRaisingFund(self):
        self.driver.find_element(By.XPATH, self.tog_RF_xpath).click()

    def clickOpenInvest(self):
        self.driver.find_element(By.XPATH, self.tog_OTI_xpath).click()

    def clickOpenConsult(self):
        self.driver.find_element(By.XPATH, self.tog_OTC_xpath).click()

    def clickHiring(self):
        self.driver.find_element(By.XPATH, self.tog_hiring_xpath).click()

    def clickDescription(self):
        self.driver.find_element(By.XPATH, self.txt_description_xpath).send_keys("")

    def clickDescriptionclear(self):
        self.driver.find_element(By.XPATH, self.txt_description_xpath).clear()

    def uploadResume(self):
        self.driver.find_element(By.XPATH, self.btn_updateRes_xpath).send_keys("D://Python/S3details.pdf")

    def clickRessave(self):
        self.driver.find_element(By.XPATH, self.btn_resSave_xpath).click()

    def clickSave(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()

    def scrollSave(self):
        Button=self.driver.find_element(By.XPATH,self.btn_save_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();",Button)

    def clickeditcard(self):
        self.driver.find_element(By.XPATH, self.btn_editcard_xpath).click()

    def clickFN(self):
        field = self.driver.find_element(By.XPATH, self.txt_firstname_xpath) # Find the field element you want to check
        field.click() # Simulate clicking on the field to put focus on it
        active_element = self.driver.switch_to.active_element # Get the currently focused element
        # Check if the currently focused element is the field you're interested in
        if active_element==field:
            self.logger.info("********** First Name field is Editable *********")
        else:
            self.logger.info("********** First Name field is not Editable *********")

    def clickLN(self):
        field = self.driver.find_element(By.XPATH, self.txt_lastname_xpath)  # Find the field element you want to check
        field.click()  # Simulate clicking on the field to put focus on it
        active_element = self.driver.switch_to.active_element  # Get the currently focused element
        # Check if the currently focused element is the field you're interested in
        if active_element == field:
            self.logger.info("********** First Name field is Editable *********")
        else:
            self.logger.info("********** First Name field is not Editable *********")

    def setDesignation(self,designation):
        self.driver.find_element(By.XPATH, self.txt_designation_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_designation_xpath).send_keys(designation)

    def settagline(self,tagline):
        self.driver.find_element(By.XPATH, self.txt_tagline_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_tagline_xpath).send_keys(tagline)

    def setsummary(self,summary):
        self.driver.find_element(By.XPATH, self.txt_summary_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_summary_xpath).send_keys(summary)

    def setaddress1(self,address1):
        self.driver.find_element(By.XPATH, self.txt_addline1_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_addline1_xpath).send_keys(address1)

    def setaddress2(self,address2):
        self.driver.find_element(By.XPATH, self.txt_addline2_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_addline2_xpath).send_keys(address2)

    def setcity(self,city):
        self.driver.find_element(By.XPATH, self.txt_city_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_city_xpath).send_keys(city)

    def setstate(self,state):
        self.driver.find_element(By.XPATH, self.txt_state_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_state_xpath).send_keys(state)

    def setcountry(self,country):
        self.driver.find_element(By.XPATH, self.txt_country_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_country_xpath).send_keys(country)

    def setpincode(self,pincode):
        self.driver.find_element(By.XPATH, self.txt_pincode_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_pincode_xpath).send_keys(pincode)

    def clickmob(self):
        field = self.driver.find_element(By.XPATH, self.txt_mobile_xpath)  # Find the field element you want to check
        field.click()  # Simulate clicking on the field to put focus on it
        active_element = self.driver.switch_to.active_element  # Get the currently focused element
        # Check if the currently focused element is the field you're interested in
        if active_element == field:
            self.logger.info("********** First Name field is Editable *********")
        else:
            self.logger.info("********** First Name field is not Editable *********")

    def clearDesignation(self):
        self.driver.find_element(By.XPATH, self.txt_designation_xpath).clear()

    def cleartagline(self):
        self.driver.find_element(By.XPATH, self.txt_tagline_xpath).clear()

    def clearsummary(self):
        self.driver.find_element(By.XPATH, self.txt_summary_xpath).clear()

    def clearaddress1(self):
        self.driver.find_element(By.XPATH, self.txt_addline1_xpath).clear()

    def clearaddress2(self):
        self.driver.find_element(By.XPATH, self.txt_addline2_xpath).clear()

    def clearcity(self):
        self.driver.find_element(By.XPATH, self.txt_city_xpath).clear()

    def clearstate(self):
        self.driver.find_element(By.XPATH, self.txt_state_xpath).clear()

    def clearcountry(self):
        self.driver.find_element(By.XPATH, self.txt_country_xpath).clear()

    def clearpincode(self):
        self.driver.find_element(By.XPATH, self.txt_pincode_xpath).clear()

    def clicksaveBC(self):
        self.driver.find_element(By.XPATH, self.btn_savebusinesscard_xpath).click()

