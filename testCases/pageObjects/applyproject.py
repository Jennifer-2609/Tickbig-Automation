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


class applyproject:
    logger = LogGen.loggen()

    whocanapply_account1_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[9]/div/div/div[2]/div/div[1]"
    whocanapply_account2_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[12]/div/div/div[2]/div/div[1]"

    # review,save,report,copy link, not interest
    pjtapply_button_xpath = "//button[text()='Apply']"
    savepjt_button_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div[1]/main/section[2]/div/div/main/main[1]/div[6]/div/button[2]/img"
    pjtthreedots_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div[1]/main/section[2]/div/div/main/main[1]/div[1]/div[3]/div/button/img"
    pjtreview_xpath = "//p[text()='Write a review']"
    pjtnotinterest_xpath = "//button[text()='Not interested']"
    pjtnotinterestYes_xpath = "//button[text()='Yes']"
    pjtreport_xpath = "//p[text()='Report']"
    pjtcopylink_xpath = "//p[text()='CopyLink']"

    pjtrating_xpath = "/html/body/div[4]/div[3]/span/label[4]"
    pjtreviewtxt_xpath = "/html/body/div[4]/div[3]/textarea"
    pjtreviewsubmit_xpath = "/html/body/div[4]/div[3]/div/button[2]"

    pjtreporttxt_xpath = "/html/body/div[4]/div[3]/textarea"
    pjtreportsubmit_xpath = "/html/body/div[4]/div[3]/div/button[2]"

    # project type apply
    pjtdeliver_xpath = "/html/body/div[4]/div[3]/form/div[2]/input"
    pjtbidamount_xpath = "/html/body/div[4]/div[3]/form/div[3]/input"
    uploadproposaldoc_xpath = "/html/body/div[4]/div[3]/form/div[4]/input"
    pjtproposaldesc_xpath = "/html/body/div[4]/div[3]/form/div[6]/textarea"
    onbehalfofpjtapply_toggle_xpath = "/html/body/div[4]/div[3]/form/div[7]/label/span[1]/span[1]/input"
    pjtapply_behalfchooseone_xpath = "/html/body/div[4]/div[3]/form/div[7]/div/div"
    pjttypesubmit_xpath = "/html/body/div[4]/div[3]/form/div[8]/button[2]"

    # Staff augmentation apply
    pjtprofiletrackerupload_xpath = "/html/body/div[4]/div[3]/form/div[2]/input"
    pjtprofileupload_xpath = "/html/body/div[4]/div[3]/form/div[3]/input"
    pjtstaffapplydesc_xpath = "/html/body/div[4]/div[3]/div/form/textarea"
    onbehalfofstaffapply_toggle_xpath = "/html/body/div[4]/div[3]/form/div[4]/label/span[1]/span[1]/input"
    staffapply_behalfchooseone_xpath = "/html/body/div[4]/div[3]/form/div[4]/div/div"
    staffapplysubmit_xpath = "//button[text()='Submit']"

    # open,close,applied,save pjt
    # profilenavbardroparrow_xpath="/html/body/div[1]/section[1]/nav/main/div[1]/aside[1]/div/span"
    # profilenavbardroparrow_xpath="/html/body/div[1]/div[2]/section[1]/main/nav/main/div[1]/aside[1]/div/span"
    profilenavbardroparrow_xpath = "//p[text()='Me']"
    pjtdownarrow_xpath = "//p[text()='Projects']"
    openpjt_xpath = "/html/body/div[1]/div[2]/section[1]/main/nav/main/div[1]/aside[1]/div/div/div/div[4]/div[2]/div/div/div/div/ul/li[2]/div/div/span"
    openpjt3dots_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div[1]/main/section[2]/div/div/main/main[1]/div[1]/div[3]/div/button/img"
    openpjtclose_xpath = "//p[text()='Close']"
    closedpjt_button_xpath = "//a[text()='Closed']"
    closedpjtrepost_xpath = "//button[text()='Repost']"
    pjtrepost_button_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[8]/button[2]/span[1]"
    appliedpjt_button_xpath = "/html/body/div[1]/div[2]/section[1]/main/nav/main/div[1]/aside[1]/div/div/div/div[4]/div[2]/div/div/div/div/ul/li[4]/div/div/span"
    savedpjt_button_xpath = "/html/body/div[1]/div[2]/section[1]/main/nav/main/div[1]/aside[1]/div/div/div/div[4]/div[2]/div/div/div/div/ul/li[5]/div/div/span"

    def __init__(self, driver):
        self.driver = driver

    def clickPjtSave(self):
        self.driver.find_element(By.XPATH, self.savepjt_button_xpath).click()

    def clickPjtthreedots(self):
        self.driver.find_element(By.XPATH, self.pjtthreedots_xpath).click()

    def clickPjtApply(self):
        self.driver.find_element(By.XPATH, self.pjtapply_button_xpath).click()

    def clickPjtdelivery(self):
        self.driver.find_element(By.XPATH, self.pjtdeliver_xpath).clear()
        self.driver.find_element(By.XPATH, self.pjtdeliver_xpath).send_keys("5")

    def clickBidamt(self):
        self.driver.find_element(By.XPATH, self.pjtbidamount_xpath).clear()
        self.driver.find_element(By.XPATH, self.pjtbidamount_xpath).send_keys("1000000")

    def uploadProposaldoc(self):
        self.driver.find_element(By.XPATH, self.uploadproposaldoc_xpath).send_keys("D://Python/S3details.pdf")

    def uploadProposaldoclarge(self):  # file too large
        self.driver.find_element(By.XPATH, self.uploadproposaldoc_xpath).send_keys("D://largefile.pdf")

    def uploadProposaldocincfile(self):  # incorrect file type
        self.driver.find_element(By.XPATH, self.uploadproposaldoc_xpath).send_keys("D://localfile.zip")

    def setpjtproposaldesc(self):
        self.driver.find_element(By.XPATH, self.pjtproposaldesc_xpath).clear()
        self.driver.find_element(By.XPATH, self.pjtproposaldesc_xpath).send_keys(
            "You can click on the ‘item to generate’ column and select the format you want content in.Below that, you can select if you want an HTML tag in your content or not")

    def clickonbehalfofpjtapply(self):
        self.driver.find_element(By.XPATH, self.onbehalfofpjtapply_toggle_xpath).click()

    def clickbehalfchooseonepjtapply(self):
        self.driver.find_element(By.XPATH, self.pjtapply_behalfchooseone_xpath).click()

    def clickpjttypesubmit(self):
        self.driver.find_element(By.XPATH, self.pjttypesubmit_xpath).click()

    def clickpjtcopylink(self):
        self.driver.find_element(By.XPATH, self.pjtcopylink_xpath).click()

    def clickPjtreview(self):
        self.driver.find_element(By.XPATH, self.pjtreview_xpath).click()

    def clickPjtreviewsubmit(self):
        self.driver.find_element(By.XPATH, self.pjtreviewsubmit_xpath).click()

    def clickPjtrating(self):
        self.driver.find_element(By.XPATH, self.pjtrating_xpath).click()

    def clickPjtreviewtext(self):
        self.driver.find_element(By.XPATH, self.pjtreviewtxt_xpath).send_keys("automation testing review")

    def clickpjtnotinterest(self):
        self.driver.find_element(By.XPATH, self.pjtnotinterest_xpath).click()

    def clickpjtnotinterestyes(self):
        self.driver.find_element(By.XPATH, self.pjtnotinterestYes_xpath).click()

    def clickpjtreport(self):
        self.driver.find_element(By.XPATH, self.pjtreport_xpath).click()

    def clickpjtreportsubmit(self):
        self.driver.find_element(By.XPATH, self.pjtreportsubmit_xpath).click()

    def clickpjtreporttext(self):
        self.driver.find_element(By.XPATH, self.pjtreporttxt_xpath).send_keys("automation testing report")

    def clickPjtdeliveryneg(self):
        self.driver.find_element(By.XPATH, self.pjtdeliver_xpath).send_keys(" ")

    def clickBidamtneg(self):
        self.driver.find_element(By.XPATH, self.pjtbidamount_xpath).send_keys(" ")

    def setpjtproposaldescneg(self):
        self.driver.find_element(By.XPATH, self.pjtproposaldesc_xpath).clear()
        self.driver.find_element(By.XPATH, self.pjtproposaldesc_xpath).send_keys("You can click")

    def clickPjtdeliveryneg1(self):
        self.driver.find_element(By.XPATH, self.pjtdeliver_xpath).send_keys("  abcdefgh@$%%$&  ")

    def clickBidamtneg1(self):
        self.driver.find_element(By.XPATH, self.pjtbidamount_xpath).send_keys("   abcdefgh@$%%$  ")

    # staff apply

    def uploadprofiletracker(self):
        self.driver.find_element(By.XPATH, self.pjtprofiletrackerupload_xpath).send_keys("D://Python/S3details.pdf")

    def uploadprofiletrackerlarge(self):  # large file
        self.driver.find_element(By.XPATH, self.pjtprofiletrackerupload_xpath).send_keys("D://largefile.pdf")

    def uploadprofiletrackerincfile(self):  # incorrect file type
        self.driver.find_element(By.XPATH, self.pjtprofiletrackerupload_xpath).send_keys("D://localfile.zip")

    def uploadpjtprofile(self):
        self.driver.find_element(By.XPATH, self.pjtprofileupload_xpath).send_keys(
            "C://Users/jenni/Downloads/localfile.zip")

    def uploadpjtprofilelarge(self):  # large file
        self.driver.find_element(By.XPATH, self.pjtprofileupload_xpath).send_keys("D://largefile.zip")

    def uploadpjtprofileincfile(self):  # incorrect file
        self.driver.find_element(By.XPATH, self.pjtprofileupload_xpath).send_keys("D://largefile.pdf")

    def setpjtstaffapplydescneg(self):
        self.driver.find_element(By.XPATH, self.pjtstaffapplydesc_xpath).clear()
        self.driver.find_element(By.XPATH, self.pjtstaffapplydesc_xpath).send_keys("You can click")

    def setpjtstaffapplydesc(self):
        self.driver.find_element(By.XPATH, self.pjtstaffapplydesc_xpath).clear()
        self.driver.find_element(By.XPATH, self.pjtstaffapplydesc_xpath).send_keys(
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s. Lorem Ipsum is simply dummy text")

    def clickonbehalfofstaffapply(self):
        self.driver.find_element(By.XPATH, self.onbehalfofstaffapply_toggle_xpath).click()

    def clickbehalfchooseonestaffapply(self):
        self.driver.find_element(By.XPATH, self.staffapply_behalfchooseone_xpath).click()

    def clickstaffapplysubmit(self):
        self.driver.find_element(By.XPATH, self.staffapplysubmit_xpath).click()

    def scrollstaffapplysubmit(self):
        Button = self.driver.find_element(By.XPATH, self.staffapplysubmit_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Button)

    # open,close,applied,save pjt

    def clickprofilenavbardroparrow(self):
        self.driver.find_element(By.XPATH, self.profilenavbardroparrow_xpath).click()

    def clickpjtdownarrow(self):
        self.driver.find_element(By.XPATH, self.pjtdownarrow_xpath).click()

    def clickopenpjt(self):
        self.driver.find_element(By.XPATH, self.openpjt_xpath).click()

    def clickopenpjt3dots(self):
        self.driver.find_element(By.XPATH, self.openpjt3dots_xpath).click()

    def clickopenpjtclose(self):
        self.driver.find_element(By.XPATH, self.openpjtclose_xpath).click()

    def clickclosedpjt(self):
        self.driver.find_element(By.XPATH, self.closedpjt_button_xpath).click()

    def clickclosedpjtrepost(self):
        self.driver.find_element(By.XPATH, self.closedpjtrepost_xpath).click()

    def scrollpjtrepostbutton(self):
        Button = self.driver.find_element(By.XPATH, self.pjtrepost_button_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Button)

    def clickpjtrepostbutton(self):
        self.driver.find_element(By.XPATH, self.pjtrepost_button_xpath).click()

    def clickappliedpjt(self):
        self.driver.find_element(By.XPATH, self.appliedpjt_button_xpath).click()

    def clicksavedpjt(self):
        self.driver.find_element(By.XPATH, self.savedpjt_button_xpath).click()

    def selectWhocanapplyAccount1(self):  # Student
        self.driver.find_element(By.XPATH, self.whocanapply_account1_xpath).click()

    def selectWhocanapplyAccount2(self):  # Student
        self.driver.find_element(By.XPATH, self.whocanapply_account2_xpath).click()
