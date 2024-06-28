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



class projects:

    # project type xpath
    projects_button_xpath="/html/body/div[1]/section[1]/main/div/div[1]/main/section[1]/main/div[2]/ul/li[2]/a"
    postpjt_button_xpath="/html/body/div[1]/section[1]/main/div/div[1]/main/section[1]/main/div[4]/a/div/p"
    postpjtfinal_button_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[10]/button[2]/span[1]"
    pjtnametype_input_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[2]/div/input"
    sectortype_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[3]/div/div/div[1]/div[1]/div[2]"
    pricingtype1_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[4]/div/div[1]/div/div/div[1]/div[1]/div[2]"
    pricingtype2_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[4]/div/div[2]/div/div/div/div[1]/div[2]"
    minpricetype_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[4]/div/div[3]/div/input[1]"
    maxpricetype_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[4]/div/div[3]/div/input[2]"
    pjtreq_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[5]/div[1]/div/div/div/textarea[1]"
    pjtresponsibility_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[5]/div[2]/div/div/div[2]/div[1]"
    skill1_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[7]/div/input"
    nextskill_button_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[7]/div/img"
    skill2_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[7]/div[2]/input"
    whocanapply_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[8]/div/div/div[1]/div[1]/div[2]"
    artscraft_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[3]/div/div/div[2]/div/div[8]"
    monthly_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[4]/div/div[1]/div/div/div[2]/div/div[1]"
    INR_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[4]/div/div[2]/div/div/div[2]/div/div[1]"

    # staff augmentation xpath
    staffdrop_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[1]/div/div"
    selectstaff_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[1]/div/div[2]/div[2]"
    postpjtfinal_button1_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[13]/button[2]/span[1]"
    minpricestaff_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[7]/div/div[3]/div/input[1]"
    maxpricestaff_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[7]/div/div[3]/div/input[2]"
    pjtnamestaff_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[2]/div/input"
    sectortypestaff_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[3]/div/div/div/div[1]/div[2]"
    contractperiod_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[4]/div/input"
    noofposition_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[5]/div/input"
    employmenttype_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[6]/div/div/div/div[1]/div[2]"
    onsite_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[6]/div/div/div[2]/div/div[1]"
    pricingstaff1_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[7]/div/div[1]/div/div/div[1]/div[1]/div[2]"
    pricingstaff2_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[7]/div/div[2]/div/div/div/div[1]/div[2]"
    monthlystaff_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[7]/div/div[1]/div/div/div[2]/div/div[1]"
    INRstaff_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[7]/div/div[2]/div/div/div[2]/div/div[1]"
    pjtreqstaff_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[8]/div[1]/div/div/div/textarea[1]"
    pjtresponsibilitystaff_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[8]/div[2]/div/div/div[2]/div[1]"
    nextskillstaff_button_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[10]/div/img"
    skillstaff1_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[10]/div/input"
    skillstaff2_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[10]/div[2]/input"
    whocanapplystaff_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[11]/div/div/div[1]/div[1]/div[2]"



    def __init__(self, driver):
        self.driver = driver

    def clickPjtButton(self):
        self.driver.find_element(By.XPATH,self.projects_button_xpath).click()

    def clickPostPjtButton(self):
        self.driver.find_element(By.XPATH,self.postpjt_button_xpath).click()

    def clickstaffdrop(self):
        self.driver.find_element(By.XPATH,self.staffdrop_xpath).click()

    def clickselectstaff(self):
        self.driver.find_element(By.XPATH,self.selectstaff_xpath).click()

    def scrollPostPjt(self):
        Button = self.driver.find_element(By.XPATH, self.postpjtfinal_button_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Button)

    def clickPostPjtFinalButton(self):
        self.driver.find_element(By.XPATH,self.postpjtfinal_button_xpath).click()

    def scrollPostPjt1(self):
        Button = self.driver.find_element(By.XPATH, self.postpjtfinal_button1_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Button)

    def clickPostPjtFinalButton1(self):
        self.driver.find_element(By.XPATH,self.postpjtfinal_button1_xpath).click()

    def setmin1(self):
        self.driver.find_element(By.XPATH, self.minpricetype_xpath).clear()
        self.driver.find_element(By.XPATH, self.minpricetype_xpath).send_keys("80000")
    def setmin2(self):
        self.driver.find_element(By.XPATH, self.minpricetype_xpath).clear()
        self.driver.find_element(By.XPATH, self.minpricetype_xpath).send_keys("50000")
    def setmax1(self):
        self.driver.find_element(By.XPATH, self.maxpricetype_xpath).clear()
        self.driver.find_element(By.XPATH, self.maxpricetype_xpath).send_keys("50000")
    def setmax2(self):
        self.driver.find_element(By.XPATH, self.maxpricetype_xpath).clear()
        self.driver.find_element(By.XPATH, self.maxpricetype_xpath).send_keys("100000")

    def setstaffmin1(self):
        self.driver.find_element(By.XPATH, self.minpricestaff_xpath).clear()
        self.driver.find_element(By.XPATH, self.minpricestaff_xpath).send_keys("80000")
    def setstaffmin2(self):
        self.driver.find_element(By.XPATH, self.minpricestaff_xpath).clear()
        self.driver.find_element(By.XPATH, self.minpricestaff_xpath).send_keys("50000")

    def setstaffmax1(self):
        self.driver.find_element(By.XPATH, self.maxpricestaff_xpath).clear()
        self.driver.find_element(By.XPATH, self.maxpricestaff_xpath).send_keys("50000")
    def setstaffmax2(self):
        self.driver.find_element(By.XPATH, self.maxpricestaff_xpath).clear()
        self.driver.find_element(By.XPATH, self.maxpricestaff_xpath).send_keys("100000")


    def setpjtname1(self):
        self.driver.find_element(By.XPATH, self.pjtnametype_input_xpath).clear()
        self.driver.find_element(By.XPATH, self.pjtnametype_input_xpath).send_keys("Serene Streets")

    def setpjtname2(self):
        self.driver.find_element(By.XPATH, self.pjtnamestaff_xpath).clear()
        self.driver.find_element(By.XPATH, self.pjtnamestaff_xpath).send_keys("Opinion Tracker")

    def setpjtreq1(self):
        self.driver.find_element(By.XPATH, self.pjtreq_xpath).clear()
        self.driver.find_element(By.XPATH, self.pjtreq_xpath).send_keys("It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters")

    def setpjtreq2(self):
        self.driver.find_element(By.XPATH, self.pjtreqstaff_xpath).clear()
        self.driver.find_element(By.XPATH, self.pjtreqstaff_xpath).send_keys("If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text.")

    def setpjtresponsibility1(self):
        self.driver.find_element(By.XPATH, self.pjtresponsibility_xpath).clear()
        self.driver.find_element(By.XPATH, self.pjtresponsibility_xpath).send_keys("There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour")

    def setpjtresponsibility2(self):
        self.driver.find_element(By.XPATH, self.pjtresponsibilitystaff_xpath).clear()
        self.driver.find_element(By.XPATH, self.pjtresponsibilitystaff_xpath).send_keys("Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy")

    def setpjtskill1(self):
        self.driver.find_element(By.XPATH, self.skill1_xpath).clear()
        self.driver.find_element(By.XPATH, self.skill1_xpath).send_keys("communication")

    def clicknextskill1(self):
        self.driver.find_element(By.XPATH,self.nextskill_button_xpath).click()

    def clicknextskill2(self):
        self.driver.find_element(By.XPATH,self.nextskillstaff_button_xpath).click()

    def setpjtskill2(self):
        self.driver.find_element(By.XPATH, self.skill2_xpath).clear()
        self.driver.find_element(By.XPATH, self.skill2_xpath).send_keys("Creative")

    def setstaffskill1(self):
        self.driver.find_element(By.XPATH, self.skillstaff1_xpath).clear()
        self.driver.find_element(By.XPATH, self.skillstaff1_xpath).send_keys("leadership")

    def setstaffskill2(self):
        self.driver.find_element(By.XPATH, self.skillstaff2_xpath).clear()
        self.driver.find_element(By.XPATH, self.skillstaff2_xpath).send_keys("adaptability")


    def setwhocanapply1(self):
        # self.driver.find_element(By.XPATH, self.whocanapply_xpath).clear()
        # self.driver.find_element(By.XPATH, self.whocanapply_xpath).send_keys("")

        dropdown_container = self.driver.find_element(By.XPATH, self.whocanapply_xpath)
        # Click on the dropdown to expand it
        dropdown_container.click()
        # Wait for the options to be visible (adjust the time if needed)
        time.sleep(10)
        # Locate all the dropdown options
        # dropdown_options = dropdown_container.find_elements(By.XPATH, '/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[8]/div/div/div[2]')
        # # Iterate through each option and click to select it
        # for option in dropdown_options:
        #     ActionChains(self.driver).move_to_element(option).click().perform()
        #     print(f"Selected: {option.text}")
        #     time.sleep(0.5)  # Adjust the sleep time if necessary

    def setwhocanapply2(self):

        dropdown_container = self.driver.find_element(By.XPATH, self.whocanapplystaff_xpath)
        dropdown_container.click()
        time.sleep(10)

    def selectsectortype1(self):
        # Locate the dropdown-like element
        dropdown_element = self.driver.find_element(By.XPATH, self.sectortype_xpath)
        # Click on the dropdown-like element to open it
        dropdown_element.click()
        # Locate and click on the specific option within the dropdown-like element
        option_element = self.driver.find_element(By.XPATH, self.artscraft_xpath)
        option_element.click()

    def selectsectortype2(self):
        # Locate the dropdown-like element
        dropdown_element = self.driver.find_element(By.XPATH, self.sectortypestaff_xpath)
        # Click on the dropdown-like element to open it
        dropdown_element.click()
        # Locate and click on the specific option within the dropdown-like element
        option_element = self.driver.find_element(By.XPATH, self.artscraft_xpath)
        option_element.click()

    def selectpricingtype1(self):
        # Locate the dropdown-like element
        dropdown_element = self.driver.find_element(By.XPATH, self.pricingtype1_xpath)
        # Click on the dropdown-like element to open it
        dropdown_element.click()
        # Locate and click on the specific option within the dropdown-like element
        option_element = self.driver.find_element(By.XPATH, self.monthly_xpath)
        option_element.click()

    def selectpricingtype2(self):
        # Locate the dropdown-like element
        dropdown_element = self.driver.find_element(By.XPATH, self.pricingtype2_xpath)
        # Click on the dropdown-like element to open it
        dropdown_element.click()
        # Locate and click on the specific option within the dropdown-like element
        option_element = self.driver.find_element(By.XPATH, self.INR_xpath )
        option_element.click()

    def setcontractperiod(self):
        self.driver.find_element(By.XPATH, self.contractperiod_xpath).clear()
        self.driver.find_element(By.XPATH, self.contractperiod_xpath).send_keys("1")

    def setnoofposition(self):
        self.driver.find_element(By.XPATH, self.noofposition_xpath).clear()
        self.driver.find_element(By.XPATH, self.noofposition_xpath).send_keys("5")

    def setemploymenttype(self):
        dropdown_element = self.driver.find_element(By.XPATH, self.employmenttype_xpath)
        dropdown_element.click()
        option_element = self.driver.find_element(By.XPATH, self.onsite_xpath)
        option_element.click()

    def selectpricingstaff1(self):
        dropdown_element = self.driver.find_element(By.XPATH, self.pricingstaff1_xpath)
        dropdown_element.click()
        option_element = self.driver.find_element(By.XPATH, self.monthlystaff_xpath)
        option_element.click()

    def selectpricingstaff2(self):
        dropdown_element = self.driver.find_element(By.XPATH, self.pricingstaff2_xpath)
        dropdown_element.click()
        option_element = self.driver.find_element(By.XPATH, self.INRstaff_xpath)
        option_element.click()

    def scrollstaffpricing(self):
        Button = self.driver.find_element(By.XPATH, self.pricingstaff1_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Button)

    def selectionelement(self):
        # List of XPaths or CSS selectors for the elements you want to find
        element_selectors = [
            (By.XPATH,'/html/body/div[1]/div[2]/section[1]/main/div/div/div/section/div[2]/div[2]/aside[1]/a/p'),  # home page job xpath
            (By.XPATH,'/html/body/div[1]/div[2]/section[1]/main/div/div/div/section/div[2]/div[2]/aside[3]/a/p'),  # home page funding xpath
            (By.XPATH,'/html/body/div[1]/div[2]/section[1]/main/div/div/div/section/div[2]/div[2]/aside[2]/a/p') # home page pjt xpath
        ]
        # Define a wait time
        wait = WebDriverWait(self.driver, 10)

        for by, selector in element_selectors:
            try:
                # # Attempt to find the element
                # element = self.driver.find_element(by, selector)
                # Wait for the element to be present
                element = wait.until(EC.presence_of_element_located((by, selector)))
                # Perform actions with the element (e.g., click, extract text, etc.)
                element.click()
                # print(element.text)
            except (NoSuchElementException, TimeoutException):
                # Skip to the next element if not found
                print(f'Element not found: {selector}')
                continue