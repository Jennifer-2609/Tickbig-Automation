from telnetlib import EC

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from utilities.customLogger import LogGen

class profileA:

    logger = LogGen.loggen()

    # path to edu & exp
    btn_editEduExp_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[5]/section/div[1]/div/i"
    btn_addExp_xpath="/html/body/div[3]/div[3]/main/section/div[3]/div/div/div[1]/div/div/form/div[2]/span"
    txt_designExp_xpath="/html/body/div[3]/div[3]/main/section/div[3]/div/div/div[1]/div/div/form/div[2]/div/div[1]/input"
    txt_compnameExp_xpath="/html/body/div[3]/div[3]/main/section/div[3]/div/div/div[1]/div/div/form/div[2]/div/div[2]/input"
    txt_joblocExp_xpath="/html/body/div[3]/div[3]/main/section/div[3]/div/div/div[1]/div/div/form/div[2]/div/div[3]/input"
    txt_emptypeExp_xpath="/html/body/div[3]/div[3]/main/section/div[3]/div/div/div[1]/div/div/form/div[2]/div/div[4]/div/div/div[1]/div[2]"
    txt_startyrExp_xpath="/html/body/div[3]/div[3]/main/section/div[3]/div/div/div[1]/div/div/form/div[2]/div/div[5]/input"
    txt_endyrExp_xpath="/html/body/div[3]/div[3]/main/section/div[3]/div/div/div[1]/div/div/form/div[2]/div/div[6]/input"
    btn_saveExp_xpath="/html/body/div[3]/div[3]/main/section/div[3]/div/div/div[1]/div/div/form/div[3]/button"
    btn_delExp_xpath="/html/body/div[3]/div[3]/main/section/div[3]/div/div/div[1]/div/div/form/div[2]/div/span"
    btn_saveExpDel_xpath="/html/body/div[3]/div[3]/main/section/div[3]/div/div/div[1]/div/div/form/div[2]/button"
    mousehover_expcard_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[5]/section/section/section[1]/div/div[1]"
    btn_binExp_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[5]/section/section/section[1]/div/div[2]/button/span/svg/path"
    fullTime_xpath="/html/body/div[3]/div[3]/main/section/div[3]/div/div/div[1]/div/div/form/div[2]/div/div[4]/div/div[2]/div/div[1]"
    partTime_xpath="/html/body/div[3]/div[3]/main/section/div[3]/div/div/div[1]/div/div/form/div[2]/div/div[4]/div/div[2]/div/div[2]"
    mousehover_pjtcard_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[5]/section/section/section[1]/div/div[1]"
    btn_delexpbin_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[5]/section/section/section[1]/div/div[1]/button"

    btn_education_xpath="/html/body/div[3]/div[3]/main/section/div[2]/div[1]/div/div/button[2]"
    btn_addEdu_xpath="/html/body/div[3]/div[3]/main/section/div[3]/div/div/div[2]/div/div/form/div[2]/span"
    btn_eduQualification_xpath="/html/body/div[3]/div[3]/main/section/div[3]/div/div/div[2]/div/div/form/div[2]/div/div[1]/input"
    btn_instnameEdu_xpath="/html/body/div[3]/div[3]/main/section/div[3]/div/div/div[2]/div/div/form/div[2]/div/div[2]/input"
    btn_instlocEdu_xpath="/html/body/div[3]/div[3]/main/section/div[3]/div/div/div[2]/div/div/form/div[2]/div/div[3]/input"
    btn_startyrEdu_xpath="/html/body/div[3]/div[3]/main/section/div[3]/div/div/div[2]/div/div/form/div[2]/div/div[4]/input"
    btn_endyrEdu_xpath="/html/body/div[3]/div[3]/main/section/div[3]/div/div/div[2]/div/div/form/div[2]/div/div[5]/input"
    btn_saveEdu_xpath="/html/body/div[3]/div[3]/main/section/div[3]/div/div/div[2]/div/div/form/div[3]/button"
    btn_delEdu_xpath="/html/body/div[3]/div[3]/main/section/div[3]/div/div/div[2]/div/div/form/div[2]/div/button/span"
    btn_saveEduDel_xpath="/html/body/div[3]/div[3]/main/section/div[3]/div/div/div[2]/div/div/form/div[2]/button"
    btn_profileEducation_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[5]/section/div[2]/div[2]/button"

    # path to achievements
    btn_editachievement_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[7]/section/div[2]/div/i"
    btn_addachievement_xpath="/html/body/div[3]/div[3]/div/div[2]/main/section/div[2]/form/div[2]/span"
    text_achievetitle_xpath="/html/body/div[3]/div[3]/div/div[2]/main/section/div[2]/form/div[2]/div/div[1]/div/input"
    text_achievedescription_xpath="/html/body/div[3]/div[3]/div/div[2]/main/section/div[2]/form/div[2]/div/div[2]/textarea"
    btn_achievesubmit_xpath="/html/body/div[3]/div[3]/div/div[2]/main/section/div[2]/form/div[3]/button"
    btn_achieveDel_xpath="/html/body/div[3]/div[3]/div/div[2]/main/section/div[2]/form/div[2]/div/button"
    btn_achieveDelSubmit_xpath="/html/body/div[3]/div[3]/div/div[2]/main/section/div[2]/form/div[2]/button"
    mousehover_achievecard_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[7]/section/main/div/div/div/div/ul/li[2]/main/div/div"
    btn_binachieve_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[7]/section/main/div/div/div/div/ul/li[2]/main/div/div/button"

    # path to milestone
    btn_editMilestone_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[7]/section/div[2]"
    btn_addMilestone_xpath="/html/body/div[3]/div[3]/div/div[2]/main/section/div[2]/form/div[2]/span"
    text_yearMilestone_xpath="/html/body/div[3]/div[3]/div/div[2]/main/section/div[2]/form/div[2]/div/div[1]/input"
    text_descriptionMilestone_xpath="/html/body/div[3]/div[3]/div/div[2]/main/section/div[2]/form/div[2]/div/div[2]/textarea"
    btn_saveMilestone_xpath="/html/body/div[3]/div[3]/div/div[2]/main/section/div[2]/form/div[3]/button"
    btn_delMilestone_xpath="/html/body/div[3]/div[3]/div/div[2]/main/section/div[2]/form/div[2]/div/button"
    btn_delSaveMilestone_xpath="/html/body/div[3]/div[3]/div/div[2]/main/section/div[2]/form/div[2]/button"
    btn_binMilestoneDel_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[7]/section/main/div/div/div/i"

    # path to social media footer
    btn_editFooter_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[11]/section/section/div[2]/div"
    txt_FB_xpath="/html/body/div[3]/div[3]/div/div/main/section/form/div[1]/div[1]/div/div/input"
    txt_Twitter_xpath="/html/body/div[3]/div[3]/div/div/main/section/form/div[1]/div[2]/div/div/input"
    txt_LinkedIn_xpath="/html/body/div[3]/div[3]/div/div/main/section/form/div[2]/div[1]/div/div/input"
    txt_Insta_xpath="/html/body/div[3]/div[3]/div/div/main/section/form/div[2]/div[2]/div/div/input"
    txt_Website_xpath="/html/body/div[3]/div[3]/div/div/main/section/form/div[3]/div/div/div/input"
    btn_saveFooter_xpath="/html/body/div[3]/div[3]/div/div/main/section/form/div[4]/button"

    btn_Twitterlink_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[9]/section/section/div[1]/a[1]"
    btn_FBlink_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[9]/section/section/div[1]/a[2]"
    btn_LinkedInlink_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[9]/section/section/div[1]/a[3]"
    btn_Instalink_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[9]/section/section/div[1]/a[4]"
    btn_Websitelink_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[9]/section/section/div[1]/a[5]"


    def __init__(self, driver):
        self.driver = driver

    def scrollEduExp(self):
        Button = self.driver.find_element(By.XPATH, self.btn_editEduExp_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Button)

    def clickEduExp(self):
        self.driver.find_element(By.XPATH, self.btn_editEduExp_xpath).click()

    def clickAddExp(self):
        self.driver.find_element(By.XPATH, self.btn_addExp_xpath).click()

    def textdesignExp(self,ExpDesgination):
        self.driver.find_element(By.XPATH, self.txt_designExp_xpath).send_keys(ExpDesgination)

    def textcompnameExp(self,ExpCompname):
        self.driver.find_element(By.XPATH, self.txt_compnameExp_xpath).send_keys(ExpCompname)

    def textjoblocExp(self,JobLocation):
        self.driver.find_element(By.XPATH, self.txt_joblocExp_xpath).send_keys(JobLocation)

    # def clickemptypeExp(self):
    #     self.driver.find_element(By.XPATH, self.txt_emptypeExp_xpath).click()


    def selectEmploymenttype(self):
        # Locate the dropdown-like element
        dropdown_element = self.driver.find_element(By.XPATH, self.txt_emptypeExp_xpath)
        # Click on the dropdown-like element to open it
        dropdown_element.click()
        # Locate and click on the specific option within the dropdown-like element
        option_element = self.driver.find_element(By.XPATH, self.partTime_xpath)
        option_element.click()

        # This Select will work when it has <select> not in <div> tag
        # dropdown_element = self.driver.find_element(By.XPATH, self.txt_emptypeExp_xpath)
        # dropdown = Select(dropdown_element)
        # # Method 1: Select option by visible text
        # dropdown.select_by_visible_text("Part Time")

        # Method 2: Select option by value
        # dropdown.select_by_value("value_1")

        # Method 3: Select option by index (0-based)
        # dropdown.select_by_index(0)
        # self.driver.find_element(By.XPATH, self.txt_emptypeExp_xpath).send_keys(types)

    def textstartyrExp(self,StartYearExp):
        self.driver.find_element(By.XPATH, self.txt_startyrExp_xpath).send_keys(StartYearExp)

    def textendyrExp(self,EndYearExp):
        self.driver.find_element(By.XPATH, self.txt_endyrExp_xpath).send_keys(EndYearExp)

    def clickSaveExp(self):
        self.driver.find_element(By.XPATH, self.btn_saveExp_xpath).click()

    def mousehoverexpcardDel(self):
        # self.driver.find_element(By.XPATH, self.mousehover_pjtcard_xpath).click()

        # Find the element to hover over
        element_to_hover_over = self.driver.find_element(By.XPATH, self.mousehover_pjtcard_xpath)

        # Create an ActionChains object
        action_chains = ActionChains(self.driver)

        # Perform the mouse hover action
        action_chains.move_to_element(element_to_hover_over).perform()

        # After performing the hover action, you can interact with the elements that appear after the hover
        # For example, you can click on an element that appears after the hover
        element_to_click = self.driver.find_element(By.XPATH, self.btn_delexpbin_xpath)
        element_to_click.click()


    # Education

    def clickEducation(self):
        self.driver.find_element(By.XPATH, self.btn_education_xpath).click()

    def clickAddEdu(self):
        self.driver.find_element(By.XPATH, self.btn_addEdu_xpath).click()

    def textQualificationEdu(self,qualification):
        self.driver.find_element(By.XPATH, self.btn_eduQualification_xpath).send_keys(qualification)

    def textInstnameEdu(self,instname):
        self.driver.find_element(By.XPATH, self.btn_instnameEdu_xpath).send_keys(instname)

    def textInstlocExp(self,InstLocation):
        self.driver.find_element(By.XPATH, self.btn_instlocEdu_xpath).send_keys(InstLocation)

    def textstartyrEdu(self,StartYearEdu):
        self.driver.find_element(By.XPATH, self.btn_startyrEdu_xpath).send_keys(StartYearEdu)

    def scrollendyrEdu(self):
        Button = self.driver.find_element(By.XPATH, self.txt_endyrExp_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Button)

    def textendyrEdu(self,EndYearEdu):
        # Wait for an element to be clickable
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.btn_endyrEdu_xpath))
            )
            # Once the element is clickable, perform actions on it
            element.click()
            element.send_keys(EndYearEdu)
        except TimeoutException:
            print("Element not found within the specified time.")
        # self.driver.find_element(By.XPATH, self.txt_endyrExp_xpath).send_keys(EndYearEdu)
        # element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "txt_endyrExp_xpath")))
        # element.send_keys(EndYearEdu)
        # element = self.driver.find_element(By.XPATH, self.txt_endyrExp_xpath).click()
        # element.send_keys(EndYearEdu)

    def clickSaveEdu(self):
        self.driver.find_element(By.XPATH, self.btn_saveEdu_xpath).click()

    def clickDelExp(self):
        self.driver.find_element(By.XPATH, self.btn_delExp_xpath).click()

    def clicksaveExpDel(self):
        self.driver.find_element(By.XPATH, self.btn_saveExpDel_xpath).click()

    def clickDelEdu(self):
        self.driver.find_element(By.XPATH, self.btn_delEdu_xpath).click()

    def clicksaveEduDel(self):
        self.driver.find_element(By.XPATH, self.btn_saveEduDel_xpath).click()

    def scrollSaveEdu(self):
        Button = self.driver.find_element(By.XPATH, self.btn_saveEdu_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Button)

    def validatestartyrEdu(self):
        self.driver.find_element(By.XPATH, self.btn_startyrEdu_xpath).send_keys("StartYearEdu")

    def validateendyrEdu(self):
        # Wait for an element to be clickable
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.btn_endyrEdu_xpath))
            )
            # Once the element is clickable, perform actions on it
            element.click()
            element.send_keys("EndYearEdu")
        except TimeoutException:
            print("Element not found within the specified time.")


    # Achievements functions

    def scrollAchieve(self):
        Button = self.driver.find_element(By.XPATH, self.btn_editachievement_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Button)

    def clickEditachieve(self):
        self.driver.find_element(By.XPATH, self.btn_editachievement_xpath).click()

    def clickAddachieve(self):
        self.driver.find_element(By.XPATH, self.btn_addachievement_xpath).click()

    def textAchievetitle(self,AchieveTitle):
        self.driver.find_element(By.XPATH, self.text_achievetitle_xpath).send_keys(AchieveTitle)

    def textAchievedescription(self,AchieveDescription):
        self.driver.find_element(By.XPATH, self.text_achievedescription_xpath).send_keys(AchieveDescription)

    def clickAchievesubmit(self):
        self.driver.find_element(By.XPATH, self.btn_achievesubmit_xpath).click()

    def clickAchieveDel(self):
        self.driver.find_element(By.XPATH, self.btn_achieveDel_xpath).click()

    def clickAchieveDelSubmit(self):
        self.driver.find_element(By.XPATH, self.btn_achieveDelSubmit_xpath).click()

    def textAchievedescriptionnew(self,AchieveDescriptionnew):
        self.driver.find_element(By.XPATH, self.text_achievedescription_xpath).send_keys(AchieveDescriptionnew)

    def textAchievedescriptionmax(self,AchieveDescriptionmax):
        self.driver.find_element(By.XPATH, self.text_achievedescription_xpath).send_keys(AchieveDescriptionmax)

    def mousehoverachievecardDel(self):
        # Find the element to hover over
        element_to_hover_over = self.driver.find_element(By.XPATH, self.mousehover_achievecard_xpath)
        # Create an ActionChains object
        action_chains = ActionChains(self.driver)
        # Perform the mouse hover action
        action_chains.move_to_element(element_to_hover_over).perform()
        # After performing the hover action, you can interact with the elements that appear after the hover
        # For example, you can click on an element that appears after the hover
        element_to_click = self.driver.find_element(By.XPATH, self.btn_binachieve_xpath)
        element_to_click.click()


    # Milestone functions

    def scrollEditMilestone(self):
        Button = self.driver.find_element(By.XPATH, self.btn_editMilestone_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Button)

    def clickEditMilestone(self):
        self.driver.find_element(By.XPATH, self.btn_editMilestone_xpath).click()

    def clickAddMilestone(self):
        self.driver.find_element(By.XPATH, self.btn_addMilestone_xpath).click()

    def textyearMilestone(self,MilestoneYear):
        self.driver.find_element(By.XPATH, self.text_yearMilestone_xpath).send_keys(MilestoneYear)

    def textInvalidyr(self,InvalidYear):
        self.driver.find_element(By.XPATH, self.text_yearMilestone_xpath).send_keys(InvalidYear)

    def textMilestonedescription(self,MilestoneDescription):
        self.driver.find_element(By.XPATH, self.text_descriptionMilestone_xpath).send_keys(MilestoneDescription)

    def clickSaveMilestone(self):
        self.driver.find_element(By.XPATH, self.btn_saveMilestone_xpath).click()

    def clickDelMilestone(self):
        self.driver.find_element(By.XPATH, self.btn_delMilestone_xpath).click()

    def clickDelSaveMilestone(self):
        self.driver.find_element(By.XPATH, self.btn_delSaveMilestone_xpath).click()

    def txtMSDescripAtLeast(self,MSDescriptionAtLeast):
        self.driver.find_element(By.XPATH, self.text_descriptionMilestone_xpath).send_keys(MSDescriptionAtLeast)

    def txtMSDescripMaxChar(self,MSDescriptionMaxChar):
        self.driver.find_element(By.XPATH, self.text_descriptionMilestone_xpath).send_keys(MSDescriptionMaxChar)

    def clickBinDelMilestone(self):
        self.driver.find_element(By.XPATH, self.btn_binMilestoneDel_xpath).click()

    # Footer functions (Social media)

    def scrollEditfooter(self):
        Button = self.driver.find_element(By.XPATH, self.btn_editFooter_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Button)

    def clickEditfooter(self):
        self.driver.find_element(By.XPATH, self.btn_editFooter_xpath).click()

    def txtFB(self):
        self.driver.find_element(By.XPATH, self.txt_FB_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_FB_xpath).send_keys("https://www.facebook.com/")

    def txtTwitter(self):
        self.driver.find_element(By.XPATH, self.txt_Twitter_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_Twitter_xpath).send_keys("https://twitter.com/")

    def txtInsta(self):
        self.driver.find_element(By.XPATH, self.txt_Insta_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_Insta_xpath).send_keys("https://www.instagram.com/")

    def txtLinkedIn(self):
        self.driver.find_element(By.XPATH, self.txt_LinkedIn_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_LinkedIn_xpath).send_keys("https://in.linkedin.com/")

    def txtWebsite(self):
        self.driver.find_element(By.XPATH, self.txt_Website_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_Website_xpath).send_keys("https://www.google.com/")

    def clickSavefooter(self):
        self.driver.find_element(By.XPATH, self.btn_saveFooter_xpath).click()

    def clickTwitterlink(self):
        self.driver.find_element(By.XPATH, self.btn_Twitterlink_xpath).click()
        # Wait for the new window to open
        new_window_handle = WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))

        # Switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[1])

        # Now you can perform actions on the new window
        # For example, get the current URL
        # print("Current URL of the new window:", self.driver.current_url)
        self.logger.info("Twitter URL is: %s", self.driver.current_url)
        self.driver.save_screenshot(".\\Screenshots\\" + "Twitter.png")
        # Close the new window
        self.driver.close()

        # Switch back to the original window
        self.driver.switch_to.window(self.driver.window_handles[0])

        # Perform actions on the original window
        # For example, get the title
        # print("Title of the original window:", self.driver.title)

    def clickFBlink(self):
        self.driver.find_element(By.XPATH, self.btn_FBlink_xpath).click()

        new_window_handle = WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.logger.info("FaceBook URL is: %s", self.driver.current_url)
        self.driver.save_screenshot(".\\Screenshots\\" + "FB.png")
        self.driver.close() # Close the new window
        self.driver.switch_to.window(self.driver.window_handles[0]) # Switch back to the original window

    def clickLinkedinlink(self):
        self.driver.find_element(By.XPATH, self.btn_LinkedInlink_xpath).click()

        new_window_handle = WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.logger.info("LinkedIn URL is: %s", self.driver.current_url)
        self.driver.save_screenshot(".\\Screenshots\\" + "LinkedIn.png")
        self.driver.close()  # Close the new window
        self.driver.switch_to.window(self.driver.window_handles[0])  # Switch back to the original window
    def clickInstalink(self):
        self.driver.find_element(By.XPATH, self.btn_Instalink_xpath).click()

        new_window_handle = WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.logger.info("Instagram URL is: %s", self.driver.current_url)
        self.driver.save_screenshot(".\\Screenshots\\" + "Insta.png")
        self.driver.close()  # Close the new window
        self.driver.switch_to.window(self.driver.window_handles[0])  # Switch back to the original window

    def clickWebsitelink(self):
        self.driver.find_element(By.XPATH, self.btn_Websitelink_xpath).click()

        new_window_handle = WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.logger.info("Website URL is: %s", self.driver.current_url)
        self.driver.save_screenshot(".\\Screenshots\\" + "Website.png")
        self.driver.close()  # Close the new window
        self.driver.switch_to.window(self.driver.window_handles[0])  # Switch back to the original window

