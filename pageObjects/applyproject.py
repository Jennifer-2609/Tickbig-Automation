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


    # review,save,report,copy link, not interest
    pjtapply_button_xpath="/html/body/div[1]/section[1]/main/div/div[1]/main/section[2]/div/div/main/main[1]/div[6]/div/button[1]"
    savepjt_button_xpath="/html/body/div[1]/section[1]/main/div/div[1]/main/section[2]/div/div/main/main[1]/div[6]/div/button[2]/img"
    pjtthreedots_xpath="/html/body/div[1]/section[1]/main/div/div[1]/main/section[2]/div/div/main/main[1]/div[1]/div[3]/div/button/img"
    pjtreview_xpath="/html/body/div[4]/div[3]/ul/div/li[2]/p"
    pjtnotinterest_xpath="/html/body/div[4]/div[3]/ul/div/li[3]/button"
    pjtnotinterestYes_xpath="/html/body/div[5]/div/div/div[2]/section/div/button[1]"
    pjtreport_xpath="/html/body/div[4]/div[3]/ul/div/li[4]/p"
    pjtcopylink_xpath="/html/body/div[4]/div[3]/ul/div/li[1]/p"

    pjtrating_xpath="/html/body/div[4]/div[3]/span/label[4]"
    pjtreviewtxt_xpath="/html/body/div[4]/div[3]/textarea"
    pjtreviewsubmit_xpath="/html/body/div[4]/div[3]/div/button[2]"

    pjtreporttxt_xpath="/html/body/div[4]/div[3]/textarea"
    pjtreportsubmit_xpath="/html/body/div[4]/div[3]/div/button[2]"

    # project type apply
    pjtdeliver_xpath="/html/body/div[4]/div[3]/form/div[2]/input"
    pjtbidamount_xpath="/html/body/div[4]/div[3]/form/div[3]/input"
    uploadproposaldoc_xpath = "/html/body/div[4]/div[3]/form/div[4]/input"
    pjtproposaldesc_xpath="/html/body/div[4]/div[3]/form/div[6]/textarea"
    onbehalfofpjtapply_toggle_xpath="/html/body/div[4]/div[3]/form/div[7]/label/span[1]/span[1]/input"
    pjtapply_behalfchooseone_xpath="/html/body/div[4]/div[3]/form/div[7]/div/div"
    pjttypesubmit_xpath="/html/body/div[4]/div[3]/form/div[8]/button[2]"


    # Staff augmentation apply
    pjtprofiletrackerupload_xpath="/html/body/div[4]/div[3]/form/div[2]/input"
    pjtprofileupload_xpath="/html/body/div[4]/div[3]/form/div[3]/input"
    pjtstaffapplydesc_xpath="/html/body/div[4]/div[3]/form/textarea"
    onbehalfofstaffapply_toggle_xpath="/html/body/div[4]/div[3]/form/div[4]/label/span[1]/span[1]/input"
    staffapply_behalfchooseone_xpath="/html/body/div[4]/div[3]/form/div[4]/div/div"
    staffapplysubmit_xpath="/html/body/div[4]/div[3]/form/div[5]/button[2]"

    # open,close,applied,save pjt
    profilenavbardroparrow_xpath="/html/body/div[1]/section[1]/nav/main/div[1]/aside[1]/div/span"
    pjtdownarrow_xpath="/html/body/div[1]/section[1]/nav/main/div[1]/aside[1]/div/div/div/div[2]/div[1]/div[3]/h2/button"
    openpjt_xpath="/html/body/div[1]/section[1]/nav/main/div[1]/aside[1]/div/div/div/div[2]/div[1]/div[3]/div/p[2]"
    openpjt3dots_xpath="/html/body/div[1]/section[1]/main/div/div[1]/main/section[2]/div/div/main/main[1]/div[1]/div[3]/div/button/img"
    openpjtclose_xpath="/html/body/div[3]/div[3]/ul/div/li[2]/p"
    closedpjt_button_xpath="/html/body/div[1]/section[1]/main/div/div[1]/main/section[1]/div[2]/a[2]"
    closedpjtrepost_xpath="/html/body/div[1]/section[1]/main/div/div[1]/main/section[2]/div/div/main/main[1]/div[6]/div/button[2]"
    pjtrepost_button_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[5]/button[2]/span[1]"
    appliedpjt_button_xpath="/html/body/div[1]/section[1]/nav/main/div[1]/aside[1]/div/div/div/div[2]/div[1]/div[3]/div/p[4]"
    savedpjt_button_xpath="/html/body/div[1]/section[1]/main/div/div[1]/main/section[1]/div[2]/a[2]"


    def __init__(self, driver):
        self.driver = driver

    def clickPjtSave(self):
        self.driver.find_element(By.XPATH, self.savepjt_button_xpath).click()

    def clickPjtthreedots(self):
        self.driver.find_element(By.XPATH, self.pjtthreedots_xpath).click()

    def clickPjtApply(self):
        self.driver.find_element(By.XPATH,self.pjtapply_button_xpath).click()

    def clickPjtdelivery(self):
        self.driver.find_element(By.XPATH, self.pjtdeliver_xpath).clear()
        self.driver.find_element(By.XPATH, self.pjtdeliver_xpath).send_keys("5")

    def clickBidamt(self):
        self.driver.find_element(By.XPATH, self.pjtbidamount_xpath).clear()
        self.driver.find_element(By.XPATH, self.pjtbidamount_xpath).send_keys("1000000")

    def uploadProposaldoc(self):
        self.driver.find_element(By.XPATH, self.uploadproposaldoc_xpath).send_keys("D://Python/S3details.pdf")

    def setpjtproposaldesc(self):
        self.driver.find_element(By.XPATH, self.pjtproposaldesc_xpath).clear()
        self.driver.find_element(By.XPATH, self.pjtproposaldesc_xpath).send_keys("You can click on the ‘item to generate’ column and select the format you want content in.Below that, you can select if you want an HTML tag in your content or not")

    def clickonbehalfofpjtapply(self):
        self.driver.find_element(By.XPATH, self.onbehalfofpjtapply_toggle_xpath).click()

    def clickbehalfchooseonepjtapply(self):
        self.driver.find_element(By.XPATH, self.pjtapply_behalfchooseone_xpath).click()

    def clickpjttypesubmit(self):
        self.driver.find_element(By.XPATH, self.pjttypesubmit_xpath).click()

    def clickpjtcopylink(self):
        self.driver.find_element(By.XPATH, self.pjtcopylink_xpath).click()

        # # Open a new tab using JavaScript
        # self.driver.execute_script("window.open('');")
        # # Switch to the new tab
        # self.driver.switch_to.window(driver.window_handles[-1])
        # # Open a different webpage in the new tab
        # self.driver.get('http://another-example.com')  # Replace with the actual URL you want to open in the new tab
        # # Optionally, perform actions on the new tab
        # time.sleep(3)  # Wait for a few seconds to see the new tab (for demonstration purposes)
        # # Close the new tab
        # self.driver.close()
        # # Switch back to the original tab
        # self.driver.switch_to.window(driver.window_handles[0])
        # # Optionally, perform actions on the original tab
        # time.sleep(3)  # Wait for a few seconds to see the original tab (for demonstration purposes)
    def clickPjtreview(self):
        self.driver.find_element(By.XPATH, self.pjtreview_xpath).click()

    def clickPjtreviewsubmit(self):
        self.driver.find_element(By.XPATH, self.pjtreviewsubmit_xpath).click()

    def clickPjtrating(self):
        self.driver.find_element(By.XPATH, self.pjtrating_xpath).click()

    def clickPjtreviewtext(self):
        self.driver.find_element(By.XPATH, self.pjtreviewtxt_xpath).send_keys("automation testing review")

    def clickpjtnotinterest(self):
        self.driver.find_element(By.XPATH,self.pjtnotinterest_xpath).click()

    def clickpjtnotinterestyes(self):
        self.driver.find_element(By.XPATH, self.pjtnotinterestYes_xpath).click()

    def clickpjtreport(self):
        self.driver.find_element(By.XPATH,self.pjtreport_xpath).click()

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

    def uploadpjtprofile(self):
        self.driver.find_element(By.XPATH, self.pjtprofileupload_xpath).send_keys("C://Users/jenni/Downloads/localfile.zip")

    def setpjtstaffapplydescneg(self):
        self.driver.find_element(By.XPATH, self.pjtstaffapplydesc_xpath).clear()
        self.driver.find_element(By.XPATH, self.pjtstaffapplydesc_xpath).send_keys("You can click")

    def setpjtstaffapplydesc(self):
        self.driver.find_element(By.XPATH, self.pjtstaffapplydesc_xpath).clear()
        self.driver.find_element(By.XPATH, self.pjtstaffapplydesc_xpath).send_keys("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s. Lorem Ipsum is simply dummy text")

    def clickonbehalfofstaffapply(self):
        self.driver.find_element(By.XPATH, self.onbehalfofstaffapply_toggle_xpath).click()

    def clickbehalfchooseonestaffapply(self):
        self.driver.find_element(By.XPATH, self.staffapply_behalfchooseone_xpath).click()

    def clickstaffapplysubmit(self):
        self.driver.find_element(By.XPATH, self.staffapplysubmit_xpath).click()


    # open,close,applied,save pjt

    def clickprofilenavbardroparrow(self):
        self.driver.find_element(By.XPATH, self.profilenavbardroparrow_xpath).click()

        # try:
        #     # Wait for the profile navbar drop arrow to be clickable
        #     profilnavbardrop = WebDriverWait(self.driver, 10).until(
        #         EC.element_to_be_clickable((By.XPATH, self.profilenavbardroparrow_xpath))
        #     )
        #
        # except NoSuchElementException as e:
        #     self.logger.error("Profile Navbar Drop Arrow Element Not Found: %s", str(e))
        #     self.logger.debug("Page Source at Failure: %s", self.driver.page_source)
        #     self.driver.save_screenshot('screenshot.png')
        #     assert False, "Profile Navbar Drop Arrow element not found"
        # except Exception as e:
        #     self.logger.error("An error occurred: %s", str(e))
        #     self.driver.save_screenshot('screenshot.png')
        #     assert False, "An unexpected error occurred"

        # self.driver.find_element(By.XPATH, self.profilenavbardroparrow_xpath).click()

        # # Locate the element to hover over
        # element_to_hover_over = self.driver.find_element(By.XPATH, self.profilenavbardroparrow_xpath)
        # # Create an ActionChains object
        # actions = ActionChains(self.driver)
        # # Perform the mouse hover action
        # actions.move_to_element(element_to_hover_over).perform()
        # time.sleep(1)


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